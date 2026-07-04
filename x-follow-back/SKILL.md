---
name: x-follow-back
description: |
  @KURAOpenclaw アカウントをフォローした人への自動フォローバックを実行する。
  ブルーバッジ（認証済み）アカウントに限定・ジャンル不問。
  1日複数回cron実行、日次上限50件。
  以下のフレーズで起動する：
  - 「フォローバックを実行して」
  - 「follow-backを実行」
  - 「Xのフォローバック実行」
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始すること。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## タスク: @KURAOpenclaw フォローバック実行

**ステップ1: スクリプト実行**

PowerShellツールで以下のコマンドを実行する:
```
& 'C:\Program Files\nodejs\node.exe' 'C:\Users\sawas\.openclaw\workspace\tools\x-poster\follow-back.js' --count 15
```

**ステップ2: 結果確認**

実行完了後、`C:\Users\sawas\.openclaw\workspace\tools\x-poster\last_followback_result.json` を Read で読み込む（存在しない場合はstdout/stderrから判断）。

**ステップ3: Discord報告**

| exitCode | 報告内容 |
|---|---|
| 0 | `✅ フォローバック完了: ${followedBackToday}件 (累計: ${totalFollowedBack}件)` |
| 1 (エラー) | `❌ フォローバック失敗: エラー内容` |
| 3 (認証失敗) | `⚠️ フォローバック認証失敗: Cookie更新が必要。x_setup_launcher.pyを実行してください。` |

---

## ファイル構成

```
C:\Users\sawas\.openclaw\workspace\tools\x-poster\
├── follow-back.js             # フォローバックスクリプト本体
├── last_followback_result.json # 最終実行結果
├── followed_back.json         # フォローバック済みDB
└── logs\
    └── followback-YYYYMMDD.log # JSONL日次ログ
```

---

## 起動メッセージ形式（cronから呼ばれる際の形式）
```
【フォローバック実行 @KURAOpenclaw】
PowerShellツールで実行: & 'C:\Program Files\nodejs\node.exe' 'C:\Users\sawas\.openclaw\workspace\tools\x-poster\follow-back.js' --count 15
完了後にlast_followback_result.jsonを読んでDiscordに結果報告（exitCode 0: 件数報告 / 3: Cookie更新要求 / 1: エラー報告）
```

---

## Stealth Browser Integration (2026-06-26)

This skill's scripts use **stealth-config.js** + **CloakBrowser** (58 C++ patches) automatically.
Fallback: standard Playwright Chromium -> chrome channel -> headed off-screen.
Config: C:\Users\sawas\.openclaw\workspace\tools\x-poster\stealth-config.js