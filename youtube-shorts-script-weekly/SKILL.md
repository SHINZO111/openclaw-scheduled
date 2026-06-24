---
name: youtube-shorts-script-weekly
description: 毎週金曜16:00 JST - 週間バズ投稿TOP3からYouTube Shorts台本3本を自動生成・保存
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

# YouTube Shorts 台本自動生成タスク — 毎週金曜16:00 JST

## 目的
今週のX投稿TOP3から、60秒以内で読める縦型ショート動画台本を3本生成し、SHINZOが撮影・編集できる状態にして保存する。

## Step 1: 今週のバズ投稿TOP3を取得
以下のファイルを Read して情報を取得:
- `C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` → 今週（月〜金）のエンゲージメント上位投稿
- `C:\Users\sawas\.openclaw\workspace\memory\cron-logs\viral-amplifier-daily.md` → バズパターンの参考

TOP3を選定基準: いいね数 > RT数×3 > IMP で重み付けスコア計算

## Step 2: YouTube Shorts台本を生成
各投稿から以下のフォーマットで台本を作成:

```
【台本テンプレート（60秒/約300文字）】

[0-5秒] フック（画面テキスト + ナレーション）
「え、これ知らないと損する？」
→ 超具体的な数字or驚き事実を1行で

[5-45秒] 本題（3ポイント構成）
ポイント1: [内容 + 画面テキスト案]
ポイント2: [内容 + 画面テキスト案]
ポイント3: [内容 + 画面テキスト案]

[45-55秒] まとめ
「つまり〜ということ」

[55-60秒] CTA
「@KURAOpenclawをフォローで毎日AIニュース届きます」

【撮影メモ】
- 背景: [シンプル推奨/ホワイトボード/etc]
- テロップ案: [キーワードリスト]
- BGM雰囲気: [テンポ感の指定]
- サムネイル文言: [クリックされやすいタイトル案]
```

## Step 3: ファイルに保存
```
保存先: C:\Users\sawas\.openclaw\workspace\content\youtube-shorts\YYYY-WW\
ファイル名: shorts_script_01.md / 02.md / 03.md
```

`Write` ツールで保存する。

## Step 4: サマリーをSHINZOに通知
```
✅ YouTube Shorts台本 3本生成完了 [YYYY-MM-DD週]

📹 台本01: [トピック名] (推定エンゲージメント: HIGH/MID/LOW)
📹 台本02: [トピック名]
📹 台本03: [トピック名]

保存先: C:\Users\sawas\.openclaw\workspace\content\youtube-shorts\YYYY-WW\
```

## 注意
- 実際の動画投稿はSHINZOが撮影・編集・アップロード（自動投稿なし）
- 台本の長さは必ず300文字以内（60秒以内）に収める
- 各台本は独立して完結する内容にする