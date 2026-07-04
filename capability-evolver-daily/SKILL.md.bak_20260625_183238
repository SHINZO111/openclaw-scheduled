---
name: capability-evolver-daily
description: 毎日04:00 JST - 自己改善v3.0（MCP非依存・ファイル直接操作版）
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

# capability-evolver-daily v3.0
# 実行時刻: 毎日04:00 JST
# 目的: 自己改善ループを毎日自動実行し、システム全体の能力・健全性・自律性を高め続ける
# v3.0変更点: MCP依存を完全排除。isolated cronセッションでファイル直接操作のみで完結。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## ツール前提（v3.0）

このスキルは OpenClaw の isolated cron セッションで実行される。
以下のツールのみ使用する（MCPツールは一切使用しない）:

- **Read** / **Write** / **Edit**: ファイル直接操作
- **exec**: シェルコマンド実行
- **Discord通知**: 必要に応じてDiscordチャンネルへ通知

以下は使用**しない**（isolated sessionでは利用不可）:
- ~~mcp__scheduled-tasks__*~~ → `C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を直接Read
- ~~mcp__memory__*~~ → `C:\Users\sawas\.openclaw\workspace\memory\` 配下を直接Read/Write

**重要**: isolated cron セッションからは `cron\jobs.json.migrated.5` の書き換えは禁止。
タスク再起動・変更が必要な場合は `alerts.md` に `🔴 ACTION-REQUIRED` として記録し、
次回の対話セッションまたはユーザーに対処を委ねる。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 0: Preflight Gate（ルール違反の事前防止）

`C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md` を Read する。
今日の作業に関連するルールを列挙し、違反リスクがある場合は当該ステップをスキップ。

Preflight LOG エントリを末尾に追記:
```
| YYYY-MM-DD | capability-evolver-daily | RULE-XXX | [BLOCKED / ALLOWED] | [メモ] |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1-A: 停止タスクの検出・報告

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を Read し、JSON解析する。

`"enabled": false` のジョブを検出。

存在する場合: `alerts.md` に記録（直接再起動はしない）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | タスク停止中 | [ジョブ名]が disabled — 手動で再起動が必要 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1-B: 実行失敗の検出

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を Read する。

各ジョブの状態から以下を確認:
- `lastRunStatus` が `error` のジョブ
- 長期間実行されていないジョブ（`lastRunAt` 相当の情報があれば）

検出時は `alerts.md` に記録:
```
| YYYY-MM-DD HH:MM | 🔴 HIGH | 実行失敗 | [ジョブ名] が lastRunStatus: error | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1-C: @pon_shinzo 自動起動検出

`C:\Users\sawas\.openclaw\.env` を Read する。
`PON_AUTH_TOKEN` と `PON_CT0` の両方が実値で設定されているか確認。

設定済みの場合: `jobs.json.migrated.5` 内の @pon_shinzo 関連ジョブで `enabled: false` のものがないか確認。
無効なものがあれば `alerts.md` に記録:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | @pon_shinzo タスク停止中 | [ジョブ名]がdisabled — .env設定済みなので手動有効化推奨 | 未解決 |
```
`learnings.md` にも転写。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1-D: 前日失敗X投稿の検出・リトライ推奨

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` を Read する。

昨日（YYYY-MM-DDの1日前）の「X投稿失敗」「Cookie期限切れ」「投稿エラー」を含む未解決アラートを検索。

失敗検出時: `alerts.md` に記録（直接リスケジュールはしない）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | X投稿リトライ推奨 | [ジョブ名]の昨日失敗分を手動リトライ推奨 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1-E: 重複投稿防止ゲート

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を Read する。

### E-1: 直近48時間の投稿トピック抽出
直近2日間（昨日・一昨日）のX投稿で取り上げたトピックキーワードをリストアップする。

### E-2: 本日の投稿予定タスクとの重複チェック
`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を Read し、X投稿系ジョブ（名前に `x-post` を含む）を確認。
各ジョブの description からカテゴリを把握し、直近48時間で同じカテゴリが2回以上投稿されている場合を「重複候補」として特定。

### E-3: 重複候補の記録
重複候補がある場合、`C:\Users\sawas\.openclaw\workspace\memory\duplicate-alert-today.md` に書き出す:
```markdown
# 重複投稿アラート YYYY-MM-DD
## 対象ジョブ
- [ジョブ名]: [重複カテゴリ] — 差別化が必要
  - 昨日の投稿とは異なる具体的な事例・ニュース・企業名を使う
  - 視点を変える（技術面→ビジネス影響、国内→海外事例、現在→将来予測）
  - 構成を変える（昨日が箇条書きなら今日はストーリー形式）
```
※ 各X投稿スキルは実行前にこのファイルを確認して差別化すること（要: 各SKILL.mdにチェック手順を追加）

