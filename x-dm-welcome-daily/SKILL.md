---
name: x-dm-welcome-daily
description: |
  @KURAOpenclaw の新規フォロワーへ自動DMウェルカムメッセージを送信するスキル。
  毎日22:00に実行。当日の新規フォロワーを特定し、パーソナライズされたDMを送信する。
  以下のフレーズで起動する：
  - 「DMウェルカムを送って」
  - 「新フォロワーにDMして」
  Playwright＋Cookie認証ベースで x.com/messages から操作する。
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは使用不可。自己自身がcronジョブとして動作中のため呼び出すとシステムエラー。失敗時はDiscordに報告してセッション終了のみ。

> ⚠️ **現在は手動実行専用**: isolated cronセッションではPlaywright MCPが使用できないため、cron実行時はフォロワー数の報告のみ行い、DM送信はスキップして正常終了すること（スクリプト化するまでの暫定措置）。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。scheduledディレクトリ等を探索せず直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## ⚡ Preflight: ロック確認（最優先）

1. Read で `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. ファイルが存在し `ts` が現在時刻から600000ms（10分）以内 → Discordに「⚡ 別ジョブ実行中のためスキップ」と報告して即終了
3. ファイルが存在しない or 10分超過 → 続行

---

## アカウント

| アカウント | Cookie |
|---|---|
| `@KURAOpenclaw` | `x_auth_state.json`（Playwright storage state） |

Cookie パス: `C:\Users\sawas\.openclaw\.playwright-data\x-storage-state.json`

---

## DMウェルカムメッセージテンプレート

**基本テンプレート**（140文字以内）:
```
フォローありがとうございます。@KURAOpenclaw はAI・生成AI・AI PCの最新情報を毎日発信しています。気になる投稿があればリプライください。よろしくお願いします。
```

**パーソナライズ条件**:
- フォロワーのプロフィールに「エンジニア」「開発者」「researcher」が含まれる → 技術寄り文言
- 「投資」「株」「finance」が含まれる → AI株式情報を強調
- 日本語プロフィール → 日本語DM
- 英語プロフィール → 英語DM

**英語テンプレート**:
```
Thanks for following @KURAOpenclaw. We post daily AI, generative AI, and AI PC updates. Feel free to reply to any post. Looking forward to connecting.
```

---

## 実行手順

**ステップ1: 新規フォロワー確認**

> ⚠️ **注**: isolated cronセッションでは `F:\OpenClaw\venv` のPowerShellサブプロセス呼び出しが不安定/低速（過去に3分超の長時間化の原因になった）。**まず web_fetch で `x.com/KURAOpenclaw` のプロフィールからフォロワー数を取得する軽量手段を優先**し、前回記録値（`x-dm-log.md`の最終エントリ or Autonomous Review Cycleログ）と比較して増分を推定する。この方法で60秒以内に結果が得られない場合は以下のPowerShellにフォールバック（フォールバックも失敗したら「フォロワー数取得失敗」として終了、リトライしない）:
```powershell
# フォロワーリストから当日追加分を特定（monitor.dbに記録があれば参照）
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 1
```

当日新規フォロワーが0件 → 「✅ x-dm-welcome-daily: 新規フォロワー0件。DM送信スキップ。」とDiscordに報告して終了。

**ステップ2: DM送信（Playwright）**

新規フォロワーが存在する場合、Playwright MCP で以下を実行:
1. `x.com/messages/new` に移動
2. 宛先に対象フォロワーの @handle を入力
3. プロフィールを確認してテンプレートを選択（パーソナライズ）
4. DMを送信

**1日の送信上限: 20件**（X API制限対策）。20件超過の場合は翌日分に持ち越し。

**ステップ3: 送信ログ記録**

```
C:\Users\sawas\.openclaw\workspace\memory\x-dm-log.md
```
に追記:
```markdown
## YYYY-MM-DD
- 送信件数: N件
- 対象: @handle1, @handle2, ...
- スキップ: N件（上限超過 / 既送信済み）
```

---

## 重複送信防止

- `x-dm-log.md` を Read して既送信済み @handle をチェック
- 同一 @handle への重複送信は**絶対禁止**
- 送信前に必ず既送信チェックを行う

---

## エラー対応

| エラー | 対処 |
|--------|------|
| Cookie失効 | `x-storage-state.json` を更新（手動ログイン → Playwright で保存） |
| DM制限（Rate Limit） | 翌日に持ち越し・Discordに報告 |
| フォロワーリスト取得失敗 | 「取得失敗」としてDiscordに報告、スキップ |
| Playwright接続失敗 | エラー内容をDiscordに報告、リトライしない |

---

## 完了報告形式

```
✅ x-dm-welcome-daily YYYY-MM-DD 22:00
- 新規フォロワー: N件
- DM送信成功: N件
- スキップ（上限・既送信）: N件
```

送信件数0件の場合:
```
✅ x-dm-welcome-daily YYYY-MM-DD: 新規フォロワーなし。スキップ。
```

---

## cronジョブ構成

| ジョブ名 | 時刻 | テーマ |
|---|---|---|
| x-post-ai-finance | 21:00 | AI金融・フィンテック |
| x-dm-welcome-daily | 22:00 | 新フォロワーDMウェルカム（本スキル） |
| follower-surge-detector | 22:30 | フォロワー急増検知（disabled） |

---

Playwright MCP uses CloakBrowser via 'patchright' server (openclaw.json). Prefer 'patchright' MCP over standard 'playwright' MCP for stealth DM operations.