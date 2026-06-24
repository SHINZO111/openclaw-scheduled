---
name: soul-evolver-monthly
description: 毎月1日06:00 JST - SOUL.md/OpenClaw設定自動進化提案生成＋前月改善ROI検証
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

SOUL.md と OpenClaw設定ファイル(CLAUDE.md) の自動進化提案を生成します。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 0: Preflight

`anti-recurrence-rules.md` を Read して [FILE] → RULE-032 確認済みと宣言してから進む。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: 先月の学習・失敗・ルールを横断読み込み

以下のファイルを Read で全て読む:
1. `C:\Users\sawas\.openclaw\workspace\memory\learnings.md`
2. `C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md`
3. `C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md`
4. `C:\Users\sawas\.openclaw\workspace\SOUL.md`

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1.5: 前月改善のROI検証（improvement-roi-monthly統合）

1. `soul-evolution-proposals.md` を Read して前月セクションの「✅ 承認」マーク付き変更を抽出（提案ID、変更内容、変更対象、実施日）
2. growth-metrics.md と x-performance-log.md から変更前後のメトリクスを比較:
   - ROI判定基準: ✅有効(+5%以上) / →通常(±5%以内) / ❌無効(-5%以下) / ⚠️データ不足(1ヶ月未満)
3. learnings.md に「improvement-roi検証」セクションを追記（有効/無効/データ不足の分類、パターン学習）
4. ❌無効の変更がある場合 → soul-evolution-proposals.md にロールバック提案を追記
5. growth-metrics.md に改善成功率を追記（有効N件/無効M件/成功率N/(N+M)%）。成功率50%未満ならalerts.mdに警告
6. Step 2のパターン分析はこのROI結果を考慮する（有効パターンを強化、無効パターンを回避）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: パターン分析

以下を抽出・分析する:

**A. 繰り返し学習パターン（3回以上言及されているテーマ）**
→ SOUL.md の姿勢10条に追加・強化すべき内容

**B. 解決できていない問題のパターン**
→ 行動規範に「○○の場合は△△する」ルールとして追記すべき内容

**C. 効果を上げている作業パターン**
→ OpenClaw設定ファイル(CLAUDE.md) の起動プロトコルに組み込んで毎セッション強制適用すべき内容

**D. SOUL.md の現行姿勢10条のうち「空洞化している」もの**
（記録上は実行できているが learnings.md や成長指標に反映されていないもの）
→ 削除・統合・強化の対象

**E. 前月ROI検証で「有効」と判定された改善パターンを優先的に提案する**

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: 進化提案を生成して soul-evolution-proposals.md に書き込む

`C:\Users\sawas\.openclaw\workspace\memory\soul-evolution-proposals.md` に追記:

```markdown
## 提案 YYYY-MM（soul-evolver-monthly 自動生成）

### SOUL.md への提案

#### 追加・強化
| 提案 | 根拠（learnings/rulesの何件） | 優先度 | SHINZO判定 |
|------|--------------------------|--------|-----------|
| [提案内容] | [N件の観察に基づく] | 高/中/低 | □承認 □却下 □修正 |

#### 削除・統合の候補
| 現行条文 | 削除理由 | SHINZO判定 |
|---------|---------|-----------|
| [現行の姿勢X条] | [空洞化の根拠] | □承認 □却下 |

### OpenClaw設定ファイル(CLAUDE.md) への提案（起動プロトコル改善）

| 提案 | 根拠 | SHINZO判定 |
|------|------|-----------|
| [毎セッション○○を確認するを追加] | [N回忘れた証拠] | □承認 □却下 |

### 前月の承認済み提案の反映状況
承認済み提案: [N件] → 反映済み: [N件] / 未反映: [N件]
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: 前月の承認済み提案を SOUL.md / OpenClaw設定ファイル(CLAUDE.md) に反映

soul-evolution-proposals.md の前回セクションで「✅ 承認」がついている提案を確認する。

承認済み提案がある場合:
1. SOUL.md を Read して対象箇所を Edit で更新
2. OpenClaw設定ファイル(CLAUDE.md)（グローバル）を Read して Edit で更新
3. soul-evolution-proposals.md の「反映済み変更ログ」テーブルに追記
4. SOUL.md の末尾の `_最終更新:` 日付を今日に更新

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: アラートを alerts.md に通知

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` に追記:
```
## 🔵 [YYYY-MM-DD] SOUL進化提案 YYYY-MM — SHINZOの確認が必要です
- 提案数: [N件]（SOUL.md追加 N件 / 削除候補 N件 / OpenClaw設定ファイル(CLAUDE.md) N件）
- 確認先: workspace/memory/soul-evolution-proposals.md
- 承認方法: 各提案の「SHINZO判定」欄に「✅ 承認」「❌ 却下」「🔄 修正:[内容]」を書いてください
- 次回反映: 来月1日の soul-evolver-monthly 実行時
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了宣言

「🧬 SOUL進化提案完了 YYYY-MM | 提案 N件 | 前月承認反映: N件 | alerts.md 通知済み」