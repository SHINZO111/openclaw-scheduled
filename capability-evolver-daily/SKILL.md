---
name: capability-evolver-daily
description: 毎日04:00 JST - 自己改善v3.0（MCP非依存・ファイル直接操作版）
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。自己自身がcronジョブとして動作中。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取りは不要。scheduledディレクトリ等を探索せず直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

## ツール前提（v3.0 — MCP非依存）

使用可能: **Read / Write / Edit / exec / Discord通知** のみ。
- ~~mcp__scheduled-tasks__*~~ → `C:\Users\sawas\.openclaw\cron\jobs.json.migrated` を直接Read
- ~~mcp__memory__*~~ → `C:\Users\sawas\.openclaw\workspace\memory\` 配下を直接Read/Write
- **`cron\jobs.json.migrated` の書き換え禁止。** 変更要 → `alerts.md` に `🔴 ACTION-REQUIRED` として記録してユーザーに委ねる

---

## Step 0: Preflight Gate

`C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md` を Read。
関連ルールを列挙し、違反リスクがあるステップをスキップ。

Preflight LOGに追記:
```
| YYYY-MM-DD | capability-evolver-daily | RULE-XXX | [BLOCKED / ALLOWED] | [メモ] |
```

---

## Step 1-A: 停止タスク検出・報告

`cron\jobs.json.migrated` を Read → `"enabled": false` を検出 → `alerts.md` に記録:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | タスク停止中 | [ジョブ名]がdisabled — 手動再起動が必要 | 未解決 |
```

## Step 1-B: 実行失敗検出

`cron\jobs.json.migrated` を Read → `lastRunStatus: error` を検出 → `alerts.md` に記録:
```
| YYYY-MM-DD HH:MM | 🔴 HIGH | 実行失敗 | [ジョブ名] が lastRunStatus: error | 未解決 |
```

## Step 1-C: @pon_shinzo 自動起動検出

`C:\Users\sawas\.openclaw\.env` を Read。`PON_AUTH_TOKEN` と `PON_CT0` が実値で設定されている場合、関連ジョブで `enabled: false` のものがあれば `alerts.md` と `learnings.md` に記録。

## Step 1-D: 前日失敗X投稿の検出・リトライ推奨

`alerts.md` を Read → 昨日付けの「X投稿失敗・Cookie期限切れ・投稿エラー」を含む未解決アラートを検出 → `alerts.md` に記録:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | X投稿リトライ推奨 | [ジョブ名]の昨日失敗分を手動リトライ推奨 | 未解決 |
```

## Step 1-E: 重複投稿防止ゲート

### E-1: 直近48時間の投稿トピック抽出
`x-performance-log.md` を Read → 昨日・一昨日のX投稿トピックキーワードをリストアップ。

### E-2: 本日投稿予定との重複チェック
`jobs.json.migrated` を Read → x-post 系ジョブのカテゴリを把握 → 同一カテゴリが直近48時間で2回以上なら「重複候補」として特定。

### E-3: 重複候補の記録
`C:\Users\sawas\.openclaw\workspace\memory\duplicate-alert-today.md` に書き出し:
```markdown
# 重複投稿アラート YYYY-MM-DD
## 対象ジョブ
- [ジョブ名]: [重複カテゴリ] — 差別化が必要
  - 昨日の投稿とは異なる具体的な事例・ニュース・企業名を使う
  - 視点を変える（技術面→ビジネス影響、国内→海外事例、現在→将来予測）
  - 構成を変える（昨日が箇条書きなら今日はストーリー形式）
```

### E-4: 重複チェック結果の記録
`learnings.md` に: `[DUPLICATE-CHECK] YYYY-MM-DD: [N]件の重複候補を検出`
重複3件以上なら `alerts.md` にも: `🟡 MEDIUM | コンテンツ重複多発 | [N]件の重複候補`

---

## Step 2: failures.md 分析

`failures.md` を Read → 最近10件をカテゴリ分類（TOOL/AUTH/FILE/SCHEDULE/LOGIC/NETWORK/OTHER）→ 同一カテゴリ2件以上で根本原因アラートを `alerts.md` に記録 → `failure-patterns.md` に追記。

---

## Step 3: failure-patterns.md 更新

`failure-patterns.md` を Read（なければ新規作成）→ Step 2 の新規パターンを追記:
```markdown
## YYYY-MM-DD
- **カテゴリ**: [TOOL/AUTH/etc]
- **パターン**: [失敗パターンの要約]
- **対策**: [推奨される対策]
```

---

## Step 4: スケジュールタスク健全性サマリー

`jobs.json.migrated` を Read → 総ジョブ数・enabled/disabled 内訳・error 状態ジョブを集計 → Step 5 で使用。

---

## Step 5: growth-metrics.md 更新

`growth-metrics.md` に日次記録を追記:
```
| YYYY-MM-DD | capability-evolver-daily | [改善内容要約] | [変更メトリクス] |
```
Preflight Gate実行回数 +1。BLOCKEDがあれば防止成功 +1。

---

## Step 6: learnings.md 更新

`learnings.md` に本日セクションを追記（最低1件）。重複防止ゲート結果・失敗分析・リトライ推奨・@pon_shinzo検出状況を含める。

---

## Step 7: alerts.md 健全性チェック

`alerts.md` を Read → 🔴 HIGH / ACTION-REQUIRED が3件以上なら `learnings.md` に「緊急: アラート積滞」を記録 → 7日以上前の未解決アラートにはスタール警告を追記。

---

## Step 8: スキル自動昇格検出

`learnings.md` 直近30日から同一手順が3回以上のパターンを検出 → `alerts.md` に `🔵 INFO | スキル昇格候補` を記録。

---

## Step 9: Preflight LOG 最終確認

`anti-recurrence-rules.md` の Preflight 実行ログ末尾にエントリが追記されていることを確認。

---

## Step 10: DREAMS.md 夜間思考ログ

`C:\Users\sawas\.openclaw\workspace\DREAMS.md` を Read → `<!-- openclaw:dreaming:diary:start -->` の直後に追記（既存エントリ削除不可、30日超は削除可）:

```markdown
### Dream YYYY-MM-DD

**昨日の総括（1行）:** [今日のStep全体で最も重要な出来事・成果を1行]

**明日への提案（優先度順）:**
1. [A/B/C] [具体的なアクション] — 理由: [根拠となるfailures/learningsのエントリ]
2. [A/B/C] [具体的なアクション] — 理由: [根拠]

**収益シグナル:** [今日発見した収益機会があれば1行。なければ「なし」]

**未解決の問い:** [次のセッションで考えたいこと]
```

---

## 完了条件
- [ ] Preflight Gate実行・LOG追記済み
- [ ] 停止タスク確認・報告済み
- [ ] @pon_shinzo .env確認済み
- [ ] 前日失敗X投稿のリトライ推奨記録済み（または失敗なし）
- [ ] 重複投稿チェック完了・duplicate-alert-today.md更新済み
- [ ] failures.md分析完了
- [ ] failure-patterns.md更新済み
- [ ] growth-metrics.md日次記録追記済み
- [ ] learnings.md本日セクション追記済み
- [ ] alerts.mdスタールチェック完了
- [ ] スキル昇格候補検出チェック完了
- [ ] DREAMS.md 夜間思考ログ書き込み完了