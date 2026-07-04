---
name: openclaw-cleanup-biweekly
model: lmstudio/nvidia/nemotron-3-nano-4b
description: 2週間に1回（毎月1日・15日 03:00 JST）— .openclaw/ 定期整理整頓
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

> ⛔ **[SYSTEM CONSTRAINT]**: cronツールは絶対使用禁止。エラーが発生した場合はDiscordで報告して終了する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
# openclaw-cleanup-biweekly
# 実行時刻: 毎月1日・15日 03:00 JST
# 目的: C:\Users\sawas\.openclaw\ の定期整理整頓（ゴミファイル削除・バックアップ世代管理・workspace/temp清掃）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 1: logs/ ゼロバイトファイル削除

```powershell
$removed = Get-ChildItem "C:\Users\sawas\.openclaw\logs" -File |
  Where-Object { $_.Length -eq 0 } |
  ForEach-Object { Remove-Item $_.FullName -Force; $_.Name }
Write-Host "Deleted zero-byte logs: $($removed.Count)"
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 2: openclaw.json バックアップ世代管理（ルート直下）

ルート直下の `openclaw.json.bak*` を確認し、4本を超えていたら古いものを `archive/openclaw-backups/` に移動する。

```powershell
$root = "C:\Users\sawas\.openclaw"
$bakDir = "$root\archive\openclaw-backups"
if (-not (Test-Path $bakDir)) { New-Item -ItemType Directory $bakDir -Force | Out-Null }

# 残す: openclaw.json, openclaw.json.last-good は除外
# bak系をLastWriteTime降順で取得し、5本目以降をアーカイブ
$baks = Get-ChildItem $root -File |
  Where-Object { $_.Name -match "^openclaw\.json\.(bak|clobbered)" } |
  Sort-Object LastWriteTime -Descending

if ($baks.Count -gt 4) {
  $baks | Select-Object -Skip 4 | ForEach-Object {
    Move-Item $_.FullName $bakDir -Force
    Write-Host "Archived: $($_.Name)"
  }
} else {
  Write-Host "openclaw.json baks: $($baks.Count) (上限以内、処理不要)"
}
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 3: workspace/ ルート直下の一時ファイル清掃

workspace/ 直下に以下の条件に当てはまるファイルがあれば `workspace/temp/` に移動する:

```powershell
$ws = "C:\Users\sawas\.openclaw\workspace"
if (-not (Test-Path "$ws\temp")) { New-Item -ItemType Directory "$ws\temp" -Force | Out-Null }

$moved = Get-ChildItem $ws -File |
  Where-Object {
    # 14日以上更新されていない temp/tmp/check_/fix_ 系ファイル
    ($_.Name -match "^(temp|tmp|check_|fix_)") -and
    ($_.LastWriteTime -lt (Get-Date).AddDays(-14))
  } |
  ForEach-Object {
    Move-Item $_.FullName "$ws\temp\" -Force
    $_.Name
  }
Write-Host "Moved to workspace/temp: $($moved.Count) files"
if ($moved.Count -gt 0) { $moved | ForEach-Object { Write-Host "  - $_" } }
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 4: workspace/temp/ の古いファイル削除

`workspace/temp/` に30日以上放置されたファイルを削除する。

```powershell
$tempDir = "C:\Users\sawas\.openclaw\workspace\temp"
$deleted = Get-ChildItem $tempDir -File |
  Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
  ForEach-Object { Remove-Item $_.FullName -Force; $_.Name }
Write-Host "Deleted old temp files: $($deleted.Count)"
if ($deleted.Count -gt 0) { $deleted | ForEach-Object { Write-Host "  - $_" } }
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 5: ルート直下の孤立ファイル検出（削除はしない・報告のみ）

ルート直下に以下のパターンで新たに増えたファイルがあれば報告する（自動削除はしない）。

```powershell
$root = "C:\Users\sawas\.openclaw"
$suspects = Get-ChildItem $root -File |
  Where-Object {
    $_.Name -match "\.(bak|tmp|log)$" -and
    $_.Name -notmatch "^openclaw\.json\.(bak|last-good)" -and
    $_.Name -notmatch "^update-check"
  }
if ($suspects.Count -gt 0) {
  Write-Host "⚠️ ルート直下の孤立ファイル（手動確認推奨）:"
  $suspects | ForEach-Object { Write-Host "  - $($_.Name) ($([math]::Round($_.Length/1KB,1))KB, $($_.LastWriteTime.ToString('yyyy/MM/dd')))" }
} else {
  Write-Host "✅ ルート直下: 孤立ファイルなし"
}
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Step 6: 実行ログ記録

`C:\Users\sawas\.openclaw\logs\cleanup-biweekly.log` に追記:

```powershell
$logLine = "$(Get-Date -Format 'yyyy-MM-dd HH:mm') | cleanup-biweekly | 完了 | logs削除:Step1 / bak整理:Step2 / temp整理:Step3-4"
Add-Content "C:\Users\sawas\.openclaw\logs\cleanup-biweekly.log" $logLine
Write-Host $logLine
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了条件
- [ ] logs/ のゼロバイトファイル削除完了
- [ ] openclaw.json バックアップが4本以下に整理済み
- [ ] workspace/temp/ への移動完了（または対象なし）
- [ ] workspace/temp/ の30日超ファイル削除完了
- [ ] ルート直下の孤立ファイル報告完了
- [ ] ログ記録完了
