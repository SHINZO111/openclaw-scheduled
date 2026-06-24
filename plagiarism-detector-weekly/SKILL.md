---
name: plagiarism-detector-weekly
description: 毎週木曜08:00 JST - note・Qiita・Zenn記事の無断転載をGoogle検索で自動検知
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

# 無断転載・盗用検知タスク — 毎週木曜08:00 JST

## 目的
note・Qiita・Zenn等に投稿した記事の無断転載・盗用をGoogle検索で週次に検知し、コンテンツ権利を保護する。

## Step 1: チェック対象記事を収集
`C:\Users\sawas\.openclaw\workspace\memory\posted-articles.json` または Memory MCPから直近30日以内の投稿記事リストを取得。

チェック対象: 各記事の固有フレーズ（タイトル・冒頭の独自表現）を3〜5個抽出。

## Step 2: Google検索で無断転載を確認
各記事の固有フレーズをGoogle検索して、自サイト以外での掲載を確認:
```
検索クエリ例:
"[記事の固有フレーズ]" -site:note.com -site:qiita.com -site:zenn.dev -site:x.com
```

`mcp__brave-search__brave_web_search` を使用（優先）。brave-searchが使えない場合は `WebSearch` ツールを使用。
> ⚠️ **注**: `mcp__playwright__browser_navigate` は isolated cron セッションでは使用不可のため使用しないこと。

## Step 3: 検索結果を評価
各結果を以下のカテゴリに分類:
- ✅ 正規引用（出典明記あり）→ 無視
- ⚠️ 部分転載（出典なし）→ 要確認
- 🚨 完全無断転載 → 即時通知・対応検討
- 🔍 類似コンテンツ（偶然の一致可能性）→ 記録のみ

## Step 4: 疑わしいサイトの詳細確認
`mcp__workspace__web_fetch` で疑わしいURLにアクセスし（`mcp__playwright__` は isolated cron 不可）:
- 公開日時を確認（自分の投稿より後か）
- 著者名・出典表記を確認
- コンテンツの一致度を確認（30%以上一致 = 転載の疑い）

## Step 5: レポートを保存・通知
`C:\Users\sawas\.openclaw\workspace\reports\plagiarism-check-YYYYMMDD.md` に保存:

```markdown
# 無断転載チェックレポート [YYYY-MM-DD]

## チェック記事数: [N]本

## 検知結果
### 🚨 要対応 ([N]件)
- URL: [転載先URL]
- 元記事: [タイトル]
- 一致度: [N]%
- 推奨アクション: [削除依頼文テンプレートを生成]

### ⚠️ 要確認 ([N]件)
...

### ✅ 問題なし ([N]件)
```

🚨検知時はCoworkセッションに即時アラート + 削除依頼メール文を自動生成。

## 注意
- 過去にチェック済みURLは再チェック不要（Memoryで管理）
- 海外サイトへの対応は英語メールテンプレートを使用