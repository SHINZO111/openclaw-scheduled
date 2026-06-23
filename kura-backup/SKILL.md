---
name: kura-backup
description: 毎日00:00 JST - ワークスペース自動バックアップ（Google Driveへ）
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、ファイルの編集も不要です。直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# Kura_Backup — ワークスペース自動バックアップ

## 実行手順（これだけ実行すればOK）

シェルツールで以下のコマンドを**そのまま実行**してください。スクリプトの編集は不要です。

```
powershell -ExecutionPolicy Bypass -File "C:\Users\sawas\.openclaw\workspace\scripts\backup_script.ps1"
```

## 実行後の確認

コマンドの出力に「✅ バックアップ処理が完了しました」が含まれていれば成功です。

エラーが出た場合は、エラーメッセージをそのまま報告してください。スクリプトの修正は行わないでください。

## 実行ログ記録（成功時のみ）

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\kura-backup.md` に以下を追記:
```
## [今日の日付] バックアップ記録
- status: success
- timestamp: [実行時刻]
```
