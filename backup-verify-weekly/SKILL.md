---
name: backup-verify-weekly
description: 毎週月曜05:20 JST。OpenClaw_Daily_Backupの成果物の存在・サイズ・更新日時を検証し、失敗検知時は原因（LastTaskResult）付きでDiscordへ警告する
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: cron.run / cron.list 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

## Step 1: タスク実行結果確認
PowerShellツールで実行:
```
Get-ScheduledTask "OpenClaw_Daily_Backup" | Get-ScheduledTaskInfo | Select-Object LastRunTime, LastTaskResult, NextRunTime
```
LastTaskResultが0以外の場合は失敗として扱う。

## Step 2: バックアップ成果物の検証
バックアップ出力先ディレクトリ（タスク定義またはスクリプトから特定）の直近ファイルについて:
- 存在するか
- サイズが前回比で極端に小さくないか（0バイトや異常な縮小は失敗扱い）
- 更新日時が直近7日以内か

## Step 3: Discord報告
正常時:
```
✅ backup-verify-weekly [YYYY-MM-DD]
LastRunTime: [日時] / LastTaskResult: 0（成功）
成果物: [ファイル名] [サイズ] [更新日時] — 正常
```
異常時:
```
⚠️ バックアップ異常検知 — backup-verify-weekly [YYYY-MM-DD]
LastRunTime: [日時] / LastTaskResult: [コード]（失敗）
原因調査: [Get-ScheduledTaskInfoの内容 / 成果物の状態]
対応要否: 手動確認を推奨
```
失敗時は理由を明記してDiscordに報告し終了（空レスポンス禁止）。