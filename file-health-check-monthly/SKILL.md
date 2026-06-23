---
name: file-health-check-monthly
description: 毎月20日02:00 JST - メモリファイル肥大化監視・500行超をarchiveに自動移管
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**


# file-health-check-monthly
# 実行時刻: 毎月20日 02:00 JST
# 目的: memory/ディレクトリのファイルが肥大化していないか監視し、500行超のファイルをarchiveに移管してシステムの応答速度を維持する

---

## Step 1: ファイルサイズ計測

以下のファイルを順番に読み込み、行数を計測する:

計測対象ファイル（`C:\Users\sawas\.openclaw\workspace\memory\` 配下）:
- anti-recurrence-rules.md
- learnings.md
- failures.md
- growth-metrics.md
- alerts.md
- x-performance-log.md
- revenue-ideas.md
- weekly-trends.md
- soul-evolution-proposals.md
- knowledge-synthesis-log.md
- benchmark-log.md
- competitors.md（存在する場合）
- pon-shinzo-setup-guide.md（存在する場合）

計測結果を以下の形式でまとめる:
```
| ファイル名 | 行数 | 状態 |
|----------|------|------|
| anti-recurrence-rules.md | [N] | 🟢 正常 / 🟡 注意(300-499) / 🔴 要アーカイブ(500+) |
...
```

---

## Step 2: 500行超ファイルのアーカイブ処理

500行以上のファイルが存在する場合、以下を実行する:

### 2-A: archiveディレクトリの確認

`C:\Users\sawas\.openclaw\workspace\memory\archive\YYYY\` ディレクトリが存在しない場合は作成する（YYYYは当年）。

### 2-B: 古いエントリをアーカイブ

例: `learnings.md` が600行の場合
- 最古の200行（おおよそ過去3ヶ月分）を `archive\2026\learnings-2026-01_to_03.md` として保存
- 元の `learnings.md` から移動した200行を削除し、上部に参照コメントを追加:
  ```
  <!-- アーカイブ: archive/2026/learnings-2026-01_to_03.md (200行) を参照 -->
  ```

### 2-C: アーカイブ対象の判断基準

| ファイル | アーカイブ対象 |
|---------|-------------|
| learnings.md | 3ヶ月以上前の## YYYY-MM-DD セクション |
| failures.md | 6ヶ月以上前の## YYYY-MM-DD セクション |
| alerts.md | 「解決済み」かつ90日以上前のエントリ |
| x-performance-log.md | 3ヶ月以上前の週次データ |
| anti-recurrence-rules.md | 【アーカイブ禁止】全ルールは永続保持 |
| growth-metrics.md | 【アーカイブ禁止】集計値は永続保持 |

---

## Step 3: 300-499行（注意ゾーン）のファイル管理

300行以上のファイルについて:
- 今後1ヶ月でアーカイブが必要になる可能性を判定
- 不要なセクション（テンプレート部分、空白行の連続）を削減する

---

## Step 4: ファイル健全性レポートの作成

`C:\Users\sawas\.openclaw\workspace\memory\growth-metrics.md` の月次記録に追記:

```
## ファイル健全性チェック YYYY-MM-DD
| ファイル | 処置前行数 | 処置後行数 | アクション |
|---------|---------|---------|---------|
| [ファイル名] | [N] | [M] | アーカイブ / 正常 / 注意 |
```

---

## Step 5: alerts.md への通知

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` の末尾に追記:

問題なしの場合:
```
| YYYY-MM-DD 02:00 | 🔵 INFO | ファイル健全性OK | 全[N]ファイル 500行以下 — アーカイブ不要 | 解決済み |
```

アーカイブ実施の場合:
```
| YYYY-MM-DD 02:00 | 🟡 MEDIUM | ファイルアーカイブ実施 | [ファイル名] ([N]行→[M]行) をarchive/YYYY/に移管 | 解決済み |
```

---

## Step 6: learnings.md への記録

`C:\Users\sawas\.openclaw\workspace\memory\learnings.md` に本日セクション追記:
```
- [FILE-HEALTH] YYYY-MM-DD ファイル健全性チェック完了。対象[N]ファイル / アーカイブ[M]件
```

---

## 完了条件
- [ ] 全対象ファイルの行数計測完了
- [ ] 500行超ファイルのアーカイブ実施（または対象なし）
- [ ] growth-metrics.mdに月次記録追記済み
- [ ] alerts.mdに通知済み
- [ ] learnings.mdに記録済み
