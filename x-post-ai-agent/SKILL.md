---
name: x-post-ai-agent
model: openrouter/google/gemini-2.5-flash
description: |
  OpenClaw から X（Twitter、@KURAOpenclaw アカウント）へ AIエージェントシステム関連の自動投稿を行うスキル。
  Playwright＋Cookie認証ベースで、投稿プロトコル（本文250-400字・リプ600-1000字、URL必須、ハッシュタグ/絵文字禁止、末尾「詳細はリプ欄へ」）、ロックファイル、検証、ログ、投稿後検証までを含む。
  以下のフレーズで起動する：
  - 「AIエージェント情報をXで投稿して」
  - 「AIエージェントシステムをツイートして」
  - 「x-post-ai-agent実行」
  `post-to-x.bat` / `post-to-x.js` をPowerShellから呼び出す。AIエージェント・自律AIシステム発信用途。
---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

> ⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

> ⛔ **コンテンツ生成時の絶対禁止事項（これを破ると validate.js が exit 2 で BLOCKING）**:
> - ハッシュタグ（`#AI` 等の `#` 記号を含むすべてのタグ）
> - 絵文字（📰🔗🤖 等あらゆる絵文字）
> - 番号付き絵文字（1️⃣2️⃣ 等）
> - マークダウン記法（`**太字**` `` `code` `` 等）
> - 装飾記号（【】◆◇●▶ 等）
>
> **スクリプト実行は必ず PowerShell で行うこと:**
> ```
> & "C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.bat" "本文" "リプライ文"
> ```

## ⚡ Preflight: Playwright ロック確認（**web_search 開始前・最優先**）

**この確認をコンテンツ生成開始前に必ず実行すること:**

1. Read ツールで `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. **ファイルが存在し、中の `ts` が現在時刻（ms）から600000ms＝10分以内** → 別のX投稿ジョブが実行中  
   Discordに「別ジョブ実行中のためスキップ」と1行報告して即終了
3. **ファイルが存在しない or `ts` が10分超過（stale）** → そのまま続行

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
# x-post-ai-agent スキル（AIエージェントシステム投稿）

## 概要

OpenClaw から X（Twitter）へ AIエージェント・自律AIシステムに関する情報を自動投稿するスキル。
毎日12:00 JSTに実行。最新のAIエージェントフレームワーク、マルチエージェントシステム、AutoGPT系ツールなどを発信。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## アカウント構成

| アカウント | 用途 | Cookieファイル |
|---|---|---|
| `@KURAOpenclaw` | AIエージェント情報発信 | `x-twitter-cookies.json` |

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## テーマ・検索キーワード

以下のキーワードでweb_searchを実行し、最新情報（24時間以内）を取得する:

- "AI agent" OR "AIエージェント" site:github.com OR site:arxiv.org (直近24h)
- "multi-agent system" OR "autonomous AI" (直近24h)
- "LLM agent" OR "agentic AI" (直近1週間)
- OpenAI Swarm、Claude Computer Use、LangGraph、AutoGen、CrewAI の最新動向

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 投稿プロトコル

### 1. リサーチ（5分以内）

web_searchで上記キーワードを検索し、最も価値ある1記事/リポジトリ/論文を選定する。

**選定基準:**
- GitHub star急増（直近24h）
- arXiv新着論文
- 主要AIラボの発表
- 実用的なエージェントフレームワークの新バージョン

### 2. 本文生成（250-400字）

```
[タイトル/見出し]（1行）

[要点を2-3文で説明]

[なぜ重要か・何が変わるか 1-2文]

詳細はリプ欄へ
[URL]
```

**必須:**
- 事実ベース（誇張なし）
- URL必須（記事/論文/GitHubリンク）
- 末尾「詳細はリプ欄へ」
- 250-400字以内

### 3. リプライ生成（600-1000字）

本文の詳細説明:
- 技術的な詳細・実装方法
- ユースケース・活用例
- 他のエージェントフレームワークとの比較（任意）
- 参考リンク（複数可）

### 4. 投稿実行

```powershell
& "C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.bat" "本文テキスト" "リプライテキスト"
```

### 5. 投稿後記録

成功した場合、以下をログに追記:
```
C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md
```

フォーマット: `YYYY-MM-DD HH:MM | x-post-ai-agent | 投稿タイトル | 結果(OK/FAIL)`

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## エラーハンドリング

| エラー | 対処 |
|--------|------|
| ロックファイルあり（10分以内） | スキップして「スキップ」と報告 |
| validate.js exit 2 | ハッシュタグ・絵文字を除去して再試行（1回まで） |
| Playwright timeout | 「投稿失敗: timeout」と報告して終了 |
| web_search 0件 | キーワードを変えて再検索（1回まで）、それでも0件なら「ニュースなし」と報告 |

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了報告フォーマット

必ず以下の形式でDiscordに報告すること:

```
[x-post-ai-agent] YYYY-MM-DD HH:MM JST
状態: 成功/失敗/スキップ
投稿内容: （本文冒頭50字）
URL: （投稿URL or 参照URL）
```
