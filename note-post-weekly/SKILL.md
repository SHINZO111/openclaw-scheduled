---
name: note-post-weekly
description: |
  OpenClaw から note.com（アカウント「新造@ポンコツ50歳の恋活成功術」）へ、恋活・婚活・恋愛心理系の
  記事を週次で自動投稿するスキル。Playwright＋Cookie認証（post-to-note.js）ベース。
  以下のフレーズで起動する：
  - 「note記事を投稿して」
  - 「恋活note書いて」
  - 「note週次投稿」
  `post-to-note.bat` / `post-to-note.js` をPowerShellから呼び出す。
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは使用不可。自己自身がcronジョブとして動作中のため呼び出すとシステムエラー。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。scheduledディレクトリ等を探索せず直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## 背景（2026-07-02 再構築）

旧 `note-poster.py`（requestsベース、架空APIエンドポイント想定・Cookie未整備）と
旧 `substack_notes_poster.py` 系（対象が note.com ではなく Substack の Notes 機能）は
どちらも note.com への投稿を実現できておらず、6/20 を最後に停止していた。
本スキルは実機の note.com エディタDOMを確認した上で新規実装した `post-to-note.js`
（`C:\Users\sawas\.openclaw\workspace\tools\note-poster\`）を使う。

---

## ⚡ Preflight: ロック確認（最優先）

1. Read で `C:\Users\sawas\.openclaw\workspace\tools\note-poster\logs\.post.lock` を読む
2. ファイルが存在し `ts` が現在時刻から600000ms（10分）以内 → Discordに「⚡ 別ジョブ実行中のためスキップ」と報告して即終了
3. ファイルが存在しない or 10分超過（stale）→ 続行（ロック取得は post-to-note.js が自動実施）

---

## Cookie 前提条件（初回のみ手動作業）

`note-cookies.json` が `C:\Users\sawas\.openclaw\workspace\tools\note-poster\` に無い場合、
投稿は exit code 3（認証失敗）で終了する。note.com には公開の投稿APIが無いため、
以下を **人間が一度だけ** 実行してCookieを取得する必要がある（cronからは自動化不可）。

```
node C:\Users\sawas\.openclaw\workspace\tools\note-poster\setup-note-cookies.js
```

ブラウザが開くので note.com に手動ログイン → ターミナルで Enter → `note-cookies.json` 生成。
Cookie は 25日超過で警告（`cookie_stale` イベント）。失効時は exit 3 で返る。

---

## アカウント

| アカウント | テーマ |
|---|---|
| 新造@ポンコツ50歳の恋活成功術（note.com） | 恋活・婚活・恋愛心理・アラフィフ〜シニア世代の出会い |

---

## 投稿フォーマット

### タイトル（20〜40文字程度）
- 具体的なターゲット（年代・状況）と悩み・結果を明示する
- 例の型: 「〜な人が知らない○○の理由」「50代の私が○○でわかったこと」「○○を続けて気づいた3つのこと」

### 本文（800〜1500文字程度）
- 一人称の実体験・気づき調（アカウント名「ポンコツ50歳」のセルフデプリケーティングなトーンを踏襲）
- 構成: 導入（あるある状況提起）→ 本論（気づき・具体的な行動やコツを2〜3個）→ まとめ（一言メッセージ）
- 見出し（##）を1〜2箇所使って読みやすく区切る
- 誇大な効果保証（「絶対に」「必ず成功する」等）は禁止。個人の実感・一般論として書く
- 参照した外部情報がある場合は「参考: URL」を末尾に記載

### ハッシュタグ（2〜4個）
- 例: 恋活, 婚活, アラフィフ婚活, 恋愛心理 などテーマに合わせて選定

---

## 禁止事項

| 禁止 | 種別 |
|---|---|
| 医療・法律・断定的な成功保証（「必ず結婚できる」等） | **BLOCKING** |
| 特定個人が特定できる実名・写真の使用 | **BLOCKING** |
| 他サイト記事の丸ごとコピペ（要約・自分の言葉での再構成のみ可） | 禁止 |
| `example.com` 等プレースホルダURL | **BLOCKING（exit 2）** |

---

## 投稿手順

**ステップ1: ネタ収集**

`web_search` で以下のようなクエリを試す（週替わりで切り口を変える）:
- `婚活 コツ 40代 OR 50代`
- `マッチングアプリ 心理 あるある`
- `恋活 男性心理 女性心理`
- `アラフィフ 婚活 体験談`

`web_search` が失敗する場合は `web_fetch` で note.com の同ジャンルの人気記事（フィード上の
恋活・婚活タグ記事）や一般的な恋愛メディアを確認し、着想を得る（丸ごと転載はしない）。

**ステップ2: タイトル・本文作成**（上記フォーマットに従う）

**ステップ3: 投稿**
```
exec: C:\Users\sawas\.openclaw\workspace\tools\note-poster\post-to-note.bat "タイトル" "本文" --tags "恋活,婚活"
```
（`--dry-run` で事前確認したい場合は第4引数に付与。ただし note.com に下書きが残るため、
確認後は手動で削除するか、公開して問題ないタイトル・本文でのみ本番実行すること。）

**ステップ4: 結果確認**
stdout に `NOTE_URL` が出力される。exit code:

| code | 意味 | 対応 |
|---|---|---|
| 0 | 投稿成功 | NOTE_URL を Discord に報告 |
| 1 | 予期せぬエラー（DOM変化等） | エラー内容をDiscordに報告、**リトライしない**（note.com側のUI変更の可能性、要人間確認） |
| 2 | 入力検証エラー | タイトル・本文を修正して再実行 |
| 3 | 認証失敗（Cookie失効・未設置） | 人間に `setup-note-cookies.js` の再実行を依頼するメッセージをDiscordに送って終了 |
| 6 | ロック競合 | 完了を待ってから再実行 |

---

## ファイル構成

```
C:\Users\sawas\.openclaw\workspace\tools\note-poster\
├── post-to-note.js         # Playwright投稿本体（ロック・ログ）
├── post-to-note.bat        # 呼び出し用バッチ
├── setup-note-cookies.js   # 手動ログイン→Cookie保存（初回のみ人間が実行）
├── lockfile.js             # 同時実行制御（x-poster から移植）
├── logger.js               # JSONLログ（x-poster から移植）
├── note-cookies.json       # Cookie（.gitignore対象、人間が手動生成）
└── logs/
    ├── post-YYYYMMDD.log   # JSONL構造化ログ（30日で自動削除）
    └── .post.lock          # PID+取得時刻（10分超過でstale自動解除）
