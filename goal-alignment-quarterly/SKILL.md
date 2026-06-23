---
name: goal-alignment-quarterly
description: 3/6/9/12月1日08:00 JST - SOUL.mdゴールと稼働タスクの整合性チェック・ドリフト検出
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# goal-alignment-quarterly
# 実行時刻: 3月・6月・9月・12月の1日 08:00 JST
# 目的: SOUL.mdに記載された目標と実際に稼働しているタスク群を照合し、「やっていることとやりたいことのズレ」を検出する

---

## Step 1: SOUL.md / CLAUDE.md の目標確認

`C:\Users\sawas\.openclaw\workspace\SOUL.md` を読み込む（存在する場合）。
`C:\Users\sawas\.openclaw\workspace\memory\soul-evolution-proposals.md` を読み込む。

以下を抽出:
- **コアミッション**: システムが最終的に何を達成すべきか
- **優先目標**: 現四半期の重点目標
- **禁止事項**: やってはいけないこと

---

## Step 2: 全稼働タスクの目的マッピング

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を直接Readして全タスクを取得。

各タスクを以下のカテゴリにマッピング:
- 📣 **コンテンツ配信** (X投稿, Note投稿)
- 📊 **分析・改善** (analytics, benchmark, optimizer)
- 🛡️ **システム保守** (backup, health-check, cookie-check)
- 🧠 **自己改善** (capability-evolver, memory-synthesis, soul-evolver)
- 💰 **収益化** (revenue-ideas)
- 🔍 **情報収集** (competitor-analysis, trend-injection)
- ⚙️ **その他**

---

## Step 3: ゴール整合性の評価

各カテゴリについて、SOUL.mdの目標との整合性を評価:

| カテゴリ | タスク数 | 目標との整合性 | 問題点 |
|---------|---------|------------|------|
| 📣 コンテンツ配信 | 14 | ✅ 整合 | - |
| 💰 収益化 | 1 | ⚠️ 弱い | 収益タスクが少ない |
...

**ドリフト検出のパターン**:
- 「目標にないカテゴリのタスクが多すぎる」→ リソース分散の懸念
- 「目標カテゴリのタスクが0件」→ 目標放棄の懸念
- 「disabled タスクが重要カテゴリに多い」→ 実質的な目標放棄

---

## Step 4: KPI達成状況の確認

`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` を読み込む。

SOUL.mdの目標数値（フォロワー数、投稿数、収益等）と実績を比較:

| KPI | 目標値 | 実績値 | 達成率 | 評価 |
|----|-------|-------|-------|------|
| @KURAOpenclawフォロワー | [目標] | [実績] | [%] | ✅/⚠️/🔴 |
| 月間X投稿数 | [目標] | [実績] | [%] | ✅/⚠️/🔴 |
| 収益化ステージ | InProgress | [実績] | - | ✅/⚠️/🔴 |

---

## Step 5: 整合性レポートと提案生成

`C:\Users\sawas\.openclaw\workspace\memory\soul-evolution-proposals.md` に追記:

```
## 提案 YYYY-QX-ALIGN（goal-alignment-quarterly 自動生成）

### 四半期ゴール整合性レポート

**総合評価**: ✅ 整合 / ⚠️ 軽微なドリフト / 🔴 重大なドリフト

#### 検出されたドリフト
| # | 問題 | 現状 | 推奨アクション | 優先度 |
|---|-----|-----|-------------|-------|

#### 提案GA-01: [具体的な提案タイトル]
- 問題: [詳細]
- 推奨変更: [具体的なアクション]

承認フロー: 「✅ 承認」を書き込む
```

---

## Step 6: alerts.md への通知

```
| YYYY-MM-DD 08:00 | 🔵 INFO | 四半期ゴール整合性チェック完了 | ドリフト[N]件検出 — soul-evolution-proposals.md 参照 | 未解決 |
```

ドリフトが 🔴 重大の場合:
```
| YYYY-MM-DD 08:00 | 🔴 HIGH | ゴール整合性: 重大ドリフト | [問題の要約] — 即時見直し推奨 | 未解決 |
```

---

## 完了条件
- [ ] SOUL.md / CLAUDE.md 目標確認済み
- [ ] 全タスクのカテゴリマッピング完了
- [ ] ゴール整合性評価完了
- [ ] KPI達成状況確認済み
- [ ] soul-evolution-proposals.md に提案登録済み
- [ ] alerts.md 通知済み

