---
name: x-dm-welcome-daily
model: openrouter/google/gemini-2.5-flash
description: 毎日23:00 JST - 新フォロワーにウェルカムDMを自動送信（フォロワーとの初期関係構築）
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

## 前提条件
- Playwright chromiumバイナリが存在すること（C:\Users\sawas\AppData\Local\ms-playwright\ 配下）
- バイナリが存在しない場合、このジョブは即座に失敗終了すること（ダウンロードを試みない）

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
# X 新フォロワー ウェルカムDM タスク — 毎日23:00 JST

## ⚠️ ToS・運用ルール
- TwitterのToSではDM自動送信は**規約上グレーゾーン**。1日5件以内の少量運用を厳守。
- フォロワーが急増している日（+50人/日超）は自動送信を**停止**してSHINZOに通知する。
- Xがレート制限・アカウント警告を出した場合は即時停止してSHINZOに報告する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: フォロワーページからユーザー名を取得

Playwright で followers ページを直接スクレイプしてユーザー名を取得する。
ユーザーIDはスナップショットのテキストから直接取得できないため、
**プロフィールURLのパス（`/username`部分）** からユーザー名を取得する。

```
mcp__playwright__browser_navigate(url="https://x.com/KURAOpenclaw/followers")
mcp__playwright__browser_snapshot()
```

スナップショットのリンク一覧（`href="/[username]"` 形式）から
フォロワーのユーザー名リストを抽出する（最大20件確認）。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: 既送信リストと照合して新規フォロワーを特定

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\x-dm-welcome-daily.md` を Read して既送信ユーザー一覧を取得する。

取得したユーザー名リストから、既送信リストにないユーザーを抽出。
新規フォロワーを最大5名まで選定する（古い順）。

新規フォロワーが0名の場合: 「新規フォロワーなし」と記録して終了。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: DM送信（ユーザー名ベースのURL使用）

X のDM compose画面は `recipient_id`（数値ID）が必要だが、
Playwright経由では数値IDの安定取得が困難なため、
**ユーザーのプロフィールページからDMアイコンをクリック**する方法を使用する。

各対象フォロワーに対して:
```
# 1. プロフィールページに移動
mcp__playwright__browser_navigate(url="https://x.com/[username]")
mcp__playwright__browser_snapshot()

# 2. プロフィールを確認（エンジニア/ビジネス/一般を判定）

# 3. DMボタン（封筒アイコン）をクリック
mcp__playwright__browser_click(selector="[aria-label='メッセージを送る'] or [data-testid='sendDMFromProfile']")
mcp__playwright__browser_snapshot()

# 4. メッセージを入力（クリップボード経由）
mcp__playwright__browser_type(text="[DMテンプレート]")

# 5. 送信（Ctrl+Enter または送信ボタン）
mcp__playwright__browser_key_press(key="Control+Enter")
```

**DMテンプレート（プロフィール別）:**
```
# エンジニア系フォロワー向け
フォローありがとうございます！AIエージェント・ローカルLLMの情報を毎日発信しています。技術的な質問もお気軽に 🤖

# ビジネス系フォロワー向け
フォローありがとうございます！AIを活用した業務改善情報を毎日お届けしています。何かご質問があればどうぞ！

# 一般向け（デフォルト）
フォローありがとうございます！毎日AIの最新情報を発信しています。質問・感想はお気軽にどうぞ 🤖
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: 送信記録をログファイルに保存

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\x-dm-welcome-daily.md` に追記:
```markdown
## WelcomeDM_Sent_[username]
- 送信日時: YYYY-MM-DD HH:mm
- ユーザー名: @[username]
- テンプレート: [種別]
- 送信成功: true/false
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: 異常検知

以下の状況が発生した場合は即時停止してSHINZOに通知:
- Xからエラー「このアカウントはDM機能が制限されています」
- レート制限エラー（429）
- 連続5件以上の送信失敗
- その日のフォロワー増加数が+50人超

```powershell
$msg = "⚠️ X DM送信を停止しました。理由: [原因]`n手動確認をお願いします。"
[System.Windows.Forms.MessageBox]::Show($msg, "X DM 警告")
```
