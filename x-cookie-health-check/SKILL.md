---
name: x-cookie-health-check
description: 毎週日曜07:00 JST - Cookie有効性チェック（@KURAOpenclaw + @pon_shinzo 両対応）
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

毎週日曜日にXの Cookie 有効性をチェックします（@KURAOpenclaw + @pon_shinzo 両対応）。

---

## Step 1: @KURAOpenclaw Cookie チェック

> ⚠️ **注**: `mcp__playwright__` は isolated cron セッションでは使用不可。代わりにCookieファイルのJSON直接解析で有効期限を確認する。

PowerShellでCookieファイルを読み込み、`auth_token` の有効期限（expiry フィールド = Unixタイムスタンプ）を確認する:

```powershell
$cookiePath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json"
$cookies = Get-Content $cookiePath | ConvertFrom-Json
$authToken = $cookies | Where-Object { $_.name -eq "auth_token" }
$now = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
if ($authToken -and $authToken.expiry -gt $now) {
    Write-Host "VALID: auth_token expires $(([DateTimeOffset]::FromUnixTimeSeconds($authToken.expiry)).ToString('yyyy-MM-dd'))"
} else {
    Write-Host "EXPIRED or MISSING: auth_token"
}
```

結果:
- VALID → 「✅ @KURAOpenclaw Cookie 有効（期限: YYYY-MM-DD）」を記録
- EXPIRED or MISSING → Step 3 へ進む（失効アラート）

---

## Step 2: @pon_shinzo Cookie チェック（設定済みの場合のみ）

`C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies-pon.json` が存在するか確認する。

存在する場合: 同様に PowerShell で auth_token の expiry を確認する。
存在しない場合: 「⏳ @pon_shinzo: Cookie未設定（setup-guide参照）」を記録してスキップ。

---

## Step 3: Cookie 失効時のアラート

いずれかのアカウントで Cookie が失効していた場合:

1. `C:\Users\sawas\.openclaw\workspace\memory\alerts.md` に追記:
```
## 🔴 [YYYY-MM-DD] Cookie失効アラート
- アカウント: @[account]
- 症状: [ログインページにリダイレクト / タイムアウト / etc.]
- 対処: RULE-T01「Cookie更新手順」に従って .env を更新してください
  1. Chromeで該当アカウントにログイン
  2. F12 → Application → Cookies → x.com
  3. auth_token と ct0 をコピー
  4. C:\Users\sawas\.openclaw\.env を更新
  5. setup-cookies.js を実行
```

2. 同時に、今後 24 時間以内の X 投稿タスクが失敗するリスクがあることを明示する

---

## Step 4: チェック結果を記録する

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` の冒頭（または既存の「Cookie健全性」セクション）に今週の結果を追記する:

```
## ✅ [YYYY-MM-DD] Cookie健全性チェック
- @KURAOpenclaw: [有効/失効]
- @pon_shinzo: [有効/失効/未設定]
- 次回チェック: [来週日曜]
```

---

## 完了宣言

「🔑 Cookie健全性チェック完了 YYYY-MM-DD | @KURAOpenclaw: [結果] | @pon_shinzo: [結果]」