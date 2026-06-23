---
name: note-analytics-monthly
description: 毎月1日00:00 JST - Note.comパフォーマンス追跡・note-performance-log更新・投稿戦略改善
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# note-analytics-monthly
# 実行時刻: 毎月21日 09:00 JST
# 目的: Note.com (@KURAOpenclaw / SHINZO) の月次パフォーマンスを追跡し、X投稿と同様の改善ループを構築する

---

## Step 1: note-performance-log.md の準備

`C:\Users\sawas\.openclaw\workspace\memory\note-performance-log.md` を読み込む。
ファイルが存在しない場合は新規作成:

```markdown
# Note.com パフォーマンスログ

> note-analytics-monthly（毎月21日）が自動更新する。
> X投稿と同様の改善ループをNote.comにも適用する。

---

## 月次パフォーマンス記録

| 月 | 投稿数 | 総ビュー数 | 総スキ数 | フォロワー増減 | TOP記事 | 評価 |
|----|-------|-----------|---------|-------------|--------|------|

---

## 記事別パフォーマンス

---

## バイラル記録（スキ50件以上）

---

## 月次戦略メモ
```

---

## Step 2: 今月の投稿データ収集

`mcp__brave-search__brave_web_search` で以下を検索:
- `site:note.com KURA AI` （KURAアカウントの最新記事を確認）
- `site:note.com AI 建設` （関連記事の動向）

直近1ヶ月の投稿について可能な範囲で以下を確認:
- 記事タイトル
- 推定ビュー数（ページランク・シェア数から推定）
- note-weekly-post の実行ログがあれば参照

データが取得できない場合は、note-performance-log.md に「未取得」として記録し、SHINZOに手動入力を依頼するアラートを出す。

---

## Step 3: note-performance-log.md 月次記録の追記

```
## YYYY-MM 月次記録

### サマリー
| 項目 | 数値 |
|------|------|
| 投稿数 | [N] |
| 総ビュー数 | [N or 未取得] |
| 総スキ数 | [N or 未取得] |
| フォロワー増減 | [±N or 未取得] |

### 記事別パフォーマンス
| タイトル | ビュー数 | スキ数 | 評価 |
|---------|---------|-------|------|
| [タイトル] | - | - | 🔲 |

### TOP記事
[最もパフォーマンスが高かった記事タイトルと特徴]

### BOTTOM記事  
[最もパフォーマンスが低かった記事タイトルと改善提案]
```

---

## Step 4: X投稿との相関分析

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を読み込む。

同じ週にX投稿TOP3のトピックとNote記事のテーマを比較:
- X投稿で高反応だったトピックがNote記事でも高反応か？
- 相関が高い場合: 「XのバズをNoteで深掘り」戦略を強化
- 相関が低い場合: Note独自の読者層を探る

分析結果を note-performance-log.md の「月次戦略メモ」に記録。

---

## Step 5: note-weekly-post プロンプト改善（オプション）

BOTTOM記事のトピックについて、改善方向を特定する（自動実行ではなく提案のみ）:
- **A: テーマ変更** — 低反応トピックを避け、X投稿TOP3と連動したテーマに変更
- **B: 構成変更** — 「結論→根拠→まとめ」の構成に統一
- **C: タイトル改善** — 数字・問いかけ・感情ワードをタイトルに含める

note-weekly-post のプロンプト更新は `C:\Users\sawas\.openclaw\workspace\alerts.md` に以下の形式で追記（isolated cronセッションからはジョブの直接変更は不可）:
```
| YYYY-MM-DD HH:MM | 🔴 ACTION-REQUIRED | note-weekly-postプロンプト更新推奨 | [変更内容] — 手動実施推奨 | 未解決 |
```

---

## Step 6: alerts.md への通知

`C:\Users\sawas\.openclaw\workspace\memory\alerts.md` の末尾に追記:

```
| YYYY-MM-DD 09:00 | 🔵 INFO | Note月次分析完了 | [N]記事分析 / TOP:[タイトル] — note-performance-log.md 参照 | 解決済み |
```

データ未取得が多い場合:
```
| YYYY-MM-DD 09:00 | 🟡 MEDIUM | Note分析データ不足 | 手動でビュー数・スキ数を note-performance-log.md に入力してください | 未解決 |
```

---

## 完了条件
- [ ] note-performance-log.md 月次記録追記済み
- [ ] X投稿との相関分析完了
- [ ] note-weekly-post プロンプト改善実施（または対象なし）
- [ ] alerts.md 通知済み
