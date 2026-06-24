---
name: system-sanity-check-weekly
model: lmstudio/nvidia/nemotron-3-nano-4b
description: 毎週金曜23:00 JST - 全コンポーネント（Cookie/ファイル/MCP/スケジューラー）E2E自動テスト
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

# system-sanity-check-weekly
# 実行時刻: 毎週金曜23:00 JST
# 目的: OpenClawシステム全コンポーネントの健全性をE2E自動テストし、週末前に障害を早期発見する

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## テスト結果の記録先

`C:\Users\sawas\.openclaw\workspace\memory\sanity-check-log.md` を読み込む（なければ作成）。

新規作成テンプレート:
```markdown
# システム健全性チェックログ

> system-sanity-check-weekly（毎週金曜）が自動更新する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## チェック記録

| 日付 | 総テスト数 | PASS | FAIL | 総合判定 |
|------|---------|------|------|--------|
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-01: スケジューラー健全性

`C:\Users\sawas\.openclaw\cron\jobs.json` を Read して取得する（正本ファイル）。

**PASS条件**:
- jobs.json が読み取り可能でパースできる
- enabled=true のジョブが10件以上存在する
- `C:\Users\sawas\.openclaw\state\openclaw.sqlite` の `cron_jobs` テーブルで next_run_at_ms が現在時刻より1時間以上過去になっているジョブ（スタック疑い）が0件

**FAIL時**: alerts.md に `🔴 HIGH | スケジューラー異常 | [詳細]` を記録

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

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

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

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

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-04: Cookie有効性推定

x-cookie-health-check の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が7日以内

**FAIL時**: 
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | Cookie確認未実施 | x-cookie-health-checkが[N]日未実行 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-05: メモリファイル読み取り確認

`C:\Users\sawas\.openclaw\workspace\memory\` ディレクトリ内の主要ファイル（`learnings.md`, `growth-metrics.md` 等）を Read して読み取り可能か確認する。

**PASS条件**: メモリディレクトリ内のファイルが読み取り可能でエラーなし

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | メモリファイル読み取り失敗 | workspace/memory/ へのアクセスに問題あり | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-06: バックアップ確認

`kura-backup` の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が25時間以内（毎日実行のため）

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🟡 MEDIUM | バックアップ未実行 | kura-backupが[N]時間未実行 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-07: capability-evolver-daily 実行確認

`capability-evolver-daily` の lastRunAt を確認する（`C:\Users\sawas\.openclaw\state\openclaw.sqlite` を直接Readして取得）。

**PASS条件**: lastRunAt が25時間以内

**FAIL時**:
```
| YYYY-MM-DD 23:00 | 🔴 HIGH | 自己改善ループ停止 | capability-evolver-dailyが[N]時間未実行 — 自律サイクル断絶 | 未解決 |
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

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

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 完了条件
- [ ] Test-01〜07 全実行済み
- [ ] Test-M01: モデルID健全性チェック実行済み
- [ ] Test-D01: ドキュメント整合性チェック実行済み（自動修正含む）
- [ ] sanity-check-log.md 更新済み
- [ ] 失敗テストがあればalerts.md記録済み
- [ ] learnings.md 記録済み


---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

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

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Test-D01: ドキュメント整合性チェック（自動修正）

目的: `cron/jobs.json` を正本として、OpenClaw基本動作に必要な全設定・文書ファイルの記述を自動照合・修正する

### Step 1: 正本情報の取得

`C:\Users\sawas\.openclaw\cron\jobs.json` を Read する。  
enabled=true の全ジョブについて **name** と **cronExpression** を抽出し、時刻を導出する（例: `"10 7 * * *"` → 07:10）。

### Step 2: チェック対象ファイルを Read する

以下を全て Read する（存在しないファイルはスキップしてFAIL記録）:

**ワークスペース文書（整合性チェック対象）:**
- `C:\Users\sawas\.openclaw\workspace\AGENTS.md`
- `C:\Users\sawas\.openclaw\workspace\SOUL.md`
- `C:\Users\sawas\.openclaw\workspace\HEARTBEAT.md`
- `C:\Users\sawas\.openclaw\workspace\TOOLS.md`
- `C:\Users\sawas\.openclaw\workspace\CONDUCTOR.md`
- `C:\Users\sawas\.openclaw\workspace\HEALTH-CHECK.md`
- `C:\Users\sawas\.openclaw\workspace\USER.md`
- `C:\Users\sawas\.openclaw\workspace\IDENTITY.md`
- `C:\Users\sawas\.openclaw\workspace\DREAMS.md`（存在する場合のみ）

