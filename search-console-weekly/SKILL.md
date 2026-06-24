---
name: search-console-weekly
description: 毎週月曜10:00 JST - Google Search Consoleの検索クエリ・流入データを取得してSEO戦略を更新
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

# Google Search Console 週次分析タスク — 毎週月曜10:00 JST

## 目的
Google Search ConsoleからSEOデータを取得し、ミテルン・note記事への検索流入を最大化する戦略を週次で更新する。

## Step 1: Google Search Consoleにアクセス

> ⚠️ **注**: `mcp__playwright__browser_navigate` は isolated cron セッションでは使用不可。代わりに `mcp__Claude_in_Chrome__navigate` を試みる。使用不可の場合は手動実行を要求する。

1. まず `mcp__Claude_in_Chrome__navigate` で `https://search.google.com/search-console/performance/search-analytics` にアクセスを試みる
2. Chrome MCPが使用不可の場合:
   ```
   ⚠️ Google Search Console週次分析 — ブラウザアクセスが必要です
   手動でアクセスしてください: https://search.google.com/search-console/performance/search-analytics
   ```
   alerts.mdに記録してタスク終了（空レスポンスは返さないこと）
3. ログイン状態確認 → 未ログインの場合: タスク中断・SHINZOへ通知

## Step 2: パフォーマンスデータを取得
GSCのパフォーマンスレポートから以下を抽出（過去28日間）:
- 検索クリック数 TOP20キーワード
- インプレッション数 TOP20キーワード
- 平均掲載順位 TOP20キーワード
- CTR（クリック率）が低いのに上位表示されているキーワード（タイトル改善候補）

プロパティごとに確認:
1. ミテルンのサイト（https://miterun.com）
2. note.com ページ（設定済みであれば）

## Step 3: データ分析
**注目指標:**
1. **クリック増加TOP5**: 先週比でクリック増加したキーワード
2. **機会キーワード**: 表示回数多いがCTR低い（メタタイトル改善で伸びる）
3. **1ページ目未満のキーワード**: 順位11〜20位（もう少しで1ページ目入り）
4. **新規流入キーワード**: 先週は0だったが今週流入があったキーワード

## Step 4: アクション提案レポート生成
`C:\Users\sawas\.openclaw\workspace\reports\seo-weekly-YYYYMMDD.md` に保存:
```markdown
# SEO週次レポート [YYYY-MM-DD]

## サマリー
- 総クリック数: [N]（前週比: +[N]%）
- 総インプレッション: [N]
- 平均順位: [N]位

## 今週のTOP検索クエリ
1. "[キーワード]" — [N]クリック / [N]順位
2. ...

## 🎯 即効アクション（今週対応推奨）
1. [キーワード]のメタタイトルを改善（現CTR [N]% → 目標[N]%）
   改善案: "[新タイトル案]"
2. ...

## 📝 コンテンツ提案
検索されているが対応記事がないキーワード:
- "[キーワード]" → note記事 or Qiita記事を作成

## 来週の目標
- クリック数: [N]（+[N]%）
- 優先キーワード: [リスト]
```

## Step 5: Memoryに更新
週次SEOデータをMemory MCPに保存（月次レポートで活用）。

## 注意
- GSCのデータ遅延は通常3〜4日（最新データは先週分まで）
- 各プロパティのアクセス権限が必要