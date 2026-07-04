---
name: kura-backup
description: 毎日00:00 JST - ワークスペース自動バックアップ（Google Driveへ）
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取り・編集は不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## 実行手順

```
powershell -ExecutionPolicy Bypass -File "C:\Users\sawas\.openclaw\workspace\scripts\backup_script.ps1"
```

出力に「SUCCESS: Backup completed.」が含まれていれば成功（旧文言「✅ バックアップ処理が完了しました」は実際のスクリプト出力と不一致だったため修正）。エラー時はメッセージをそのまま報告（スクリプトの修正は不要）。

## 成功時のみ: ログ記録

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\kura-backup.md` に追記:
```
## [今日の日付] バックアップ記録
- status: success / timestamp: [実行時刻]
```