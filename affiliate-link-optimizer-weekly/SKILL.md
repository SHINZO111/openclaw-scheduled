---
name: affiliate-link-optimizer-weekly
description: 毎週月曜12:00 JST - 先週の高エンゲージメント投稿にアフィリエイトリンクを付与・収益化候補を提案
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

# アフィリエイトリンク最適化タスク — 毎週月曜12:00 JST

## 目的
先週の高エンゲージメントX投稿・note記事を分析し、関連するアフィリエイト商品を提案。収益化の機会を最大化する。

## Step 1: アフィリエイトプログラム設定を読み込む
`C:\Users\sawas\.openclaw\workspace\config\affiliate-programs.md` を読み込む。
存在しない場合は以下の内容でファイルを作成（⚠️ 設定値は初回実行後に必ずSHINZOが更新すること）:
```markdown
# アフィリエイトプログラム設定

## Amazonアソシエイト
- アソシエイトID: 未設定（https://affiliate.amazon.co.jp/ で取得後、このファイルを更新すること）
- 対象カテゴリ: AIツール関連書籍、PCハードウェア

## もしもアフィリエイト / A8.net
- 登録済みサービス: 未登録（https://www.moshimo.com/ / https://www.a8.net/ で登録後に追記）

## 直接アフィリエイト提携
- Cursor AI: 未設定（https://cursor.com/affiliates で申請後に追記）
- Claude API: Anthropicは現在公式アフィリエイトなし。紹介コード等が公開されたら追記
```

## Step 2: 先週のトップ投稿を取得
`C:\Users\sawas\.openclaw\workspace\memory\` ディレクトリ内のファイル（x-performance-log.md、growth-metrics.md 等）を読み込み、先週（月〜日）のエンゲージメント上位10投稿を取得。

## Step 3: トピックとアフィリエイトのマッチング
各投稿トピックに対して関連商品・サービスを提案:

| トピック | 提案アフィリエイト商品 | 想定クリック率 |
|---------|-----------------|------------|
| AI PC / ローカルLLM | NVIDIA GPU、AI PC本 | 高 |
| 生成AIツール | Midjourney、Cursor、Claude Pro | 高 |
| AI株 | 証券口座紹介、投資本 | 中 |
| AI医療/健康 | 健康管理アプリ | 低 |

## Step 4: 収益化アクション案を生成
以下の形式でレポートを `C:\Users\sawas\.openclaw\workspace\reports\affiliate-weekly-YYYYMMDD.md` に保存:

```markdown
# アフィリエイト最適化レポート [YYYY-MM-DD週]

## 今週の収益化機会トップ3

### 1位: [投稿トピック]
- エンゲージメント: いいね[N] / IMP[N]
- 推奨アフィリエイト: [商品名] ([プログラム名])
- アクション: note記事末尾にリンク追加 / X投稿にリプライ追加

### 2位: ...

## 今週の推定収益ポテンシャル
- クリック予測: 約[N]回
- 推定収益: ¥[N]〜¥[N]

## 来週への提案
[次週どのトピックを強化すべきか]
```

## Step 5: SHINZOへ通知
上記レポートのサマリーを表示する。実際のリンク設置はSHINZOが確認・判断して行う。