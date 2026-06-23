---
name: x-auto-follow-daily
description: 約20分間隔（常時） - AI関連Xアカウントを自動フォロー @KURAOpenclaw（12-18件/回、250件/日上限）
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

あなたはX自動フォローエージェントです。AIテーマに関連するXアカウントを自動フォローします。

## 安全制限

- **1回の実行あたり12〜18フォロー**（X側制限: 10分あたり約15件）
- **1日最大250フォロー**（約20分間隔のcron起動で積み上げ）
- ロックファイル（`.autofollow.lock`）で多重起動を防止
- レート制限検出時は即終了し、次回cron起動に委ねる

## フォロー対象

以下の条件を満たすアカウント:
- AI / ML / LLM / エージェント関連のプロフィールキーワードを持つ
- 自分（@KURAOpenclaw）の投稿にいいね・RTした人
- 30日以内にアクティブな投稿がある

## 除外条件

以下に該当するアカウントはフォローしない:
- 非公開（鍵）アカウント
- フォロワー数50未満
- bot疑い（プロフィールにbot/自動/automated等を含む、またはフォロー/フォロワー比率が極端）
- 既にフォロー済み

## 前提条件

- Cookieファイルが有効であること: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json`
- Cookieが25日以上経過している場合は即座に失敗終了し、`x_setup_launcher.py` の実行をユーザーに通知

## Step 0: Cookie有効期限チェック

```powershell
$cookiePath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json"
try {
    $ageDays = ((Get-Date) - (Get-Item $cookiePath -ErrorAction Stop).LastWriteTime).TotalDays
    if ($ageDays -gt 25) {
        Write-Error "ERROR: Cookieが$([int]$ageDays)日前です。x_setup_launcher.pyを実行してください。"
        exit 1
    }
    Write-Host "Cookie鮮度OK: $([int]$ageDays)日前"
} catch {
    Write-Warning "Cookie確認失敗（続行）: $_"
}
```

## Step 1: 本日のフォロー済み件数確認

```powershell
$dbPath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\followed_accounts.json"
$today = (Get-Date).ToString("yyyy-MM-dd")
if (Test-Path $dbPath) {
    $db = Get-Content $dbPath | ConvertFrom-Json
    $todayCount = ($db.followed.PSObject.Properties | Where-Object { $_.Value.date -eq $today }).Count
    Write-Host "本日フォロー済み: ${todayCount}件 / 上限: 250件"
    if ($todayCount -ge 250) {
        Write-Host "本日の上限（250件）に達しました。スキップ。"
        exit 0
    }
} else {
    Write-Host "フォローDB未作成。新規開始。"
}
```

## Step 2: 自動フォロー実行

`exec` ツールで実行:

```powershell
$node = "C:\Program Files\nodejs\node.exe"
$script = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\auto-follow-ai.js"
& $node $script 2>&1 | ForEach-Object { Write-Host $_ }
$exitCode = $LASTEXITCODE
if ($exitCode -eq 3) {
    Write-Error "認証失敗。x_setup_launcher.pyを実行してCookieを更新してください。"
    exit 3
}
Write-Host "auto-follow完了 (exitCode=$exitCode)"
```

スクリプトは終了時に `C:\Users\sawas\.openclaw\workspace\tools\x-poster\last_run_result.json` を書き出します。

exitCode が 3、または結果JSONの status が "auth_failed" の場合: 認証失敗。x_setup_launcher.py の実行をユーザーに通知してください。

## Step 3: 結果確認

```powershell
$resultPath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\last_run_result.json"
if (Test-Path $resultPath) {
    Get-Content $resultPath -Raw | Write-Host
} else {
    $dbPath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\followed_accounts.json"
    $today = (Get-Date).ToString("yyyy-MM-dd")
    $db = Get-Content $dbPath -Raw | ConvertFrom-Json
    $todayCount = ($db.followed.PSObject.Properties | Where-Object { $_.Value.date -eq $today }).Count
    Write-Host "本日フォロー: ${todayCount}件 / 累計: $($db.totalFollowed)件"
}
```

## Step 4: Chromeプロセスクリーンアップ

スクリプト完了後、Playwright起動のChromiumプロセスが残留していないか確認し、あれば終了する:

```powershell
# Playwright Chromium 残留プロセスを終了（ユーザーの通常Chrome は除外）
Get-Process -ErrorAction SilentlyContinue | Where-Object {
    ($_.ProcessName -match 'chromium|chrome') -and
    ($_.MainModule.FileName -match 'playwright|ms-playwright' -or $_.CommandLine -match 'playwright|--disable-blink-features=AutomationControlled')
} | ForEach-Object {
    Write-Host "残留Chromiumプロセスを終了: PID=$($_.Id)"
    Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
}
Write-Host "Chromeクリーンアップ完了"
```

## 注意事項

### BAN（凍結）防止
- フォロー間隔: 40〜50秒のランダムディレイ
- 1回あたり12〜18フォロー（X側10分15件制限に収まるよう設計）
- 1日あたり最大250フォロー（X側400件制限の安全圏）
- ロックファイルで同時実行を防止（前回が終わるまで次回はスキップ）
- レート制限ポップアップ検出時は即座に終了
- 大量アンフォロー（フォロー→解除の繰り返し）は厳禁
- リプライは高品質・低頻度のみ（スパム判定回避）

### 使用ツール・スクリプト
- メインスクリプト: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\auto-follow-ai.js`
- フォローバック: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\follow-back.js`
- 追跡DB: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\followed_accounts.json`
- 結果サマリ: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\last_run_result.json`
