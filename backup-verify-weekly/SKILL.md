---
name: backup-verify-weekly
description: 毎週月曜05:00 JST - バックアップファイル整合性確認・kura-backupの実行確認
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# backup-verify-weekly
# 実行時刻: 毎週月曜05:00 JST（kura-backupの翌朝）
# 目的: kura-backupが正常に実行されたか、バックアップファイルが存在・読み取り可能かを自動検証し、データ損失リスクを排除する

---

## Step 1: kura-backup の実行確認

`C:\Users\sawas\.openclaw\cron\jobs.json.migrated.5` を直接Readして `kura-backup` タスクの情報を取得・確認する。

**確認項目**:
- `enabled`: true かどうか
- `lastRunAt`: 25時間以内に実行されているか（毎日00:00実行のため）

**FAIL条件**: lastRunAt が30時間以上前 または null

---

## Step 2: バックアップファイルの存在確認

kura-backup が実行するバックアップ先ディレクトリを確認する。

`C:\Users\sawas\.openclaw\` 配下のバックアップ関連ファイル・ディレクトリを確認:
- `backup/` ディレクトリが存在するか
- 最新バックアップファイルのタイムスタンプは昨日以降か
- バックアップサイズが0でないか

**代替確認**: バックアップの存在が確認できない場合は、workspace配下の主要ファイルが直接読み取れるかで代替確認する:
- growth-metrics.md が読み取れる → workspace自体は正常
- 最終更新日が最近である → データは存在している

---

## Step 3: 重要ファイルの最終更新確認

以下の主要ファイルの最終更新日時を確認し、適切に更新されているかチェックする:

| ファイル | 期待更新頻度 | 最終更新 | 判定 |
|---------|-----------|--------|------|
| growth-metrics.md | 毎日 | [日時] | ✅/⚠️ |
| learnings.md | 毎日 | [日時] | ✅/⚠️ |
| alerts.md | 随時 | [日時] | ✅/⚠️ |
| x-performance-log.md | 毎週火曜 | [日時] | ✅/⚠️ |
| anti-recurrence-rules.md | 変更時 | [日時] | ✅/⚠️ |

---

## Step 4: 結果集計と記録

### sanity-check-log.md への追記

`C:\Users\sawas\.openclaw\workspace\memory\sanity-check-log.md` を読む（system-sanity-check-weeklyが作成したファイル）。

```
## バックアップ検証 YYYY-MM-DD

| チェック項目 | 結果 | 詳細 |
|-----------|------|------|
| kura-backup実行確認 | ✅ PASS / ❌ FAIL | lastRunAt: [値] |
| バックアップファイル存在 | ✅ PASS / ❌ FAIL | [詳細] |
| 主要ファイル最終更新 | ✅ PASS / ⚠️ 注意 | [古いファイルがあれば列挙] |
| 総合判定 | ✅ 正常 / ⚠️ 要確認 / 🔴 異常 | - |
```

### alerts.md への通知

全PASS:
```
| YYYY-MM-DD 05:00 | 🔵 INFO | バックアップ検証PASS | kura-backup正常実行・主要ファイル正常 | 解決済み |
```

バックアップ未実行:
```
| YYYY-MM-DD 05:00 | 🔴 HIGH | バックアップ未実行 | kura-backupが[N]時間未実行 — データ損失リスクあり | 未解決 |
```

ファイル更新が古い:
```
| YYYY-MM-DD 05:00 | 🟡 MEDIUM | ファイル更新停滞 | [ファイル名]が[N]日間未更新 — 自動タスクの停止を確認 | 未解決 |
```

### learnings.md への記録
```
- [BACKUP-VERIFY] YYYY-MM-DD バックアップ検証: [PASS/FAIL] — [特記事項]
```

---

## 完了条件
- [ ] kura-backup の実行状況確認済み
- [ ] バックアップファイル存在確認済み
- [ ] 主要ファイル最終更新確認済み
- [ ] sanity-check-log.md 記録済み
- [ ] alerts.md 通知済み

