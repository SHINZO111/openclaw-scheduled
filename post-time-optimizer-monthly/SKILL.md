---
name: post-time-optimizer-monthly
description: 毎月1日05:20 JST。x-performance-log.mdの時間帯別平均impを集計し、現行cron時刻との差分を提案する（自動変更はせずSHINZO承認制）
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: cron.run / cron.list 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

## Step 1: データ読込
Read: C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md
直近30日分のpostレコード（時刻・imp）を抽出する。データが不足している場合は「⚠️ データ不足 — 提案スキップ」をDiscordに報告して終了する。

## Step 2: 時間帯別平均imp集計
1時間単位で平均impを集計し、上位3時間帯・下位3時間帯を特定する。

## Step 3: 現行cron時刻との差分提案
C:\Users\sawas\.openclaw\cron\jobs.json.migrated を Read し、x-post-*系5ジョブの現行時刻と比較。
ズレが大きい（上位時間帯から2時間以上離れている）ジョブがあれば「変更提案」として列挙する。
**自動でjobs.json.migratedを書き換えない。提案のみ。**

## Step 4: Discord報告
```
🕐 投稿時間最適化提案 — post-time-optimizer-monthly [YYYY-MM]
【imp上位時間帯】[時間帯1] [時間帯2] [時間帯3]
【imp下位時間帯】[時間帯1] [時間帯2] [時間帯3]
【変更提案】
- x-post-xxx: 現行[HH:MM] → 提案[HH:MM]（根拠: ...）
⚠️ 実際の変更はSHINZOが承認後に実施してください。
```
失敗時は理由を明記してDiscordに報告し終了（空レスポンス禁止）。