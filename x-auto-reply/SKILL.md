---
name: x-auto-reply
model: openrouter/google/gemini-2.5-flash
description: |
  X（Twitter）自動リプライ監視システムの管理スキル。
  @KURAOpenclaw アカウントの指定ユーザーの投稿を自動検知し、AIでリプライ文を生成・送信する。
  以下のフレーズで起動する：
  - 「X自動リプライを設定して」
  - 「リプライ監視を追加して @handle」
  - 「X自動リプライのステータス確認」
  - 「リプライ統計を見せて」
  - 「X監視を起動/停止して」
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。

> ⛔ **[SYSTEM CONSTRAINT]**: cronツールは絶対使用禁止。エラーが発生した場合はDiscordで報告して終了する。

---

## ⚡ Preflight: Playwright ロック確認（**web_search 開始前・最優先**）

**この確認をコンテンツ生成開始前に必ず実行すること:**

1. Read ツールで `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. **ファイルが存在し、中の `ts` が現在時刻（ms）から600000ms＝10分以内** → 別のX投稿ジョブが実行中  
   Discordに「⚡ 別ジョブ実行中のためスキップ」と1行報告して即終了
3. **ファイルが存在しない or `ts` が10分超過（stale）** → そのまま続行  
   （ロック取得は post-to-x.js が自動で行う。手動作成は不要）

---

# X 自動リプライ監視システム管理スキル

## システム概要

| 要素 | 詳細 |
|------|------|
| ベースディレクトリ | `F:\OpenClaw\x_monitor\` |
| スクリプト | `F:\OpenClaw\x_monitor\scripts\` |
| Python venv | `F:\OpenClaw\venv\Scripts\python.exe` |
| DB | `F:\OpenClaw\x_monitor\monitor.db` |
| 設定 | `F:\OpenClaw\x_monitor\config.json` |
| アカウント | `F:\OpenClaw\x_monitor\accounts.json` |
| ログ | `F:\OpenClaw\x_monitor\logs\` |
| Cookie | `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json` |

## Task Schedulerタスク

| タスク名 | 役割 | 実行間隔 |
|---------|------|---------|
| `OpenClaw_XMonitor_Poll` | TLスクレイプ→AI生成→待機キュー投入 | 5分ごと |
| `OpenClaw_XMonitor_Sender` | 待機中リプライを送信 | 30秒ごと |
| `OpenClaw_XMonitor_Cancel` | キャンセルサーバー（Flask localhost:19876） | 起動時常駐 |

---

## コマンド別手順

### 🟢 ステータス確認

```powershell
# Task Schedulerの状態
$tasks = @("OpenClaw_XMonitor_Poll","OpenClaw_XMonitor_Sender","OpenClaw_XMonitor_Cancel")
$tasks | ForEach-Object {
    $t = Get-ScheduledTask -TaskName $_ -ErrorAction SilentlyContinue
    if ($t) { "$_ : $($t.State)" } else { "$_ : 未登録" }
}

# 直近7日間の統計
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 7

# 最新ログ（直近20行）
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content -Tail 20
```

結果を以下の形式で報告:
```
✅ X自動リプライ ステータス YYYY-MM-DD
- Poll: [Running/Ready/未登録]
- Sender: [Running/Ready/未登録]
- CancelServer: [Running/Ready/未登録]
- 直近7日 送信: N件 / 生成: N件
- 最終エラー: [なし / 内容]
```

---

### ➕ 監視アカウント追加

ユーザーから `@handle` を受け取り、以下を実行:

```powershell
# アカウント追加（category: ai/tech/business/general）
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" `
    add-account "@handle" `
    --priority NORMAL `
    --category general `
    --max-daily 3
```

**優先度の判断基準:**
- `HIGH`: フォロワー10万超 or ビジネス上重要
- `NORMAL`: 通常監視対象

**カテゴリの選択:**
- `ai`: AI・機械学習関連アカウント
- `tech`: テック・エンジニア系
- `business`: ビジネス・スタートアップ系
- `general`: その他

追加後、accounts.jsonの内容を確認して報告:
```powershell
Get-Content "F:\OpenClaw\x_monitor\accounts.json" | ConvertFrom-Json | Where-Object { $_.enabled -eq $true } | Select-Object handle, priority, category, max_daily_replies
```

---

### 🔄 アカウント有効/無効切り替え

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" toggle-account "@handle"
```

---

### 🚫 除外キーワード追加

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" add-keyword "@handle" "除外したいキーワード"
```

---

### 🚀 システム起動（Task Scheduler登録）

```powershell
# 管理者権限でセットアップスクリプトを実行
PowerShell -ExecutionPolicy Bypass -File "F:\OpenClaw\x_monitor\setup.ps1"
```

venvが存在しない場合はまず環境構築:
```powershell
cd F:\OpenClaw\x_monitor
python -m venv F:\OpenClaw\venv
& "F:\OpenClaw\venv\Scripts\pip.exe" install -r requirements.txt
& "F:\OpenClaw\venv\Scripts\playwright.exe" install chromium
```

---

### 🛑 システム停止

```powershell
# タスクを無効化（削除ではなく無効化）
Disable-ScheduledTask -TaskName "OpenClaw_XMonitor_Poll" -ErrorAction SilentlyContinue
Disable-ScheduledTask -TaskName "OpenClaw_XMonitor_Sender" -ErrorAction SilentlyContinue
Disable-ScheduledTask -TaskName "OpenClaw_XMonitor_Cancel" -ErrorAction SilentlyContinue
Write-Host "✅ X自動リプライ監視を停止しました"
```

再起動:
```powershell
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Poll"
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Sender"
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Cancel"
```

---

### 📊 詳細統計・ログ確認

```powershell
# 日別送信数
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 30

# 最新pollログ
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content -Tail 50

# 最新senderログ
Get-ChildItem "F:\OpenClaw\x_monitor\logs\sender_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content -Tail 30

# クラッシュログ
if (Test-Path "F:\OpenClaw\x_monitor\logs\crash.log") {
    Get-Content "F:\OpenClaw\x_monitor\logs\crash.log" -Tail 20
}
```

---

### ⚙️ Discord Webhook設定

config.jsonのdiscord_webhook_urlを更新:

```powershell
$config = Get-Content "F:\OpenClaw\x_monitor\config.json" | ConvertFrom-Json
$config.notification.discord_webhook_url = "WEBHOOK_URL_HERE"
$config | ConvertTo-Json -Depth 10 | Set-Content "F:\OpenClaw\x_monitor\config.json" -Encoding UTF8
```

---

### 🔑 APIキー設定

```powershell
# .envファイルにOpenRouter APIキーを設定
$envPath = "F:\OpenClaw\x_monitor\.env"
"OPENROUTER_API_KEY=sk-xxxxxxxx" | Set-Content $envPath -Encoding UTF8
```

---

## エラー対応フロー

| エラー | 対処 |
|--------|------|
| `auth_failed` | `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json` のCookieを更新 |
| `GENERATING`で詰まる | DBで手動リカバリ: `UPDATE detected_tweets SET status='FAILED' WHERE status='GENERATING'` |
| Task未登録 | `setup.ps1` を再実行 |
| OpenRouter APIエラー | `.env`のAPIキーを確認、残高チェック |

## 完了報告フォーマット

操作完了後は必ず以下を返すこと:
```
✅ [操作名] 完了 YYYY-MM-DD HH:MM
- 対象: @handle（追加操作の場合）
- 結果: [詳細]
- 次のアクション: [必要な場合のみ]
```
