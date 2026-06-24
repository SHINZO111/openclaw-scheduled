---
name: x-trend-injection-weekly
model: openrouter/google/gemini-2.5-flash
description: 毎週月曜07:00 JST - 週次AIトレンド取得・投稿戦略注入・週1本収益化CTA付与
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

# x-trend-injection-weekly
# 実行時刻: 毎週月曜07:00 JST
# 目的: 今週のAIトレンドをX投稿タスク全体に注入する。加えて、週1本だけ収益化CTAを特定の投稿に付与する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: 今週のAIトレンド収集

### 1-A: weekly-trends.md の確認
`C:\Users\sawas\.openclaw\workspace\memory\weekly-trends.md` を読み込む。
rss-aggregator-daily が直近7日間に蓄積したTOP記事を確認する（スコア上位5件）。

### 1-B: Brave Searchで補完
`mcp__brave-search__brave_web_search` で以下を検索:
- 「AI 最新ニュース 今週」
- 「artificial intelligence news this week」

1-Aと1-Bを合わせて今週の注目トレンドTOP5を確定する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: トレンドをweekly-trends.mdに記録

今週セクション（`## YYYY-WXX（YYYY-MM-DD 週）`）を作成・追記:

```
### 今週の注目トレンドTOP5
1. [トピック1] — [要約1文] （ソース: [情報源]）
2. [トピック2] — ...
3. [トピック3] — ...
4. [トピック4] — ...
5. [トピック5] — ...

### 速報（スコア8点以上）
[あれば記録。rss-aggregatorが既に注入済みの場合は参照のみ]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: 今週の投稿方針を全X投稿タスクに注入

今週のトレンドTOP3を基に、関連する X投稿タスク（最大5件）について `C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で注入依頼を追記する（isolated cronセッションからはジョブの直接変更は不可）:

注入依頼内容（各タスクについて1行ずつalerts.mdに追記）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | トレンド注入依頼 | [タスクID] — 今週のトレンド指示を更新: トレンド1=[トレンド名](積極的に言及) / トレンド2=[トレンド名](関連づけて投稿) / トレンド3=[トレンド名](必要に応じて言及) | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: 週1本の収益化CTA付与（NEW）

**ルール**: 毎週月曜の投稿1本のみ、末尾に収益化CTAを追加する。
過剰なCTAはフォロワーを離脱させるため、週1本厳守。

### 4-A: CTA付与対象タスクの選定

今週のトレンドTOP1に最も近いカテゴリのX投稿タスクを1件選ぶ。

例: 今週トレンドが「AIエージェント」なら `x-post-ai-agent` を選択。

### 4-B: CTA文の生成

CTA種別を週ごとにローテーション（毎週変えてマンネリ防止）:

今週が何週目かを確認し（weekly-trends.mdの週番号から判断）:
- **奇数週**: Note.com記事誘導CTA
  ```
  📖 もっと詳しく知りたい方はNoteの解説記事へ → note.com/[KURAアカウント]
  ```
- **偶数週**: フォロー促進CTA
  ```
  🔔 毎日AIの最新情報をお届け中。フォローして情報収集を自動化しよう！
  ```
- **月初週（1日〜7日）**: 特別CTA（SHINZOが revenue-ideas.md で設定したIn Progress案件）
  ```
  [revenue-ideas.mdのIn Progressアイテムに応じたCTA文を生成]
  ```

### 4-C: CTA注入

選定した1タスクについて `C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で追記する（isolated cronセッションからはジョブの直接変更は不可）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | 収益化CTA付与依頼 | [タスクID] — 今週の収益化CTA: [CTA文] / 今週はこのタスクのみCTAを付与 | 未解決 |
```

### 4-D: CTA実施ログ

`C:\Users\sawas\.openclaw\workspace\memory\revenue-ideas.md` のIn Progressセクションに追記:
```
- YYYY-MM-DD: CTA付与実施（タスク: [タスクID] / 種別: [CTA種別]）
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: 速報投稿のトリガー確認

今週のトレンドにスコア9点以上の重大発表がある場合:
- 通常の投稿スケジュールを待たず、`C:\Users\sawas\.openclaw\workspace\alerts.md` に速報実行依頼を追記する（isolated cronセッションからはジョブの直接変更は不可）:
  ```
  | YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | 速報投稿実行依頼 | x-post-ai-latest — スコア9点以上の重大発表あり。当日中にワンショット実行推奨 | 未解決 |
  ```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 6: 完了記録

learnings.md に追記:
```
- [TREND-INJECT] YYYY-WXX: トレンドTOP5注入完了 / CTA付与: [タスクID]([CTA種別])
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
- [ ] 今週のトレンドTOP5確定済み
- [ ] weekly-trends.md 今週セクション記録済み
- [ ] X投稿タスク（最大5件）にトレンド注入済み
- [ ] 週1本CTA付与済み（対象タスク: [ID]）
- [ ] CTA実施ログ記録済み
- [ ] 速報トリガー確認済み（対象なしの場合はスキップ）