```

---

## cronジョブ構成

| ジョブ名 | 時刻 | テーマ |
|---|---|---|
| note-post-weekly | 毎週月曜 10:00 JST | 恋活・婚活・恋愛心理（本スキル） |

X投稿ジョブ（09:00〜22:00 JST帯）と時間が被らないよう設定。

**起動メッセージ形式**:
```
【note投稿 - 新造@ポンコツ50歳の恋活成功術】
1. web_searchで恋活・婚活・恋愛心理系のネタを1件選定
2. タイトル作成（20〜40字）
3. 本文作成（800〜1500字・一人称実体験調・見出し1〜2箇所）
4. ハッシュタグ選定（2〜4個）
5. exec: C:\Users\sawas\.openclaw\workspace\tools\note-poster\post-to-note.bat "タイトル" "本文" --tags "タグ1,タグ2"
6. 結果をDiscordに報告（exit 3: Cookie再設定を人間に依頼 / exit 1: UI変更の可能性を報告し人間確認を待つ / それ以外: 内容修正のうえ再実行）
```

---

## 既知の制約・今後の課題

- 投稿フローのセレクタは 2026-07-02 時点の note.com エディタDOMを実機確認して実装したもの。
  note.com側のUI変更で `button:has-text("公開に進む")` 等が壊れる可能性がある（exit 1で検知）。
- 記事タイプは常に「無料」固定。有料記事・マガジン追加はこのスキルでは扱わない。
- Cookie失効時の自動復旧はできない（ブラウザでの手動ログインが必須のため）。exit 3 が続く場合は
  人間に `setup-note-cookies.js` の再実行を依頼すること。