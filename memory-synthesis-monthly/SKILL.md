---
name: memory-synthesis-monthly
description: 毎月8日03:00 JST - メモリファイル横断統合・抽象パターン昇格
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

`C:\Users\sawas\.openclaw\workspace\memory\` ディレクトリ内のメモリファイル群を横断統合して、抽象パターンを昇格させます。

---

## Step 0: Preflight

`anti-recurrence-rules.md` を Read して確認済みと宣言してから進む。

---

## Step 1: メモリファイル全体を読み込む

`C:\Users\sawas\.openclaw\workspace\memory\` ディレクトリ内のすべてのファイル（`.md` ファイル群、`cron-logs/` サブディレクトリ含む）を Read して内容を把握する。

取得した内容を以下に分類:
- ファイル数: N件
- cron-logs内のエントリ数: N件
- 最も古い記録: [日付]
- 最も新しい記録: [日付]

---

## Step 2: 関連観察を発見してリレーションを作成

以下のパターンでエンティティ間の関係を分析する:

**A. 同一ツール・システムへの複数観察**
例: 「bird CLI認証」と「X投稿Cookie方式」→ "SUPERSEDES" リレーション

**B. 問題 → 解決策のペア**
例: 「ブラウザ競合エラー」と「30分ずらし解決策」→ "RESOLVED_BY" リレーション

**C. 同一カテゴリの繰り返し観察**
例: 「API残高確認」が3件 → "PATTERN_OF" リレーション

発見した関係を `C:\Users\sawas\.openclaw\workspace\memory\knowledge-synthesis-log.md` に記録:
```markdown
### 発見した関係
| From | To | 関係タイプ |
|------|-----|----------|
| [記録A] | [記録B] | SUPERSEDES / RESOLVED_BY / PATTERN_OF / LEADS_TO / CONTRADICTS |
```

---

## Step 3: 上位抽象パターンをエンティティとして昇格

Step 2 で発見した繰り返しパターン（3件以上の同類観察）から、上位抽象概念を生成する:

例:
- 3件の「ブラウザタスク競合」観察 → 「PATTERN: ブラウザ自動化は時刻管理が脆弱」エンティティを作成
- 4件の「Cookie失効」観察 → 「PATTERN: セッション認証は定期更新が必須」エンティティを作成

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\memory-synthesis-monthly.md` に追記:
```markdown
## PATTERN: [パターン名]
- タイプ: AbstractPattern
- パターンの説明: [説明]
- 根拠となる観察: N件
- 推奨対策: [対策]
```

---

## Step 4: 既存ルールとの重複チェック

生成した抽象パターンを `anti-recurrence-rules.md` の既存ルールと照合する。

- パターンがルールとして未登録 → alerts.md に「新ルール候補」として通知
- パターンが既存ルールと矛盾 → alerts.md に「ルール更新候補」として通知
- パターンが既存ルールと重複 → knowledge-synthesis-log.md に既存ルール番号との対応を記録

---

## Step 5: knowledge-synthesis-log.md を更新

`C:\Users\sawas\.openclaw\workspace\memory\knowledge-synthesis-log.md` に追記:

```markdown
## YYYY-MM 統合レポート

### グラフ統計
- 統合前: エンティティ N件 / リレーション N件
- 統合後: エンティティ N件 / リレーション N件
- 新規追加リレーション: N件
- 新規昇格パターン: N件

### 今月発見したパターン
| パターン名 | 根拠観察数 | 関連ルール | アクション |
|-----------|---------|---------|---------|
| [パターン] | N件 | RULE-XXX or なし | [昇格済/新ルール提案/既存と統合] |

### 廃止候補エンティティ（古くなった観察）
- [6ヶ月以上前のエンティティで現在の状況と異なるもの]
```

---

## Step 6: alerts.md への通知

新規ルール候補・更新候補があれば alerts.md に追記:
```
## 🟣 [YYYY-MM-DD] メモリファイル統合完了: N件の新パターン発見
- 新規ルール候補: N件（anti-recurrence-rules.mdへの追加を推薦）
- 廃止エンティティ候補: N件
- 詳細: workspace/memory/knowledge-synthesis-log.md
```

---

## 完了宣言

「🧠 メモリファイル統合完了 YYYY-MM | 新リレーション: N件 | 昇格パターン: N件 | 新ルール候補: N件」