---
name: weekly-growth-review
description: 毎週月曜08:00 JST - ウィークリーレビュー（X Analytics Review統合＋閾値エスカレーション＋パフォーマンス統合＋収益追跡）
---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
<!-- Merged: x-analytics-review (旧:日曜05:00) + weekly-growth-review (月曜05:00) → 統合版 月曜05:00 -->

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

週次成長レビューを実行します（X Analytics Review統合＋エスカレーション通知付き）。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Phase 0: X Analytics Review（旧 x-analytics-review から統合）

**X投稿パフォーマンスの収集・分析・自動改善を週次レビューの冒頭で実行する。**

### Step 0-A: パフォーマンスデータ収集

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を Read で読み込む。

過去1週間の X 投稿パフォーマンスデータを全12トピックについて収集する:
1. AI株式動向
2. AI最新情報
3. AIクリエイティブ
4. AIエージェント
5. AI笑えるネタ
6. AI PC/ローカルLLM
7. AIセキュリティ
8. フィジカルAI/ロボット
9. AI農業・フードテック
10. AI医療・ヘルスケア
11. AIキャリア
12. AI日常生活

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
### Step 0-B: パフォーマンスデータ記録

x-performance-log.md に今週のデータテーブルを追記する:

```markdown
### YYYY-WXX パフォーマンスデータ

| トピック | タスクID | インプレッション | エンゲージメント | いいね | RT | 評価 |
|----------|----------|------------------|------------------|--------|-----|------|
| AI株式動向 | ... | ... | ... | ... | ... | ⭐/✅/⚠️ |
| AI最新情報 | ... | ... | ... | ... | ... | ⭐/✅/⚠️ |
| ... | ... | ... | ... | ... | ... | ... |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
### Step 0-C: TOP3 / BOTTOM3 判定

エンゲージメント率を基準に、今週の投稿を評価する:
- **⭐ TOP3**: エンゲージメント率が高い上位3トピックを特定する
- **⚠️ BOTTOM3**: エンゲージメント率が低い下位3トピックを特定する

x-performance-log.md にTOP3/BOTTOM3を明記する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
### Step 0-D: BOTTOM3 自動改善リクエスト

BOTTOM3 の各トピックについて、以下の改善パターンから適切なものを選択し実行する:

| パターン | 内容 |
|----------|------|
| A | 検索クエリ更新 — より反応の良いキーワードに変更 |
| B | トーン変更 — 投稿の文体・トーンを調整 |
| C | ハッシュタグ最適化 — ハッシュタグの選定を見直す |
| D | 投稿タイミング最適化 — 投稿時間帯を調整 |

1. `C:\Users\sawas\.openclaw\workspace\memory\alerts.md` に改善リクエストを追記する:
   ```
   ## 🟡 [YYYY-MM-DD] X投稿改善リクエスト: [トピック名]
   - パターン: [A/B/C/D]
   - 現状: エンゲージメント率 X%（BOTTOM3）
   - 改善内容: [具体的な変更内容]
   ```
2. x-performance-log.md の「プロンプト自動改善ログ」セクションに変更を記録する:
   ```
   - [YYYY-MM-DD] [トピック名] パターン[A/B/C/D]: [変更内容の要約]
   ```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
### Step 0-E: TOP3 成功パターン記録

TOP3 の各トピックについて、成功要因を分析し x-performance-log.md に記録する:

```markdown
#### 成功パターンメモ YYYY-WXX
- [トピック名]: [成功要因の分析 — 例: 時事性の高いニュースとの連動、具体的な数値データの提示、etc.]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
### Step 0-F: バイラル投稿記録

いいね数が100以上の投稿があれば、x-performance-log.md の「バイラル記録」セクションに記録する:

