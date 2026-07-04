---
name: monthly-performance-report
description: 毎月1日05:00 JST。月間imp合計・フォロワー増減・リプライ実績（monitor.db集計）・KPI表との差分をDiscordに1レポート報告する
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: cron.run / cron.list 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

## Step 1: 投稿imp集計
Read: C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md
直近30日分のpostレコードから月間imp合計・投稿imp平均を算出する。

## Step 2: リプライ実績集計
PowerShellツールで実行:
```
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 30
```
検知件数・送信件数・失敗件数を取得する。

## Step 3: KPIマイルストーンとの差分
監査・改善計画（audit-improvement-plan-20260702.md §4 KPIマイルストーン）の該当週目標値と実績を比較し、達成率（%）を算出する。
70%未満の指標があれば赤字で明記する。

## Step 4: Discord報告
```
📊 月次パフォーマンスレポート — monthly-performance-report [YYYY-MM]
【投稿】月間imp合計: N / 投稿imp平均: N
【リプライ】検知: N件 / 送信: N件 / 失敗: N件
【KPI進捗】目標比 N%（達成 / 未達）
【所感】[上振れ・下振れの要因を1-2行]
```
失敗時は理由を明記してDiscordに報告し終了（空レスポンス禁止）。