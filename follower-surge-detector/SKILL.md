---
name: follower-surge-detector
model: lmstudio/nvidia/nemotron-3-nano-4b
description: 毎日00:00 JST - @KURAOpenclawフォロワー数を前日比較し急増（+50人/日）を検知・分析
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

# フォロワー急増検知タスク — 毎日00:00 JST

## 目的
@KURAOpenclawのフォロワー数を毎日記録し、急増（+50人/日）を検知した際に原因を即時分析してバズ増幅アクションを提案する。

## Step 1: 現在のフォロワー数を取得
`mcp__brave-search__brave_web_search` で `KURAOpenclaw X followers site:x.com` を検索し、
またはXプロフィールURL `https://x.com/KURAOpenclaw` を `mcp__workspace__web_fetch` で取得して
フォロワー数を抽出する。

取得できない場合は `exec` ツールで以下を実行:
```powershell
node "C:\Users\sawas\.openclaw\workspace\tools\get-x-profile.js" --user KURAOpenclaw
```
スクリプトが存在しない場合は Brave Search 結果からフォロワー数を推定する。

## Step 2: 前日データと比較
`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` を読み込み、前日のフォロワー数を取得

差分を計算:
- +50人以上 → 🚀 急増検知
- +10〜49人 → 📈 順調増加
- ±10人 → 📊 平常運転
- -10人以下 → 📉 減少（要確認）

## Step 3: 急増時の原因分析（+50人以上の場合）
1. 本日の投稿エンゲージメントを `C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` から取得
2. 急増のトリガーとなった投稿を特定（エンゲージメント急上昇）
3. バイラル要因を分析（トピック・表現・時間帯）
4. `viral-amplifier-daily` と連携して増幅コンテンツを即時生成

## Step 4: フォロワー数をファイルに記録
`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` に以下を追記:
```
## YYYY-MM-DD フォロワー記録
- 日時: YYYY-MM-DD
- フォロワー数: [N]
- 前日比: +[N] ([N]%増)
- 判定: [急増/順調/平常/減少]
- バズ投稿: [あれば記録]
```

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\follower-surge-detector.md` にも実行ログを追記。

## Step 5: 通知レポート
```
📊 フォロワー数レポート [YYYY-MM-DD]
現在: [N]人（前日比: +[N]）
判定: [🚀急増 / 📈順調 / 📊平常 / 📉減少]

[急増時のみ]
🎯 急増トリガー: [投稿内容]
💡 推奨アクション: [増幅コンテンツ案]
```

## 注意
- フォロワー数データは30日間保持
- 急減の場合はアカウント凍結リスクを確認（違反コンテンツないか確認）