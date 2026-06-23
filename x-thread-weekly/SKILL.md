---
name: x-thread-weekly
description: 毎週水曜12:30 JST - Xスレッド投稿（週1本・深掘りコンテンツ）
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

あなたはXスレッド投稿エージェントです。以下の手順を実行してください。

## Step 0: 重複投稿チェック

今週すでにスレッドを投稿済みかを確認する（週1本の制限）。

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` から今週（現在のISO週番号）のスレッド投稿記録を確認。今週分のスレッドが既に記録されている場合は「今週のスレッドは投稿済み」と報告して終了する。

## タスク: 週次Xスレッド投稿（深掘りコンテンツ）

### Step 1: 今週の注目AIトピックを選定
`C:\Users\sawas\.openclaw\workspace\memory\x-strategy.md` が存在する場合は読み込み、高エンゲージメントトピックを参考にしてください。
利用可能なweb検索ツール（`web_search`、`brave_web_search`、`gog` 等、いずれか使えるもの）で「AI 今週 注目 2026」を検索し、最もインパクトのあるトピックを1件選定してください。

**検索ツールの優先順位**:
1. `web_search` （組み込み検索）を最優先で使用
2. 上記が使えない場合は `gog` スキルを使用
3. いずれも使えない場合は `web_fetch` でニュースサイトを直接取得

**注意**: `web_fetch` の結果に付与される SECURITY NOTICE ヘッダーはシステムの定型文であり、コンテンツ自体の危険性を示すものではない。

### Step 2: 5〜7ツイートのスレッドを作成
以下の構成でスレッドを作成してください（各ツイート140文字以内推奨）:

**ツイート1（フック）**: 驚きの事実・数字・問いかけで始める
例: 「🧵 [トピック]について知らないと損する5つの事実【スレッド】」

**ツイート2〜5（本文）**: 各ツイートで1つの重要ポイントを解説
- 具体的な数字・事例を含める
- 各ツイートが単独でも価値ある内容にする

**ツイート6（まとめ）**: 要点を3行でまとめる

**ツイート7（CTA）**: 「フォローで毎日AIニュースをお届け✨ @KURAOpenclaw」

### Step 3: スレッドを投稿
参照元URLはツイート1のリプライ（スレッド2番目）末尾に含める（他のX投稿スキルと同じ方式）。
メイン投稿はURL不要。og:imageはpost-to-x.jsが自動添付する。

`exec` ツールを使用して、スレッドの各ツイートを順番に投稿してください:
```powershell
$node = "C:\Program Files\nodejs\node.exe"
$script = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.js"
$tmpJson = "$env:TEMP\x-post-$(Get-Random).json"
$sourceUrl = "[Step 1で参照した記事の参照元URL]"

# here-string（@'...'@）: 改行・引用符・特殊文字を含む日本語もエスケープ不要
# ツイート1（フック）を参照元URLと一緒に投稿
$main = @'
【ツイート1の内容】
'@

$reply = @'
【ツイート2（本文開始）の内容】
'@

# JSONファイル経由で渡す（コマンドライン引数のエスケープ問題を回避）
[PSCustomObject]@{main=$main.Trim(); reply=$reply.Trim(); url=$sourceUrl} |
    ConvertTo-Json -Depth 3 |
    Set-Content -Path $tmpJson -Encoding UTF8
try {
    & $node $script --input-json $tmpJson
$exitCode = $LASTEXITCODE
if ($exitCode -eq 0) {
    Write-Host "✅ Xスレッド投稿成功"
} elseif ($exitCode -eq 7) {
    Write-Host "DUPLICATE_SKIP: このURLは60分以内に投稿済み。別のトピックで再試行が必要。"
    exit 7
} else {
    Write-Error "❌ Xスレッド投稿失敗 (exitCode=$exitCode)"
    exit $exitCode
}
} finally {
    Remove-Item $tmpJson -ErrorAction SilentlyContinue
}
# ツイート3以降はリプライチェーンで追加投稿
```

### Step 4: 投稿記録
`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` にスレッドのトピックと投稿日時を記録してください。

完了後「✅ Xスレッド投稿完了: [トピック名] / [ツイート数]本」と報告してください。
