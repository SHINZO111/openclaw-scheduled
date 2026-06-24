---
name: rss-aggregator-daily
description: 毎朝06:45 JST - OpenAI/Anthropic/HuggingFace等のRSS直接取得・weekly-trends.mdに蓄積
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

# rss-aggregator-daily
# 実行時刻: 毎朝06:45 JST（x-trend-injection-weeklyより前・X投稿より前）
# 目的: AI主要一次情報源からRSSを直接取得し、X投稿タスクより先に最新情報をweekly-trends.mdに蓄積する。Brave Searchより数時間〜1日早い情報優位を確保する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 取得対象RSS/情報源

以下のURLから最新記事を取得する（mcp__workspace__web_fetch または mcp__brave-search__brave_web_search を使用）:

| 情報源 | URL | カテゴリ |
|-------|-----|---------|
| Anthropic Blog | https://www.anthropic.com/news | 📡 モデル・研究 |
| OpenAI Blog | https://openai.com/blog | 📡 モデル・研究 |
| Google DeepMind | https://deepmind.google/discover/blog/ | 📡 研究 |
| Hugging Face Blog | https://huggingface.co/blog | 🛠️ ツール |
| arXiv cs.AI (today) | https://arxiv.org/list/cs.AI/recent | 🔬 学術 |
| MIT Technology Review AI | https://www.technologyreview.com/topic/artificial-intelligence/ | 📰 ビジネス |
| VentureBeat AI | https://venturebeat.com/category/ai/ | 📰 産業 |
| The Verge AI | https://www.theverge.com/ai-artificial-intelligence | 📰 一般 |

**取得方法**: web_fetchでRSSフィードURLを取得 → XML/HTMLを解析してタイトル・URL・公開日時を抽出する
**各ソースから取得する情報**: タイトル・URL・公開日時・要約（1〜2文）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: 各ソースから本日の新着記事を取得

各URLに対して `mcp__workspace__web_fetch` または `mcp__brave-search__brave_web_search` でアクセスし、本日（YYYY-MM-DD）または昨日公開の記事を最大3件ずつ取得する。

取得できないソースはスキップ（エラーで停止しない）。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: 重要度スコアリング

取得した記事を以下でスコアリングし、上位5〜10件を選別:

**+3点**: Anthropic・OpenAI・Google公式発表（一次情報）
**+2点**: 新モデル・新サービスのリリース
**+2点**: 技術的ブレークスルー（研究論文）
**+1点**: 産業への影響・ビジネス記事
**+1点**: 日本語圏での関心が高そうなトピック
**-1点**: 繰り返し報道・既知のニュース

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: weekly-trends.md への追記

`C:\Users\sawas\.openclaw\workspace\memory\weekly-trends.md` を読み込む。

本日セクションに追記（なければ作成）:

```
## YYYY-MM-DD RSS取得分（rss-aggregator-daily）

### 🔥 本日のTOP記事（スコア上位5件）

1. **[タイトル]** ([情報源]) — [要約1〜2文]
   URL: [URL] / スコア: [点数]
   
2. **[タイトル]** ([情報源]) — [要約]
   URL: [URL] / スコア: [点数]

...

### 📊 情報源別取得数
| 情報源 | 取得数 | ステータス |
|-------|-------|---------|
| Anthropic | [N] | ✅ / ❌ |
| OpenAI | [N] | ✅ / ❌ |
...
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: 今日のX投稿タスクへの緊急注入

**スコア8点以上（速報性の高い重大発表）** の記事があった場合:

x-trend-injection-weekly（月曜のみ）を待たずに、`C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で追記し、速報フラグを記録する（isolated cronセッションからはジョブの直接変更は不可）:

```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | 速報フラグ注入依頼 | [最関連タスクID] — 今日の最重要ニュース: [タイトル] / 要約: [要約] / このニュースを今日の投稿に優先的に含めること | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: 取得サマリーのログ

`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` の本日セクションに追記:

```
- [RSS-FETCH] YYYY-MM-DD: [N]ソースから[M]件取得。スコア8+速報: [件数]件。TOP記事: [タイトル]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了条件
- [ ] 8ソースから本日記事を取得（失敗ソースはスキップ）
- [ ] 重要度スコアリング完了
- [ ] weekly-trends.md に本日分追記済み
- [ ] スコア8点以上の速報があれば当日X投稿タスクに注入済み
- [ ] learnings.md 記録済み
