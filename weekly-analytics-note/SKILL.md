---
name: weekly-analytics-note
model: openrouter/google/gemini-2.5-flash
description: 毎週月曜09:00 JST - noteアクセス解析を集計して週次レポートをworkspaceに保存
---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# weekly-analytics-note

## 概要
毎週月曜09:00 JST に実行。noteのアクセス解析データをまとめ、週次レポートをworkspaceに保存する。

## 実行内容
1. note.comのアクセス解析ページを確認（ブラウザ経由 or スクレイピング）
2. 以下の指標を取得・集計:
   - 記事別PV（週間）
   - フォロワー数推移
   - スキ数推移
   - 流入元上位3件
3. 前週比較を計算
4. レポートを `workspace\reports\note-analytics-weekly-YYYYMMDD.md` に保存
5. 特異値（急増・急減）があれば `workspace\alerts.md` に追記

## 出力フォーマット
```
# note週次レポート YYYY-MM-DD
## サマリー
- 総PV: X (+Y% 前週比)
- フォロワー: X (+Y)
- 総スキ: X (+Y)

## 記事別PV Top5
1. 記事タイトル: PV数
...

## 所見・次週アクション
- 
```

## 参照ファイル
- 出力先: `workspace\reports\note-analytics-weekly-YYYYMMDD.md`
- アラート: `workspace\alerts.md`
- cronログ: `workspace\memory\cron-logs\weekly-analytics-note.md`
