---
name: daily-note-post
model: openrouter/google/gemini-2.5-flash
description: 月・木 21:00 JST - 恋活コンテンツのストック管理 + 校正 + note.com自動投稿 + X告知（完全自律版）

## 重要: 恋活コンテンツ専用ジョブ
- このジョブは恋活コンテンツのみを担当
- AI技術解説はnote-weekly-postで管理
- Substack関連はsubstack-engageで管理
- 重複投稿を防ぐため、カテゴリを明確に分離
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

## ⚡ Preflight: Playwright ロック確認（**web_search 開始前・最優先**）

**この確認をコンテンツ生成開始前に必ず実行すること:**

1. Read ツールで `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. **ファイルが存在し、中の `ts` が現在時刻（ms）から600000ms＝10分以内** → 別のX投稿ジョブが実行中  
   Discordに「⚡ 別ジョブ実行中のためスキップ」と1行報告して即終了
3. **ファイルが存在しない or `ts` が10分超過（stale）** → そのまま続行  
   （ロック取得は post-to-x.js が自動で行う。手動作成は不要）

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## note.com 完全自律パイプライン

月曜・木曜の21時に実行。以下の3フェーズを順番に実行する。
**全フェーズをOpenClawのLLM（Agent tool）で実行する。外部APIキー不要。**

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## 前提条件

- Playwright chromiumバイナリが存在すること（C:\Users\sawas\AppData\Local\ms-playwright\ 配下）
- バイナリが存在しない場合、このジョブは即座に失敗終了すること（ダウンロードを試みない）

`C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\auth_state.json` が存在すること。
存在しない場合は **タスクを停止し、ユーザーに以下の実行を依頼する**：
```
python C:\Users\sawas\.openclaw\scheduled\daily-note-post\save_note_auth.py
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Phase 1: ストック確認＆記事自動生成

### Step 1-1: 残りストックを確認

`Read` ツールで以下を読む：
`C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\posted_articles.json`

`posted` リストに含まれていない `article*_for_posting.txt` の数をカウントする。

### Step 1-2: ストック5本以下なら記事生成（Agent tool並列実行）

**条件**: 未投稿が5本以下の場合のみ実行。6本以上あればPhase 2へスキップ。

**手順**:

1. `story_bible.md` を read_file で読み込む（ストーリー設定・文体ルール・進行状況）
2. 直近3本の記事ファイルを read_file で読み込む（文脈把握）
3. story_bible.md と直近記事の内容をもとに、次の5本の記事設計を決める：
   - 各記事のタイトル案、内容要約、ストーリー上の位置づけ
   - 奇数番号 = 実録、偶数番号 = ノウハウ
4. **Agent tool で並列生成する**：
   - 5本を2〜3グループに分割
   - 各Agentのpromptに以下を含める：
     - story_bible.md の文体ルール全文
     - 担当記事の設計（タイトル・内容・番号）
     - 前後の記事との繋がり情報
     - 「`Write` ツールで直接ファイル保存すること」
     - 保存先: `C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\`
     - ファイル名: `article{番号}_m_story_{番号}_for_posting.txt`
   - Agentへの指示テンプレート：
     ```
     以下の記事ファイルを生成してください。`Write` ツールで保存。
     保存先: C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\
     
     ## 文体ルール
     （story_bible.md の文体ルールをここに貼る）
     
     ## 生成する記事
     - ファイル名: article{N}_m_story_{N}_for_posting.txt
     - タイトル: 【50歳の実録XX】○○○○
     - 内容: （要約）
     - 文字数: 5000〜7000文字
     - 有料マーカー: 70%地点に挿入
     - 末尾: ---\n\n新造＠ポンコツ50歳の恋活成功術
     ```
5. 全Agentの完了後、`story_bible.md` の「ストーリー進行状況」セクションを更新

**重要**: generate_articles.py は使わない。OpenClawのAgent toolで生成する（外部APIキー不要）。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Phase 2: 投稿前校正チェック

### Step 2-1: 次の投稿対象記事を特定

`posted_articles.json` の `posted` リストに含まれていない記事のうち、
番号が最も小さいものが次の投稿対象。

### Step 2-2: 校正チェック実行（Agent tool）

**Agent tool** で編集校正エージェントを起動する。promptに以下を含める：

```
あなたは一流出版社の編集者です。以下の記事ファイルを読み、
誤字脱字・文章校正チェックを行い、問題があればedit_blockで修正してください。

対象: {ファイルパス}

