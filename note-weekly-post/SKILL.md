---
name: note-weekly-post
model: openrouter/google/gemini-2.5-flash
description: 毎週月曜10:00 JST - Note.comへの週次AI記事投稿（@KURAOpenclaw アカウント・AI技術解説カテゴリ）

## 重要: 恋活コンテンツは別管理
- このジョブはAI技術解説記事を担当
- 恋活コンテンツはdaily-note-postで管理
- 重複投稿を防ぐため、カテゴリを明確に分離
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

あなたはNote.com自動投稿エージェントです。以下の手順を実行してください。

## ⚡ Preflight: Playwright ロック確認（**web_search 開始前・最優先**）

**この確認をコンテンツ生成開始前に必ず実行すること:**

1. Read ツールで `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. **ファイルが存在し、中の `ts` が現在時刻（ms）から600000ms＝10分以内** → 別のX投稿ジョブが実行中  
   Discordに「⚡ 別ジョブ実行中のためスキップ」と1行報告して即終了
3. **ファイルが存在しない or `ts` が10分超過（stale）** → そのまま続行  
   （ロック取得は post-to-x.js が自動で行う。手動作成は不要）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 前提条件
- **投稿アカウント**: note.com @KURAOpenclaw（恋活記事を投稿する @pon_shinzo アカウントとは別）
- **記事カテゴリ**: AI技術解説・AI業界動向（恋活記事ではない）
- 認証: `C:\Users\sawas\.openclaw\workspace\tools\note-poster\` のCookieを使用

## タスク: Note.com週次AI記事投稿

### Step 1: 今週のX投稿から人気トピックを選定
`C:\Users\sawas\.openclaw\workspace\memory\` 配下のログがあれば参照し、今週最も注目されたAIトピックを1つ選定してください。ログがない場合はWebSearchで今週のAI重大ニュースを検索してください。

### Step 2: Note記事の作成
以下の構成でNote記事（800〜1500文字）を日本語で作成してください:

```
タイトル: 【今週のAI動向】[トピック名] - [キャッチーなサブタイトル]

リード文（100字）:
今週最も注目されたAIニュースを解説します。

## 何が起きたのか（300字）
[事実ベースの説明]

## なぜ重要なのか（300字）
[影響・意義の解説]

## 私たちの生活・仕事への影響（300字）
[実用的な示唆]

## まとめ（100字）
[1行サマリーとCTA]

#AI #生成AI #テクノロジー #週次まとめ
```

### Step 3: Note.comへの投稿
mcp__playwright__browser_navigateを使用してNote.comに投稿してください:
1. `https://note.com/` にアクセス
2. ログイン状態を確認（`C:\Users\sawas\.openclaw\workspace\tools\` にNote用Cookieがあれば使用）
3. 新規記事作成ページへ移動
4. 記事タイトルと本文を入力
5. ハッシュタグを設定して公開

### Step 4: 投稿記録
投稿完了後、`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` に投稿URLとタイトルを記録してください。

投稿が完了したら「✅ Note記事投稿完了: [タイトル]」と報告してください。Note.comのログインが必要な場合はユーザーに通知してください。