---
name: x-reply-watchdog
description: |
  X自動リプライシステムのウォッチドッグ。
  Task Schedulerタスクの死活監視・自動復旧・日次サマリーを行う。
  以下のフレーズで起動する：
  - 「X自動リプライのジョブを実行して」
  - 「リプライシステムを起動して」
  - 「X監視ジョブのヘルスチェック」
  - 「自動リプライが動いているか確認して」
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。

> ⛔ **[SYSTEM CONSTRAINT]**: cronツールは絶対使用禁止。エラーが発生した場合はDiscordで報告して終了する。

---

# X 自動リプライ ウォッチドッグ

## システム定数

```
PYTHON   = F:\OpenClaw\venv\Scripts\python.exe
SCRIPTS  = F:\OpenClaw\x_monitor\scripts
SETUP    = F:\OpenClaw\x_monitor\setup.ps1
TASKS    = OpenClaw_XMonitor_Poll, OpenClaw_XMonitor_Sender, OpenClaw_XMonitor_Cancel
```

---

## Step 1: Task Scheduler 死活確認

以下のPowerShellを実行して各タスクの状態を取得する:

```powershell
$tasks = @("OpenClaw_XMonitor_Poll","OpenClaw_XMonitor_Sender","OpenClaw_XMonitor_Cancel")
$result = $tasks | ForEach-Object {
    $t = Get-ScheduledTask -TaskName $_ -ErrorAction SilentlyContinue
    if ($t) {
        [PSCustomObject]@{ Name=$_; State=$t.State; LastRun=(Get-ScheduledTaskInfo -TaskName $_).LastRunTime; LastResult=(Get-ScheduledTaskInfo -TaskName $_).LastTaskResult }
    } else {
        [PSCustomObject]@{ Name=$_; State="未登録"; LastRun=$null; LastResult=$null }
    }
}
$result | Format-Table -AutoSize
```

判定基準:
- `Ready` または `Running` → 正常
- `Disabled` → 要再有効化
- `未登録` → 要セットアップ
- `LastTaskResult` が `0` 以外 → 直前実行でエラー

---

## Step 2: 異常があれば自動復旧

### 2a. タスクが「未登録」の場合
```powershell
& "F:\OpenClaw\x_monitor\setup.ps1"
```
実行後、再度 Step 1 のコマンドで登録を確認する。

### 2b. タスクが「Disabled」の場合
```powershell
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Poll"
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Sender"
Enable-ScheduledTask -TaskName "OpenClaw_XMonitor_Cancel"
```

### 2c. LastTaskResult が 0xFFFF（一般エラー）の場合
最新ログを確認して原因を特定する:
```powershell
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" |
    Sort-Object LastWriteTime -Desc |
    Select-Object -First 1 |
    Get-Content -Tail 30
```

---

## Step 3: 直近の実行統計を確認

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 1
```

取得できない場合はスキップして Step 4 へ進む。

---

## Step 4: 手動ポーリング（オプション）

ユーザーから「今すぐポーリングを実行して」と指示があった場合のみ実行:

```powershell
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\poll.py"
```

通常のウォッチドッグ実行では **実行しない**（Task Schedulerに委ねる）。

---

## Step 5: 完了報告

以下のフォーマットで報告する:

```
✅ X自動リプライ ウォッチドッグ YYYY-MM-DD HH:MM

【タスク状態】
- Poll (5分間隔):   [Ready / Running / Disabled / 未登録]
- Sender (1分間隔): [Ready / Running / Disabled / 未登録]
- CancelServer:     [Ready / Running / Disabled / 未登録]

【直近24h実績】
- 検知ツイート: N件
- 生成成功:     N件
- 送信完了:     N件
- エラー:       N件

【対処】
- [異常があれば実施した対処を記載 / なければ「異常なし」]
```

---

## エラー別対処テーブル

| エラー | 原因 | 対処 |
|--------|------|------|
| `auth_failed` in logs | Xセッション切れ | `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json` を更新するようユーザーに通知 |
| `GENERATING` 孤立行が多数 | poll.pyクラッシュ後の残骸 | `UPDATE detected_tweets SET status='FAILED' WHERE status='GENERATING'` をSQLiteで実行 |
| Task未登録 | setup.ps1未実行 or 再起動後 | `setup.ps1` を再実行 |
| OpenRouter 429 | APIレート超過 | 15分待機を推奨、ユーザーにOpenRouterダッシュボード確認を依頼 |
| `tweetButton still present` | X UI変更 / レートリミット | `dom_health.py` を実行してセレクタ確認: `& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\dom_health.py"` |
