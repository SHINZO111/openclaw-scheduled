---
name: post-time-optimizer-monthly
description: 毎月1日05:40 JST - 投稿時間帯別エンゲージメント分析・cron最適化提案
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# post-time-optimizer-monthly
# 実行時刻: 毎月25日 08:00 JST
# 目的: @KURAOpenclaw の投稿時間帯別エンゲージメントを分析し、より多くのフォロワーにリーチできるよう投稿時刻を自動提案・適用する

---

## Step 1: 現在の投稿スケジュール確認

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を直接Readして X投稿タスク（x-post-*）の現在のcron時刻を取得する:

| タスクID | 現在の投稿時刻（JST） |
|---------|------------------|
| x-post-ai-stock | 08:00 |
| x-post-ai-latest | 09:00 |
... （全12タスク）

---

## Step 2: 時間帯別パフォーマンスデータ収集

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を読み込む。

過去1ヶ月分のデータから時間帯別エンゲージメントを集計:

| 時間帯 | 平均エンゲージメント | 投稿タスク数 | 評価 |
|-------|-----------------|-----------|------|
| 07:00-09:00 | - | 2 | - |
| 09:00-11:00 | - | 2 | - |
| 11:00-13:00 | - | 2 | - |
| 13:00-15:00 | - | 2 | - |
| 15:00-17:00 | - | 2 | - |
| 17:00-19:00 | - | 2 | - |

データが不足している場合（x-performance-logが空の場合）:
`mcp__brave-search__brave_web_search` で「Twitter 日本 最適投稿時間 2025 エンゲージメント」を検索し、業界ベストプラクティスを参照する。

---

## Step 3: 最適時間帯の特定

以下の観点で最適時間帯を判定:
1. **自データ優先**: x-performance-logに3ヶ月以上のデータがあれば自データを使用
2. **業界標準**: データ不足の場合は日本のX最適投稿時間（一般的に07:00-09:00、12:00、21:00-23:00が高い）を参照
3. **競合回避**: competitor-analysis-weekly の結果と重複しない時間帯を選ぶ

---

## Step 4: 改善提案の生成

現在の時刻配置と最適時刻の差分を計算し、変更提案を生成:

```
## 投稿時刻最適化提案 YYYY-MM

| タスクID | 現在時刻 | 推奨時刻 | 改善見込み | 変更推奨度 |
|---------|--------|--------|---------|---------|
| x-post-ai-stock | 08:00 | 07:30 | +10% | 🟡 中 |
| x-post-ai-funny | 12:00 | 12:30 | +5% | 🔵 低 |
...
```

---

## Step 5: soul-evolution-proposals.md への提案登録

`C:\Users\sawas\.openclaw\workspace\memory\soul-evolution-proposals.md` に追記:

```
## 提案 YYYY-MM-TIME（post-time-optimizer-monthly 自動生成）

### 投稿時刻最適化提案

#### 提案PTO-01: [タスクID] 投稿時刻変更
- 現在: [時刻]
- 推奨: [時刻]  
- 根拠: [自データ or 業界標準]
- 改善見込み: [+N%]

承認フロー: 「✅ 承認」を書き込む → 次回実行時にcron自動更新
```

---

## Step 6: 承認済み提案の自動適用

soul-evolution-proposals.md で「✅ 承認」マークのある PTO-XX 提案を確認する。

承認済みがある場合、`C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で追記（isolated cronセッションからはジョブの直接変更は不可）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | cron時刻変更要求 | [タスクID] — 現在[旧cron式]→推奨[新cron式] | 未解決 |
```

適用後にsoul-evolution-proposals.md の `## 反映済み変更ログ` に追記。

---

## Step 7: alerts.md への通知

```
| YYYY-MM-DD 08:00 | 🔵 INFO | 投稿時刻最適化分析完了 | [N]件の変更提案を生成 — soul-evolution-proposals.md 参照 | 未解決 |
```

---

## 完了条件
- [ ] 現在スケジュール確認済み
- [ ] 時間帯別パフォーマンス分析完了
- [ ] 最適時刻特定済み
- [ ] soul-evolution-proposals.md に提案登録済み
- [ ] 承認済み提案を自動適用済み（または対象なし）