チェック項目:
1. 誤字脱字: 漢字の変換ミス、タイポ
2. 文法: 助詞の誤り、主述の不一致
3. 表記ゆれ: 「俺」統一、「Mさん」表記統一
4. 有料マーカー: 「ここから先は有料記事になります」が存在するか
5. タイトル形式: 「# 【50歳の...】」で始まっているか
6. 末尾署名: 「新造＠ポンコツ50歳の恋活成功術」が存在するか
7. 文字数: 3000文字以上あるか

修正方針: 著者の文体を崩さない最小限の修正。修正箇所を報告。
```

Agentの結果を確認し、重大な問題がなければ Phase 3 へ進む。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## Phase 3: note.com投稿＆X告知

### Step 3-1: 1日1回制限チェック

`posted_articles.json` の `last_posted_at` が今日（JST）の場合はスキップ。

### Step 3-2: 投稿スクリプト実行

`exec` ツールで実行：

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = 'utf-8'
& 'C:\Program Files\Python312\python.exe' 'C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\daily_post_runner.py'
```

**注意**: `daily_post_runner.py` 内の `run_post_generation_check()` はAPIキーなしで失敗するが、
投稿自体は正常に完了する。このエラーは無視してよい（Phase 1で生成済み）。

### Step 3-3: 結果確認

投稿後、以下のログファイルを read_file で確認：
`C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\logs\post_YYYYMMDD_*.log`

**結果判定：**
- `✅ 自動投稿処理完了` → 投稿成功
- `AUTH_ERROR` → **タスク停止**。`save_note_auth.py` の再実行をユーザーに依頼
- `❌ 投稿エラー` → 失敗。エラーをログに記録して終了
- `✅ X投稿完了` → X告知成功
- X失敗 → note投稿は成功済み。エラーのみ記録

### Step 3-4: posted_articles.json は自動更新

`daily_post_runner.py` が自動で `posted_articles.json` を更新する。
Claude による手動編集は不要。

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## アーキテクチャ

```
OpenClaw Cron（月曜・木曜 21:00 JST）
  ↓
OpenClaw セッション起動（SKILL.md 読み込み）
  │
  ├─ Phase 1: ストック管理（Agent tool 並列実行）
  │   ├─ posted_articles.json 確認
  │   ├─ 残り5本以下？ → story_bible.md + 直近記事を読み込み
  │   ├─ Agent tool で記事生成サブエージェント起動（2〜3並列）
  │   │    └─ 各Agent: write_file で記事ファイル保存
  │   └─ story_bible.md 更新
  │
  ├─ Phase 2: 投稿前校正（Agent tool）
  │   ├─ 次の投稿対象を特定
  │   ├─ Agent tool で編集校正エージェント起動
  │   │    └─ 誤字脱字・文法・表記ゆれ → edit_block で修正
  │   └─ 結果確認
  │
  └─ Phase 3: 投稿実行
       ├─ daily_post_runner.py 実行（PowerShell経由）
       │    ├─ 投稿前品質チェック（pre_publish_check.py）
       │    ├─ note.com に投稿（Playwright、100円、タグ3種）
       │    ├─ Xシェアボタン経由で @pon_shinzo へ告知
       │    └─ posted_articles.json 自動更新
       └─ ログファイル確認 → 結果報告
```

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## スケジュール

| 曜日 | 時刻 | cron式 |
|------|------|--------|
| 月曜 | 21:00 JST | `0 21 * * 1` |
| 木曜 | 21:00 JST | `0 21 * * 4` |

投稿ペース: 週2本（月・木）
価格: ¥100 固定
タグ: 恋活, チャット, 50代

---

# ⛔⛔⛔ ABSOLUTE PROHIBITION — cronツール完全禁止 ⛔⛔⛔

**このセッションでは `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは絶対に使用してはならない。**

- このエージェント自身がcronジョブとして実行されており、cronツールを呼び出すとシステムエラーになる
- 失敗・エラー等、**いかなる状況でもcronツールを使ってはならない**
- 自己再起動・別ジョブ起動も**完全禁止**
- **唯一の許可された終了方法**: エラー内容をDiscordに報告してメッセージを返し、セッションを終了する

---
## トラブルシューティング

| 症状 | 原因 | 対処 |
|------|------|------|
| `AUTH_ERROR` | auth_state.json セッション切れ | `save_note_auth.py` を手動実行 |
| `FAILED: タイトル入力欄が見つかりません` | note.com UI変更 | `error_screenshot.png` を確認 |
| Phase 1 で記事の質が低い | story_bible.md の情報不足 | story_bible.md を手動で充実させる |
| X投稿失敗 | X cookie 期限切れ | `x_setup_launcher.py` を実行 |

**ログファイル**: `C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\logs\post_YYYYMMDD_HHMMSS.log`
**エラースクリーンショット**: `C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\error_screenshot.png`
**ストーリー設定**: `C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\story_bible.md`
