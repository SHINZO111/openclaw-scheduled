---
name: memory-consolidation
description: 毎週日曜23:00 JST - メモリ統合（重複削除・古い情報整理）
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取りは不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## タスク: 週次メモリ統合

> 📌 **Bootstrap肥大化防止が最優先**: memory/の日付ファイルが蓄積するとisolated cronがタイムアウトする。必ずStep 0を先に実行すること。

**Step 0: 日付ファイルの7日超クリーンアップ（必須・最優先）**

`C:\Users\sawas\.openclaw\workspace\memory\` 配下のファイルを列挙。
ファイル名が `YYYY-MM-DD` または `YYYY-MM-DD-HHMM` 形式（例: `2026-06-24-1302.md`）のものを対象にする。

処理手順:
1. 各日付ファイルを Read して内容を確認
2. **作成から7日以上経過**しているファイル → 重要エントリ（⭐/重要/KEY等のマーカーか、5行以上の具体的な知見）があれば `MEMORY.md` の末尾に `## [元ファイル名] より [YYYY-MM-DD]` として要約を追記
3. 要約追記後（または内容が不要と判断した場合）→ **ファイルを削除（Write で空にしてから Delete、またはmcp__Windows-MCP__PowerShell で `Remove-Item`）**
4. 削除ファイルと保存した知見の件数を記録

目標: **memory/ の .md ファイル総サイズを 80KB 以下に維持する**

**Step 1**: `C:\Users\sawas\.openclaw\workspace\memory\` 配下の主要ファイルを読み込む。

**Step 2**: 各ファイルを処理:
- **learnings.md**: 重複削除 / 30日超の軽微エントリをアーカイブセクションへ移動（重要な学習は残す）
- **growth-metrics.md**: 直近30日分を保持 / それ以前は月次サマリー1行に圧縮
- **failures.md**: 解決済みに `[RESOLVED]` 付与 / 90日超の解決済みエントリを削除
- **anti-recurrence-rules.md**: 効果未確認ルールに `[要見直し]` / 重複ルールをマージ

**Step 3**: `C:\Users\sawas\.openclaw\CLAUDE.md` を読み込み、古くなった情報・矛盾があれば提案としてまとめる（直接編集はしない）。

**Step 4**: `learnings.md` に統合レポートを追記:
```
## [YYYY-MM-DD] 週次メモリ統合レポート
- 処理ファイル数: X件 / 削除エントリ: X件 / アーカイブ: X件
- memory/ 総サイズ: XX KB（目標80KB以下）
- 要注意事項: [あれば記載]
```

完了後「✅ メモリ統合完了: [削除X件 / アーカイブX件 / memory/サイズ: XX KB]」と報告。