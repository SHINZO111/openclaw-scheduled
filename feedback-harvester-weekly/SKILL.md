---
name: feedback-harvester-weekly
description: 毎週月曜06:00 JST - SHINZOの承認/却下コメントを学習・判断パターンをMemory MCPに転写
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# feedback-harvester-weekly
# 実行時刻: 毎週月曜06:00 JST
# 目的: soul-evolution-proposals.mdへのSHINZOの承認・却下・修正コメントを収集し、判断パターンをMemory MCPに学習させる。次回の提案精度を向上させる。

---

## Step 1: soul-evolution-proposals.md の差分確認

`C:\Users\sawas\.openclaw\workspace\memory\soul-evolution-proposals.md` を読み込む。

前週（7日以内）に新たに「✅ 承認」「❌ 却下」「🔄 修正」マークが付いた提案を検出する。

新規フィードバックがない場合: このステップをスキップして Step 4 へ。

---

## Step 2: フィードバックの分類・意図推定

各フィードバックについて判断意図を推定する:

### ✅ 承認された提案の共通特徴
- 提案の具体性レベル（抽象的 / 具体的）
- 影響範囲（小 / 中 / 大）
- 即効性（短期 / 長期）
- 技術的複雑さ（低 / 中 / 高）
- SHINZOが書き込んだコメント（あれば）

### ❌ 却下された提案の共通特徴
- 上記と同様の分析
- 却下理由の推定（複雑すぎる / 方向性が違う / タイミングが悪い 等）

### 🔄 修正要求の内容
- 何が問題で修正が求められたか
- 修正の方向性

---

## Step 3: cronログファイルへの判断パターン記録

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\feedback-harvester-weekly.md` に以下を追記:
```
## YYYY-MM-DD 判断パターン記録

### 承認パターン
- YYYY-MM-DD: 承認 — [提案概要] / 特徴: [具体性/影響範囲/即効性]

### 却下パターン
- YYYY-MM-DD: 却下 — [提案概要] / 推定理由: [理由]

### 関係性（パターンが3件以上蓄積の場合）
- SHINZOPreferences_Approved → ProposalPattern_Concrete_SmallScope: TENDS_TO_APPROVE
```

---

## Step 4: learnings.md への転写

`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` 本日セクションに追記:

```
## YYYY-MM-DD (feedback-harvester-weekly)

### SHINZOフィードバック学習
- 承認パターン: [今週学習した承認されやすい提案の特徴]
- 却下パターン: [今週学習した却下されやすい提案の特徴]
- 次回提案への反映: [具体的な改善方向]
```

新規フィードバックがない週:
```
- [FEEDBACK-HARVEST] 今週のフィードバックなし — soul-evolution-proposals.mdに未回答の提案が[N]件あり
```

---

## Step 5: 未回答提案のリマインダー

soul-evolution-proposals.mdに「未回答」（✅❌🔄のいずれもない）提案が2週間以上ある場合:

alerts.md に追記:
```
| YYYY-MM-DD 06:00 | 🟡 MEDIUM | 提案未回答 | [提案ID]が[N]日間未回答 — soul-evolution-proposals.md 確認をお願いします | 未解決 |
```

---

## Step 6: 累積パターンサマリー（月初のみ）

月の最初の月曜日の場合:

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\feedback-harvester-weekly.md` から承認・却下パターンの全記録を読み込み、傾向をまとめる:

```
## SHINZOの意思決定パターン（YYYY-MM累積）
- 承認率: [N/M]件 = [X]%
- 最も承認されやすい提案タイプ: [タイプ]
- 最も却下されやすい提案タイプ: [タイプ]
- 推定される優先価値観: [推定]
```

この結果を soul-evolver-monthly・quarterly-prompt-review のプロンプトに反映することで提案精度が上がる。

---

## 完了条件
- [ ] soul-evolution-proposals.md の差分確認済み
- [ ] フィードバックの分類・意図推定完了
- [ ] cronログファイルへの判断パターン記録済み
- [ ] learnings.md 転写済み
- [ ] 未回答提案リマインダー確認済み
- [ ] 月初の場合: 累積パターンサマリー生成済み
