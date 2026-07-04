---
name: openclaw-cleanup-biweekly
description: 2週間に1回（毎月1日・15日 03:00 JST）— .openclaw/ 定期整理整頓
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取りは不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## Step 1: logs/ ゼロバイトファイル削除

```powershell
$removed = Get-ChildItem "C:\Users\sawas\.openclaw\logs" -File |
  Where-Object { $_.Length -eq 0 } |
  ForEach-Object { Remove-Item $_.FullName -Force; $_.Name }
Write-Host "Deleted zero-byte logs: $($removed.Count)"
```

## Step 2: openclaw.json バックアップ世代管理（4本超を archive/ へ）

```powershell
$root = "C:\Users\sawas\.openclaw"
$bakDir = "$root\archive\openclaw-backups"
if (-not (Test-Path $bakDir)) { New-Item -ItemType Directory $bakDir -Force | Out-Null }

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

## Step 3: workspace/ 一時ファイル清掃（14日以上の temp/tmp/check_/fix_ 系を workspace/temp/ へ）

```powershell
$ws = "C:\Users\sawas\.openclaw\workspace"
if (-not (Test-Path "$ws\temp")) { New-Item -ItemType Directory "$ws\temp" -Force | Out-Null }

$moved = Get-ChildItem $ws -File |
  Where-Object {
    ($_.Name -match "^(temp|tmp|check_|fix_)") -and
    ($_.LastWriteTime -lt (Get-Date).AddDays(-14))
  } |
  ForEach-Object { Move-Item $_.FullName "$ws\temp\" -Force; $_.Name }
Write-Host "Moved to workspace/temp: $($moved.Count) files"
```

## Step 4: workspace/temp/ の30日超ファイル削除

```powershell
$deleted = Get-ChildItem "C:\Users\sawas\.openclaw\workspace\temp" -File |
  Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
  ForEach-Object { Remove-Item $_.FullName -Force; $_.Name }
Write-Host "Deleted old temp files: $($deleted.Count)"
```

## Step 5: ルート直下の孤立ファイル検出（報告のみ・削除しない）

```powershell
$suspects = Get-ChildItem "C:\Users\sawas\.openclaw" -File |
  Where-Object {
    $_.Name -match "\.(bak|tmp|log)$" -and
    $_.Name -notmatch "^openclaw\.json\.(bak|last-good)" -and
    $_.Name -notmatch "^update-check"
  }
if ($suspects.Count -gt 0) {
  Write-Host "⚠️ ルート直下の孤立ファイル（手動確認推奨）:"
  $suspects | ForEach-Object { Write-Host "  - $($_.Name) ($([math]::Round($_.Length/1KB,1))KB, $($_.LastWriteTime.ToString('yyyy/MM/dd')))" }
} else { Write-Host "✅ ルート直下: 孤立ファイルなし" }
```

## Step 6: 実行ログ記録

```powershell
$logLine = "$(Get-Date -Format 'yyyy-MM-dd HH:mm') | cleanup-biweekly | 完了"
Add-Content "C:\Users\sawas\.openclaw\logs\cleanup-biweekly.log" $logLine
Write-Host $logLine
```

---

## 完了条件
- [ ] logs/ ゼロバイトファイル削除
- [ ] openclaw.json bak が4本以下に整理
- [ ] workspace/temp/ への移動完了（または対象なし）
- [ ] workspace/temp/ の30日超ファイル削除
- [ ] ルート直下の孤立ファイル報告
- [ ] ログ記録完了