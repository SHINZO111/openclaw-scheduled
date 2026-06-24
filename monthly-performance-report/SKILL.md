---
name: monthly-performance-report
description: 毎月1日00:00 JST - 月次パフォーマンスレポート＋能力ベンチマーク
---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
<!-- Merged: capability-benchmark-monthly (旧:28日05:00) + monthly-performance-report (1日05:00) → 統合版 1日05:00 -->

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

あなたは月次レポートエージェントです。以下の手順を実行してください。

## タスク: 月次パフォーマンスレポート生成

### Step 1: データ収集
以下のファイルを読み込んでください:
- `C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md`
- `C:\Users\sawas\.openclaw\workspace\memory\learnings.md`
- `C:\Users\sawas\.openclaw\workspace\memory\failures.md`（存在する場合）
- `C:\Users\sawas\.openclaw\backups\backup-log.txt`（存在する場合）

### Step 2: 月次サマリーの算出
先月のデータを集計してください:
- X投稿: 実施件数 / 目標件数（12件/日 × 日数）= 達成率
- バックアップ: 成功日数 / 総日数
- エラー発生件数とカテゴリ別分類
- 改善サイクルの実施回数
- 最も多く使われたスキル・ツール

### Step 3: 能力ベンチマーク（capability-benchmark-monthly統合）

開始時刻を記録。以下の5タスクを順次実行する（投稿は実行しない）:

**BM-01: X投稿文生成速度テスト**
web_search で「AI 最新ニュース 今日」を検索→最も重要なニュース1件選定→280文字以内のX投稿文生成。所要秒数と品質自己評価(1-5)を記録。

**BM-02: learnings.md 要約速度テスト**
`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` を Read→100文字以内の要約生成。所要秒数と情報網羅度(1-5)を記録。

**BM-03: ルールチェック速度テスト**
`C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md` を Read→「X投稿関連ルール」を全て列挙。所要秒数と網羅性(1-5)を記録。

**BM-04: メトリクス読み取り精度テスト**
`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` から解決率・防止率・PEND件数・総セッション数を報告。所要秒数を記録。

**BM-05: トレンド取得速度テスト**
web_search で「AI 最新トレンド 今週」を検索→上位3トピック列挙。所要秒数と鮮度(1-5)を記録。

**結果集計:** 全5タスクの速度スコア(平均秒数)と品質スコア(平均点)を算出。
**benchmark-log.md 更新:** `C:\Users\sawas\.openclaw\workspace\memory\benchmark-log.md` に今月の結果と前月比を追記。
**退化検出:** いずれかで前月比-15%以上退化 → alerts.md に🟠警告。

### Step 4: 月次レポートファイルの生成
Write ツールまたは exec ツールを使用して保存:
```powershell
$month = (Get-Date).AddMonths(-1).ToString("yyyy-MM")
$reportPath = "C:\Users\sawas\.openclaw\workspace\reports\monthly-$month.md"
New-Item -ItemType Directory -Force -Path "C:\Users\sawas\.openclaw\workspace\reports"
```

以下の形式でレポートを作成して保存してください:
```markdown
# 月次パフォーマンスレポート: [YYYY年MM月]

## 📊 KPIサマリー
- X投稿達成率: XX% (XXX/XXX件)
- バックアップ成功率: XX% (XX/XX日)
- エラー発生件数: XX件
- 改善サイクル実施: XX回

## 🏆 今月のハイライト
[主な成果・改善点]

## ⚠️ 課題と対策
[失敗パターンと対策]

## 🏁 能力ベンチマーク
| タスク | 今月(秒) | 先月(秒) | 変化 |
|--------|---------|---------|------|
| BM-01 X投稿生成 | X | Y | ±Z% |
| BM-02 要約生成 | X | Y | ±Z% |
| BM-03 ルールチェック | X | Y | ±Z% |
| BM-04 メトリクス読取 | X | Y | ±Z% |
| BM-05 トレンド取得 | X | Y | ±Z% |
| 総合スコア | X | Y | ±Z% |

## 📈 来月の重点目標
1. [目標1]
2. [目標2]
```

### Step 5: growth-metrics.mdに月次サマリーを追記
生成したレポートのサマリー版を `growth-metrics.md` に追記してください。

完了後、レポートの主要KPIをユーザーに報告してください。