**設定ファイル（存在確認のみ）:**
- `C:\Users\sawas\.openclaw\openclaw.json`
- `C:\Users\sawas\.openclaw\config.yml`
- `C:\Users\sawas\.openclaw\.env`
- `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json`
- `C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.js`

**メモリファイル（存在確認＋ログ汚染チェック）:**
- `C:\Users\sawas\.openclaw\workspace\memory\anti-recurrence-rules.md`
- `C:\Users\sawas\.openclaw\workspace\memory\failures.md`
- `C:\Users\sawas\.openclaw\workspace\memory\learnings.md`
- `C:\Users\sawas\.openclaw\workspace\memory\improvement-proposals.md`
- `C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md`

**スケジュールスキル（Preflight＋パス確認）:**
- `C:\Users\sawas\.openclaw\scheduled\` 配下の全 SKILL.md ファイル（`x-post-*` / `x-dm-*` / `x-auto-*` / `viral-amplifier-*` / `daily-note-post` / `note-weekly-post` など X投稿・運用系）

### Step 3: 自動検出・修正チェックリスト

Read した各ファイルに対して以下を順番に確認し、問題があればEdit toolで即修正する:

**D-1: 廃止参照の検出・修正**
| 検出パターン | 正しい値 | 対象ファイル |
|---|---|---|
| `jobs.json.migrated.*` | `jobs.json` | 全文書 |
| `x-twitter-cookies.json` | `x_auth_state.json` | 全文書 |
| `C:\Users\sawas\x_auth_state.json`（ルートパス） | `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json` | 全文書 |
| `.claude/scheduled_tasks.json` を「設定ファイル」として参照 | `cron/jobs.json` | 全文書 |
| `memory/cron-map.md` | `cron/jobs.json` | 全文書 |

**D-2: ログ汚染の検出・除去**  
各ファイルの末尾行を確認し、`YYYY-MM-DD HH:MM:SS - ` のパターンで始まる行（監視スクリプトの出力が混入したもの）があれば削除する。

**D-3: X投稿ジョブ時刻の整合チェック・修正**  
Step 1 で取得した jobs.json の実際の時刻と、各ワークスペース文書に記載されているジョブ時刻を比較する。  
不一致があれば Edit tool で文書側を修正する（jobs.json が常に正本）。

**D-4: X投稿系SKILL.md Preflight セクション確認**  
X投稿・運用系の各 SKILL.md に以下のセクションヘッダーが存在するか確認する:
```
## ⚡ Preflight: Playwright ロック確認
```
存在しないファイルはFAILリストに記録し、alerts.md に `🟡 MEDIUM | Preflight未設定 | [ファイル名]` を追記する。

**D-5: 設定ファイル存在確認**  
Step 2 の設定ファイル5件が全て存在するか確認する。  
存在しないファイルがあれば alerts.md に `🔴 HIGH | 必須ファイル不在 | [パス]` を記録する。

### Step 4: 修正結果をDiscordに報告

以下の形式で報告する:

```
🔍 [Test-D01] ドキュメント整合性チェック完了

修正済み: N件
  - [ファイル名]: [修正内容]
  ...

要確認(FAIL): N件
  - [内容]
  ...

問題なし: ✅ 全チェックPASS
```

修正が0件・FAIL0件の場合は `✅ Doc整合性: 異常なし` の1行のみでよい。

**FAIL時**: alerts.md に記録し、sanity-check-log.md の詳細欄に追記する。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 【2026-06-23 修正メモ】
- 旧 cron/jobs.json.migrated.5 参照を jobs.json に修正（Test-01）
- Test-01/04/06/07 の lastRunAt 確認は cron_jobs テーブルの next_run_at_ms を参照
- Python例: conn.execute("SELECT name,next_run_at_ms FROM cron_jobs WHERE name=?", (name,)).fetchone()

## 【2026-06-24 追加】
- Test-D01: ドキュメント整合性チェック追加（jobs.jsonを正本として全設定・文書ファイルを自動照合・修正）

