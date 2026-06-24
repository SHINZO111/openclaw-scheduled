---
name: x-analytics-review
model: lmstudio/nvidia/nemotron-3-nano-4b
description: 毎週日曜12:00 JST - Xアナリティクス確認・x-performance-log更新・BOTTOM3プロンプト自動改善
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

# x-analytics-review v2.0
# 実行時刻: 毎週日曜12:00 JST
# 目的: @KURAOpenclaw のX投稿パフォーマンスを分析し、最悪パフォーマンスのタスクプロンプトを自動改善する

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: パフォーマンスデータ収集

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を読み込む。

直近1週間（前回レビュー以降）の投稿データを確認する。

手動確認が必要な場合: X (twitter.com/KURAOpenclaw) のアナリティクス画面から
- インプレッション数
- エンゲージメント数（いいね・RT・返信）
- フォロワー増減

を確認し、以下のトピック別に記録する:
- AI株式動向 (x-post-ai-stock)
- AI最新情報 (x-post-ai-latest)
- AIクリエイティブ (x-post-ai-creative)
- AIエージェント (x-post-ai-agent)
- AI笑えるネタ (x-post-ai-funny)
- AI PC/ローカルLLM (x-post-aipc-latest)
- AIセキュリティ (x-post-ai-security)
- フィジカルAI/ロボット (x-post-physical-ai-latest)
- AI農業・フードテック (x-post-ai-agrifood)
- AI医療・ヘルスケア (x-post-ai-health)
- AIキャリア・スキルアップ (x-post-ai-career)
- AI日常生活 (x-post-ai-lifestyle)

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: x-performance-log.md 更新

`x-performance-log.md` に今週分のデータを追記する:

```
## YYYY-WXX（YYYY-MM-DD 週）

| トピック | タスクID | インプレッション | エンゲージメント | いいね | RT | 評価 |
|---------|---------|---------------|---------------|------|-----|------|
| AI株式動向 | x-post-ai-stock | - | - | - | - | 🔲 |
...
```

データが取得できないトピックは「-」で埋める。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: TOP3 / BOTTOM3 特定

今週のエンゲージメント数（取得できている場合）またはパターン認識（投稿内容の反応傾向）から:

**TOP3トピック**: 最も反応が良かった3件
→ x-performance-log.md に `⭐ TOP` マーキング

**BOTTOM3トピック**: 最も反応が低かった（または0の）3件
→ x-performance-log.md に `⚠️ BOTTOM` マーキング

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: BOTTOM3 タスクのプロンプト自動改善（NEW in v2.0）

BOTTOM3に特定されたトピックのタスクIDについて、以下を実行する。

### 4-1: 改善方針の決定

BOTTOM3の各タスクについて、以下の改善パターンから適切なものを選択する:

**改善パターンA: 検索クエリの更新**
- 現在の検索キーワードを時事性の高いものに変更
- より具体的なニッチキーワードを追加
- 英語ワード + 日本語ワードを組み合わせる

**改善パターンB: トーン・スタイルの変更**
- 現在「解説調」→「問いかけ調」（"〜って知ってた？"スタイル）
- 現在「ニュース報告」→「驚き表現」（"衝撃！"スタイル）
- 現在「長文」→「箇条書き+絵文字」スタイル

**改善パターンC: ハッシュタグ最適化**
- トレンドハッシュタグを `weekly-trends.md` から取得して追加
- 投稿カテゴリに合った特化ハッシュタグを選定

**改善パターンD: 投稿タイミング最適化**
- TOP3トピックの投稿時刻を確認し、エンゲージメントが高い時間帯（朝7〜9時・昼12〜13時・夜20〜22時 JST）に合わせる
- BOTTOM3の投稿時刻が他スキルと重複している場合（20分未満）は分散させる
- 投稿タイミング変更が必要な場合は `C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で追記する（isolated cronセッションからはジョブの直接変更は不可）:
  ```
  | YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | 投稿タイミング変更依頼 | [タスクID] — cronExpressionを[新しい値]に変更推奨（例: 朝9時5分→"5 9 * * *"、夜21時→"0 21 * * *"） | 未解決 |
  ```
- 変更後は `C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を直接Readして確認する
- 任意の2スキル間の間隔は最低20分を維持すること

### 4-2: 改善プロンプトの適用

BOTTOM3の各タスクIDについて、`C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で改善依頼を追記する（isolated cronセッションからはジョブの直接変更は不可）:

改善例（x-post-ai-agrifood が BOTTOM3 の場合）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | BOTTOM3プロンプト改善依頼 | x-post-ai-agrifood — 検索クエリ: 「AI農業 2025」→「AgriTech AI 最新 OR AI農業DX OR スマート農業」/ トーン: 解説調→驚き表現 / ハッシュタグ: #AI農業 #AgriTech #スマート農業 を追加 | 未解決 |
```

**重要**: 既存プロンプトの投稿ロジック（post-to-x.js の呼び出し、Cookie パス等）は変更しない。変更するのは「検索クエリ」「トーン指示」「ハッシュタグ」「投稿時刻」のみ。

### 4-3: 改善記録

改善を実施したタスクについて `x-performance-log.md` の当該週セクションに追記:
```
### プロンプト自動改善ログ（YYYY-MM-DD実施）
| タスクID | 改善パターン | 改善内容の要約 |
|---------|------------|--------------|
| x-post-ai-agrifood | B + C | トーンを驚き表現に変更、#AgriTechを追加 |
| x-post-ai-health | D | 投稿時刻を08:30→21:00 JSTに変更（夜帯エンゲージメント改善） |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: TOP3 の戦略メモ更新

TOP3のトピックについて:
- 成功要因を分析（時事性？感情喚起？具体的数字？）
- 同じ手法を他のトピックにも適用できるか検討
- `x-performance-log.md` に戦略メモを追記:
  ```
  ### 成功パターンメモ（YYYY-MM-DD）
  - TOP1 ([トピック]): [成功要因の分析]
  - 他トピックへの応用: [提案]
  ```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 6: ウイルス投稿の記録

過去7日間でいいね100件以上の投稿があった場合:
`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` の `## バイラル記録` セクションに追記:
```
| YYYY-MM-DD | [タスクID] | [投稿内容の要約] | [いいね数] | [成功要因] |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 7: 週次戦略メモ出力

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` の末尾に以下を追記:
```
## 週次戦略メモ YYYY-WXX
- 今週のフォーカス: [TOP3トピックの強化]
- 改善実施: [BOTTOM3のプロンプト更新完了]
- 来週の仮説: [次に試したい改善案]
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
- [ ] x-performance-log.md 今週分追記済み
- [ ] TOP3 / BOTTOM3 特定済み
- [ ] BOTTOM3 タスクのプロンプト自動改善実施済み（またはデータ不足のため保留）
- [ ] 成功パターンメモ記録済み
- [ ] 週次戦略メモ追記済み

