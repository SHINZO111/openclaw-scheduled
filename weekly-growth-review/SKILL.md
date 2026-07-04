---
name: weekly-growth-review
description: 毎週月曜05:00 JST。x-performance-log.mdの直近1週間から勝ちパターン・負けパターンを抽出しgrowth-insights.mdに記録、改善提案をDiscord報告する
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: cron.run / cron.list 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

## Step 1: データ読込
Read: C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md
直近7日分のpost/replyレコードを抽出する。データが無い/空スタブのままの場合は「⚠️ データ不足 — x-analytics-review未稼働の可能性」をDiscordに報告して終了する。

## Step 2: 勝ちパターン・負けパターン抽出
- imp上位10件・下位10件をテーマ／形式（本文構成・投稿時間帯・締めフレーズ）で分類
- 共通する要素（キーワード・時間帯・文字数帯）を勝ちパターンとして言語化
- 下位10件についても共通する弱点を言語化

## Step 3: growth-insights.mdへ追記
C:\Users\sawas\.openclaw\workspace\memory\growth-insights.md に追記:
```markdown
## WeeklyGrowthReview_YYYYMMDD
- 集計期間: YYYY-MM-DD 〜 YYYY-MM-DD
- 勝ちパターン: [テーマ/時間帯/構成の共通点]
- 負けパターン: [共通する弱点]
- 改善提案: 1) ... 2) ... 3) ...
```

## Step 4: Discord報告
「📈 週次成長レビュー — 勝ちパターン要約 / 改善提案3つ」を1メッセージで報告。
失敗時は理由を明記してDiscordに報告し終了（空レスポンス禁止）。