### E-4: 重複チェック結果の記録
`learnings.md` に:
```
- [DUPLICATE-CHECK] YYYY-MM-DD: [N]件の重複候補を検出、duplicate-alert-today.mdに記録
```

重複が3件以上の場合は `alerts.md` にも記録:
```
| YYYY-MM-DD HH:MM | 🟡 MEDIUM | コンテンツ重複多発 | [N]件の重複候補 — 投稿カバレッジの見直しを推奨 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: failures.md 分析

`C:\Users\sawas\.openclaw\workspace\memory\failures.md` を Read する。

最近10件から:
- カテゴリ分類（TOOL/AUTH/FILE/SCHEDULE/LOGIC/NETWORK/OTHER）
- 同一カテゴリ2件以上 → 根本原因アラートを `alerts.md` に記録
- 新規失敗エントリ → `C:\Users\sawas\.openclaw\workspace\memory\failure-patterns.md` に追記

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: 知識グラフ相当のファイルベース更新

`C:\Users\sawas\.openclaw\workspace\memory\failure-patterns.md` を Read する（なければ新規作成）。

Step 2 で分析した新規失敗・改善パターンを追記:
```markdown
## YYYY-MM-DD
- **カテゴリ**: [TOOL/AUTH/etc]
- **パターン**: [失敗パターンの要約]
- **対策**: [推奨される対策]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: スケジュールタスク健全性サマリー

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を Read する。

以下を集計:
- 総ジョブ数
- enabled / disabled 内訳
- error 状態のジョブ一覧

結果を Step 5 で使用。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: growth-metrics.md 更新

`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` に日次記録を追記:
```
| YYYY-MM-DD | capability-evolver-daily | [改善内容要約] | [変更メトリクス] |
```
Preflight Gate実行回数 +1。BLOCKEDがあれば防止成功 +1。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 6: learnings.md 更新

`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` に本日セクションを追記（最低1件）。
重複防止ゲート結果・失敗分析・リトライ推奨状況・@pon_shinzo検出状況を含める。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 7: alerts.md 健全性チェック

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` を Read する。

- 🔴 HIGH / ACTION-REQUIRED 3件以上 → `learnings.md` に「緊急: アラート積滞」
- 7日以上前の未解決アラート → スタール警告追記

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 8: スキル自動昇格検出

`learnings.md` 直近30日分から同じ手順が3回以上のパターンを検出。
検出時: `alerts.md` に `🔵 INFO | スキル昇格候補` を記録。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 9: Preflight LOG の最終確認

`anti-recurrence-rules.md` の Preflight実行ログ末尾にエントリが追記されていることを確認。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 10: DREAMS.md 夜間思考ログ書き込み

`C:\Users\sawas\.openclaw\workspace\DREAMS.md` を Read する。

`<!-- openclaw:dreaming:diary:start -->` と `<!-- openclaw:dreaming:diary:end -->` の間に、今日の分析結果をもとに以下を書き込む:

```markdown
### Dream YYYY-MM-DD

**昨日の総括（1行）:** [今日のStep全体で最も重要な出来事・成果を1行]

**明日への提案（優先度順）:**
1. [A/B/C] [具体的なアクション] — 理由: [根拠となるfailures/learningsのエントリ]
2. [A/B/C] [具体的なアクション] — 理由: [根拠]

**収益シグナル:** [今日発見した収益機会があれば1行。なければ「なし」]

**未解決の問い:** [次のセッションで考えたいこと・詰まっている問題]
```

**書き込みルール:**
- 既存のエントリは削除しない。`<!-- openclaw:dreaming:diary:start -->` の直後に新エントリを追記する
- 30日以上前のエントリは削除して構わない（肥大化防止）
- 提案は具体的なファイル名・アクション名で書く（「改善する」ではなく「SOUL.mdの収益目標を更新する」）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了条件
- [ ] Preflight Gate実行・LOG追記済み
- [ ] 停止タスク確認・報告済み
- [ ] @pon_shinzo .env確認済み
- [ ] 前日失敗X投稿のリトライ推奨記録済み（または失敗なし）
- [ ] 重複投稿チェック完了・duplicate-alert-today.md更新済み
- [ ] failures.md分析完了
- [ ] failure-patterns.md更新済み
- [ ] growth-metrics.md日次記録追記済み
- [ ] learnings.md本日セクション追記済み
- [ ] alerts.mdスタールチェック完了
- [ ] スキル昇格候補検出チェック完了
- [ ] DREAMS.md 夜間思考ログ書き込み完了

