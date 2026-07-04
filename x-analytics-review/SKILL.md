---
name: x-analytics-review
description: 毎週日曜05:00 JST。@KURAOpenclaw の直近投稿のインプレッション・エンゲージメントを収集し x-performance-log.md に構造化記録する
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: cron.run / cron.list 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

## Step 1: 収集スクリプト実行
exec: node C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-analytics-scrape.js
（自プロフィールの直近20投稿+直近リプライのviews/like/RT/replyをDOMから取得しJSON出力）

> ⚠️ **前提**: `x-analytics-scrape.js` は未実装（実装工数目安: 半日）。post-to-x.jsのstealth基盤・Cookie読込を流用し、x.com/KURAOpenclaw を開き記事セルからviews数値を抽出する実装が必要。Premium加入済みならAnalyticsページ経由の方が正確なので加入状態を先に確認すること。
> スクリプトが存在しない/失敗する間は、Step 2以降をスキップし「⚠️ 収集失敗: x-analytics-scrape.js未実装」をStep 4形式でDiscordに報告して終了する（空レスポンス禁止）。

## Step 2: 結果読込
Read: C:\Users\sawas\.openclaw\workspace\tools\x-poster\analytics_result.json

## Step 3: ログ追記
C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md に追記:
| 日付 | 種別(post/reply) | ID | imp | like | RT | reply | テーマ |

週間サマリ（合計imp・トップ3・ワースト3・前週比）も同ファイル冒頭に更新。

## Step 4: Discord報告
「📊 週間imp合計 / 前週比 / トップ投稿」を1メッセージで報告。
スクリプト失敗時は「⚠️ 収集失敗: [理由]」を報告して終了（空レスポンス禁止）。