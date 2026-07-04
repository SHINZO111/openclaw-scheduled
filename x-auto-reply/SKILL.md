---
name: x-auto-reply
description: |
  X（Twitter）自動リプライ監視システムの管理スキル。
  @KURAOpenclaw アカウントの指定ユーザーの投稿を自動検知し、AIでリプライ文を生成・送信する。
  以下のフレーズで起動する：
  - 「X自動リプライを設定して」「リプライ監視を追加して @handle」
  - 「X自動リプライのステータス確認」「リプライ統計を見せて」「X監視を起動/停止して」
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取りは不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## ⚡ Preflight: ロック確認（最優先）

1. Read で `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. ファイルが存在し `ts` が現在時刻から600000ms（10分）以内 → Discord に「⚡ 別ジョブ実行中のためスキップ」と報告して即終了
3. ファイルなし or 10分超過 → 続行

---

## システム構成

| 要素 | パス |
|------|------|
| ベースDir | `F:\OpenClaw\x_monitor\` |
| Python | `F:\OpenClaw\venv\Scripts\python.exe` |
| DB | `F:\OpenClaw\x_monitor\monitor.db` |
| 設定 | `F:\OpenClaw\x_monitor\config.json` |
| アカウント | `F:\OpenClaw\x_monitor\accounts.json` |
| ログ | `F:\OpenClaw\x_monitor\logs\` |
| Cookie | `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json` |

| タスク名 | 役割 | 間隔 |
|---------|------|------|
| `OpenClaw_XMonitor_Poll` | TLスクレイプ→AI生成→待機キュー投入 | 5分 |
| `OpenClaw_XMonitor_Sender` | 待機中リプライを送信 | 30秒 |
| `OpenClaw_XMonitor_Cancel` | キャンセルサーバー（Flask localhost:19876） | 常駐 |

---

## コマンド別手順

### 🟢 ステータス確認

```powershell
@("OpenClaw_XMonitor_Poll","OpenClaw_XMonitor_Sender","OpenClaw_XMonitor_Cancel") | ForEach-Object {
    $t = Get-ScheduledTask -TaskName $_ -ErrorAction SilentlyContinue
    if ($t) { "$_ : $($t.State)" } else { "$_ : 未登録" }
}
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 7
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" | Sort-Object LastWriteTime -Desc | Select -First 1 | Get-Content -Tail 20
```

報告形式:
```
✅ X自動リプライ ステータス YYYY-MM-DD
- Poll/Sender/CancelServer: [Running/Ready/未登録]
- 直近7日 送信: N件 / 生成: N件 / 最終エラー: [なし/内容]
```

### ➕ 監視アカウント追加

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" `
    add-account "@handle" --priority NORMAL --category general --max-daily 3
# priority: HIGH（フォロワー10万超 or 重要）/ NORMAL
# category: ai / tech / business / general
Get-Content "F:\OpenClaw\x_monitor\accounts.json" | ConvertFrom-Json | Where-Object { $_.enabled -eq $true } | Select handle, priority, category, max_daily_replies
```

### 🔄 有効/無効 切り替え

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" toggle-account "@handle"
```

### 🚫 除外キーワード追加

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" add-keyword "@handle" "キーワード"
```

### 🚀 起動 / 🛑 停止

```powershell
# 起動
PowerShell -ExecutionPolicy Bypass -File "F:\OpenClaw\x_monitor\setup.ps1"

# 停止
Disable-ScheduledTask -TaskName "OpenClaw_XMonitor_Poll","OpenClaw_XMonitor_Sender","OpenClaw_XMonitor_Cancel"

# 再開
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Poll","OpenClaw_XMonitor_Sender","OpenClaw_XMonitor_Cancel"
```

### 📊 詳細ログ確認

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 30
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" | Sort-Object LastWriteTime -Desc | Select -First 1 | Get-Content -Tail 50
Get-ChildItem "F:\OpenClaw\x_monitor\logs\sender_*.log" | Sort-Object LastWriteTime -Desc | Select -First 1 | Get-Content -Tail 30
```

### ⚙️ 各種設定

```powershell
# Discord Webhook
$c = Get-Content "F:\OpenClaw\x_monitor\config.json" | ConvertFrom-Json
$c.notification.discord_webhook_url = "WEBHOOK_URL_HERE"
$c | ConvertTo-Json -Depth 10 | Set-Content "F:\OpenClaw\x_monitor\config.json" -Encoding UTF8

# OpenRouter APIキー
"OPENROUTER_API_KEY=sk-xxxxxxxx" | Set-Content "F:\OpenClaw\x_monitor\.env" -Encoding UTF8
```

---

## エラー対応

| エラー | 対処 |
|--------|------|
| `auth_failed` | `x_auth_state.json` のCookieを更新 |
| `GENERATING`で詰まる | `UPDATE detected_tweets SET status='FAILED' WHERE status='GENERATING'` |
| Task未登録 | `setup.ps1` を再実行 |
| OpenRouter APIエラー | `.env`のAPIキーを確認・残高チェック |

## 完了報告

```
✅ [操作名] 完了 YYYY-MM-DD HH:MM
- 対象: @handle（追加操作の場合）/ 結果: [詳細] / 次のアクション: [必要な場合のみ]
```