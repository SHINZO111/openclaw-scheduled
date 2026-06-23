---
name: system-sanity-check-weekly
description: 毎週金曜23:00 JST - 全コンポーネント（Cookie/ファイル/MCP/スケジューラー）E2E自動テスト
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# system-sanity-check-weekly
# 実行時刻: 毎週金曜23:00 JST
# 目的: OpenClawシステム全コンポーネントの健全性をE2E自動テストし、週末前に障害を早期発見する

---

## テスト結果の記録先

`C:\Users\sawas\.openclaw\workspace\memory\sanity-check-log.md` を読み込む（なければ作成）。

新規作成テンプレート:
```markdown
# システム健全性チェックログ

> system-sanity-check-weekly（毎週金曜）が自動更新する。

---

## チェック記録

| 日付 | 総テスト数 | PASS | FAIL | 総合判定 |
|------|---------|------|------|--------|
```

---

## Test-01: スケジューラー健全性

`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得する。

**PASS条件**:
- jobs.json.migrated.5 が読み取り可能でパースできる
- enabled=true のジョブが10件以上存在する
- nextRunAt が過去になっているジョブ（スタック）が0件

**FAIL時**: alerts.md に `🔴 HIGH | スケジューラー異常 | [詳細]` を記録

---

## Test-02: 主要ファイルの読み取り可能性

以下のファイルを順番に読み込み、空でないことを確認する:
- `C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md`
- `C:\Users\sawas\.openclaw\workspace\memory\learnings.md`
- `C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md`
- `C:\Users\sawas\.openclaw\workspace\memory\alerts.md`
- `C:\Users\sawas\.openclaw\workspace\memory\failures.md`
- `C:\Users\sawas\.openclaw\.env`

**PASS条件**: 全ファイルが読み取り可能で0行より多い

**FAIL時**: どのファイルが読み取れないかを特定してアラート

---

## Test-03: X投稿インフラ確認

`C:\Users\sawas\.openclaw\.env` を読む。

**PASS条件**:
- `AUTH_TOKEN` が設定されている（空でない）
- `CT0` が設定されている（空でない）
- `C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.js` が存在する（ファイルが読み取れる）

**FAIL時**: 
```
| YYYY-MM-DD 23:00 | 🔴 HIGH | X投稿インフラ異常 | Cookie/post-to-x.jsに問題あり — 即時確認推奨 | 未解決 |
```

---

## Test-04: Cookie有効性推定

x-cookie-health-check の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が7日以内

**FAIL時**: 
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | Cookie確認未実施 | x-cookie-health-checkが[N]日未実行 | 未解決 |
```

---

## Test-05: メモリファイル読み取り確認

`C:\Users\sawas\.openclaw\workspace\memory\` ディレクトリ内の主要ファイル（`learnings.md`, `growth-metrics.md` 等）を Read して読み取り可能か確認する。

**PASS条件**: メモリディレクトリ内のファイルが読み取り可能でエラーなし

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | メモリファイル読み取り失敗 | workspace/memory/ へのアクセスに問題あり | 未解決 |
```

---

## Test-06: バックアップ確認

`kura-backup` の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が25時間以内（毎日実行のため）

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | バックアップ未実行 | kura-backupが[N]時間未実行 | 未解決 |
```

---

## Test-07: capability-evolver-daily 実行確認

`capability-evolver-daily` の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が25時間以内

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🔴 HIGH | 自己改善ループ停止 | capability-evolver-dailyが[N]時間未実行 — 自律サイクル断絶 | 未解決 |
```

---

## Step 最終: 結果の集計・記録

### sanity-check-log.md への追記
```
| YYYY-MM-DD | 7 | [PASS数] | [FAIL数] | ✅ 正常 / ⚠️ 要確認 / 🔴 異常 |

### 詳細
| テスト | 結果 | メモ |
|-------|------|------|
| Test-01: スケジューラー | ✅ PASS | タスク[N]件すべて正常 |
| Test-02: ファイル読み取り | ✅ PASS | 全6ファイル正常 |
...
```

### learnings.md への記録

本日セクションに追記:
```
- [SANITY-CHECK] YYYY-MM-DD 週次E2Eテスト: [PASS N/7] — [特記事項]
```

### 全テストPASSの場合
alerts.md に:
```
| YYYY-MM-DD 23:00 | 🔵 INFO | 週次テスト全PASS | 全7テスト正常 — システム健全 | 解決済み |
```

---

## 完了条件
- [ ] Test-01〜07 全実行済み
- [ ] sanity-check-log.md 更新済み
- [ ] 失敗テストがあればalerts.md記録済み
- [ ] learnings.md 記録済み


---

## Test-M01: モデルID健全性チェック（モデルチェーン変更後追加 2026-06-22）

目的: フォールバックチェーン内の廃止済みモデルIDを週次で自動検出する

以下をexecで実行せよ：

```powershell
$cacheFile = 'C:\Users\sawas\.openclaw\cache\openrouter-models.json'
$configFile = 'C:\Users\sawas\.openclaw\openclaw.json'
if (-not (Test-Path $cacheFile)) { Write-Host 'SKIP: cache not found'; exit 0 }
$validIds = (Get-Content $cacheFile -Raw | ConvertFrom-Json).data | Select-Object -ExpandProperty id
$config = Get-Content $configFile -Raw | ConvertFrom-Json
$fallbacks = $config.agents.defaults.model.fallbacks
$localPrefixes = @('lmstudio/', 'zai/', 'openrouter/free', 'openrouter/auto', 'openrouter/owl-alpha')
$invalid = $fallbacks | Where-Object {
    $f = $_
    $isLocal = $localPrefixes | Where-Object { $f -like "$_*" }
    if ($isLocal) { return $false }
    $modelId = $f -replace '^openrouter/', ''
    return $validIds -notcontains $modelId
}
if ($invalid) {
    Write-Host 'FAIL: 廃止済みモデルID検出:'
    $invalid | ForEach-Object { Write-Host "  - $_" }
    exit 1
} else { Write-Host 'PASS: 全モデルID有効' }
```

**PASS**: 何もしない
**FAIL**:
1. `alerts.md` に `🔴 HIGH | 廃止済みモデルID検出 | [IDリスト] — openclaw.jsonのfallbacksから除去せよ` を記録
2. openclaw.jsonのfallbacksから該当IDを除去し、JSONをバリデートせよ



---
## 【2026-06-23 修正メモ】
- 旧 cron/jobs.json.migrated.5 参照をSQLite（openclaw.sqlite）に修正済み
- Test-01/04/06/07のlastRunAt確認は cron_jobs テーブルの next_run_at_ms を参照
- Python例: conn.execute("SELECT name,next_run_at_ms FROM cron_jobs WHERE name=?", (name,)).fetchone()