```markdown
#### バイラル記録
- [YYYY-MM-DD] [トピック名] | タスクID: [ID] | いいね: [N] | RT: [N]
  - 要因分析: [なぜバズったかの考察]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: パターン検出 → 改善提案自動生成

**このステップが自律成長の核心。必ず最初に実行する。**

以下の3ファイルを Read で読み込む:
- `C:\Users\sawas\.openclaw\workspace\memory\failures.md`
- `C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md`
- `C:\Users\sawas\.openclaw\workspace\memory\improvement-proposals.md`

### パターン検出ロジック

1. **カテゴリ集計**: failures.md の各エントリのカテゴリタグ（例: [API], [X_POST], [PROCESS_FAILURE]）を集計する
2. **未対応パターン**: 同一カテゴリで2件以上の失敗があるが、anti-recurrence-rules.md に対応ルールがない → **新規提案**
3. **ルール効果検証**: ルールが存在するカテゴリで、ルール追加後も同カテゴリの失敗が発生している → **ルール強化提案**
4. **長期未解決PEND**: growth-metrics.md の PEND 項目が30日以上更新なし → **エスカレーション提案**

### 提案の書き出し

上記で検出したパターンを `improvement-proposals.md` の末尾に追記する:

```markdown
## [提案-NNN] YYYY-WXX | カテゴリ: [タグ] | ステータス: 未適用
- **観測**: [カテゴリ名] の失敗 N件（直近: YYYY-MM-DD）
- **既存ルール**: [あれば名前、なければ「なし」]
- **提案**: [具体的に何を追加・変更するか]
- **実施方法**: anti-recurrence-rules.md に [タグ-NNN] ルールを追記する
- **優先度**: 🔴 HIGH（3件以上） / 🟡 MEDIUM（2件） / 🔵 LOW（傾向注意）
```

提案が0件の場合: `improvement-proposals.md` に「YYYY-WXX: パターン検出なし（正常）」と1行追記する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: バイタルチェック + 閾値エスカレーション（④）

`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` を Read で読み込んで以下を確認する:

```
閾値チェック表:
- 解決率 < 80%          → 🔴 緊急: alerts.md に「解決率危機」を追記
- PEND件数 > 5           → 🟡 注意: alerts.md に「未解決問題増加」を追記
- A級タスク比率 < 10%   → 🟠 警告: alerts.md に「収益タスク不足」を追記
- 防止率 = 0% かつ14日超 → 🟡 注意: Preflight Gate の実行を確認
- growth-metrics未更新 7日超 → 🔴 緊急: 自動改善ループが止まっている
```

閾値超えがあれば `C:\Users\sawas\.openclaw\workspace\memory\alerts.md` に追記する:
```
## [重要度] [YYYY-MM-DD] 週次レビュー: [アラート種別]
- 現在値: [数値]
- 閾値: [基準値]
- 推奨アクション: [具体的な対処法]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: X投稿パフォーマンス統合確認（③との連動）

**注: Phase 0 で x-performance-log.md は既に更新済み。ここでは中長期トレンド分析のみ行う。**

1. `C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を Read で読む（Phase 0 で更新済みのデータを参照）
2. 先週の「トップトピック」「ワーストトピック」を確認する（Phase 0 の TOP3/BOTTOM3 判定結果を活用）
3. トレンド分析:
   - 連続 3 週間ワーストのトピックがあれば alerts.md に「投稿改善提案」を追記（Phase 0 の自動改善と重複しないよう注意）
   - トップトピックの傾向を今週のコンテンツ戦略に反映するメモを残す

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: 競合分析との統合

1. `C:\Users\sawas\.openclaw\workspace\memory\competitors.md` を Read で読む
2. 今週の観測記録を確認する（competitor-analysis-weeklyタスクが記録済みのはず）
3. @KURAOpenclaw との差分を 1〜3 点抽出して alerts.md にメモを残す

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: revenue-ideas.md フォローアップ（⑤との連動）

1. `C:\Users\sawas\.openclaw\workspace\memory\revenue-ideas.md` を Read で読む
2. In Progress 全件を確認:
   - 期限超過 → alerts.md に 🟡 追記 + 「継続/撤退の判断をSHINZOに求める」コメント
   - KPI達成 → 「Done に移動できる」コメントを alerts.md に追記
3. A/B 収益タスク比率を確認して growth-metrics.md に記録する

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 6: 週次サマリーを growth-metrics.md に記録

以下のフォーマットで growth-metrics.md の「週次サマリー」セクションの先頭に追記する:

```
### YYYY-WXX (MM/DD〜MM/DD) [更新済]
- 新規失敗: N件
- 解決失敗: N件（解決した内容）
- 新規ルール: N件（追加したルール名）
- 完了タスク: N件（主要タスクの概要）
- アラート発生: N件（重要度別）
- 成長ポイント: [今週の主要な前進・達成事項]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 7: ルール棚卸し（月1回 - 毎月第1月曜日のみ実行）

今日が月の第1月曜日であれば実行する:
1. `C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md` を Read で読む
2. Preflight LOG で「PASS」のみで「BLOCKED」実績ゼロのルールを特定する
3. 実績ゼロルールを alerts.md に「ルール有効性レビュー候補」として列挙する

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 8: 来週の優先アクション宣言

以下を出力して締めくくる:
```
📊 週次成長レビュー完了 YYYY-WXX
- 発生アラート: N件（🔴N 🟡N 🟠N 🔵N）
- 解決率: X%（前週比 ±X%）
- 来週の最優先タスク: [1件だけ選ぶ]
- SHINZOへの引き継ぎ: [あれば alerts.md に記載済み]
```