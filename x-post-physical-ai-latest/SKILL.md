---
name: x-post-physical-ai-latest
description: |
  OpenClaw から X（Twitter、@KURAOpenclaw アカウント）へ フィジカルAI / ロボティクス関連の自動投稿を行うスキル。
  Playwright＋Cookie認証ベースで、投稿プロトコル（本文180-270字・リプ600-1000字、URL必須、ハッシュタグ/絵文字禁止、末尾「詳細はリプ欄へ」）を含む。
  以下のフレーズで起動する：
  - 「フィジカルAIをXで投稿して」
  - 「ロボティクスをツイートして」
  - 「フィジカルAI投稿」
  `post-to-x.bat` / `post-to-x.js` をPowerShellから呼び出す。ロボット・自律走行・具現化AI・物理AIシステム発信用途。
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等のcron系ツールは使用不可。自己自身がcronジョブとして動作中のため呼び出すとシステムエラー。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。scheduledディレクトリ等を探索せず直接タスクを開始。**

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## ⚡ Preflight: Playwright ロック確認（最優先）

1. Read で `C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\.post.lock` を読む
2. ファイルが存在し `ts` が現在時刻から600000ms（10分）以内 → Discordに「⚡ 別ジョブ実行中のためスキップ」と報告して即終了
3. ファイルが存在しない or 10分超過（stale）→ 続行（ロック取得はpost-to-x.jsが自動実施）

---

## アカウント

| アカウント | Cookie |
|---|---|
| `@KURAOpenclaw` | `x-twitter-cookies.json`（AUTH_TOKEN/CT0から生成） |

---

## 投稿フォーマット

### 本文（180〜270文字。X実測280字が投稿ブロックの絶対上限）

**文体**: 業界を追っている友人がリアルタイムで反応している感じ。完璧な文章にしない。
- 冒頭フック（30文字以上）: 具体的な固有名詞・数字・事実を含める
- 段落分割（`\n\n`）で3〜4段落に
- 末尾は次の3種を日替わりローテーション: ①詳細はリプ欄へ ②続きと出典はリプに置いた ③補足をリプ欄にまとめた
- 絵文字: 文頭に1個だけ
- 本文にURLを入れない（外部リンクは表示抑制対象。URLはリプライ末尾「参考: URL」のみ）
- 画像を添付する場合は post-to-x.bat の第3引数に画像パスを渡す（§Phase2 有効化後）

**stop-slop品質チェック（投稿前に必ず実施）**: `C:\Users\sawas\.openclaw\scheduled\stop-slop\SKILL.md` を読んで全面チェック。禁止フレーズ・構造クセ・副詞・無生物主語・受動態・リズム異常がないか確認し、あれば修正してから投稿。

### リプライ（600〜1000文字）

構成パターン（記事に合うものを選ぶ）:
- **What→So What型**: 何が起きた→なぜ重要か→見立て（3段落）
- **数字ドリブン型**: 核心の数字2-3個→比較で文脈づけ→示唆
- **逆張り型**: 一般的な見方→でも実は→根拠
- **時系列型**: 背景→今回→今後の読み

1段落最大3文、段落間に空行。参照URLをリプライ末尾に「参考: URL」として記載。

---

## 禁止事項（全面）

| 禁止 | 種別 |
|---|---|
| `#AI` 等ハッシュタグ（`#`記号を伴う全て） | **BLOCKING（exit 2）** |
| 絵文字（本文冒頭1個を除くすべて）、番号絵文字（1️⃣等） | 禁止 |
| 装飾記号（【】◆●▶ 等）、マークダウン（`**` `` `code` ``） | 禁止 |
| 報告調（〜しました・〜されています・〜とのことです） | 禁止 |
| `example.com` / `<URL>` 等プレースホルダURL | **BLOCKING（exit 2）** |

---

## URL実在性（最重要）

- URLは必ず `web_search` / `web_fetch` で実際に確認したものだけを使う
- 404・ドメイン不在は**BLOCKING**（401/403はBot検知なので実在扱いで通過するが、コンテンツ取得不可の場合は別URLを優先し、推測で本文を補完しないこと）
- `validate.js` と `post-to-x.js` のプリフライトが自動ブロック

---

## 投稿手順

**ステップ1: 情報収集（レートリミット対策あり）**

まず `web_search` で以下のクエリを試す:
- `ロボット AI 最新`
- `physical AI robotics Boston Dynamics OR Figure OR 1X`
- `自律走行 OR ヒューマノイドロボット 最新情報`
- `NVIDIA Cosmos OR embodied AI`

`web_search` が 429（レートリミット）で失敗した場合、以下の直接フェッチに切り替える（優先順）:
1. `web_fetch` で `https://techcrunch.com/category/robotics/` を確認
2. `web_fetch` で `https://www.therobotreport.com/` を確認
3. `web_fetch` で `https://gigazine.net/` のトップページを確認してロボット・フィジカルAI関連記事を探す
4. `web_fetch` で `https://www.itmedia.co.jp/aiplus/` を確認（日本語記事）
5. `web_fetch` で `https://robotstart.info/` を確認（日本語ロボット専門）

→ 参照元URLを1つ確保する。`web_fetch` で実在・記事内容を確認（401/403はOK、404は別を選ぶ）

**ステップ2: 本文作成**（180〜270文字）
- 本文にはURLを入れない（リプライ末尾にのみ記載）
- 末尾は次の3種を日替わりローテーション: ①詳細はリプ欄へ ②続きと出典はリプに置いた ③補足をリプ欄にまとめた

**ステップ3: リプライ作成**（600〜1000文字）
- 見出し（■）＋箇条書き（・）で構造化
- 参照URLを末尾に「参考: URL」として記載

**ステップ4: 投稿**
```
exec: C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.bat "本文" "リプライ文"
```

**ステップ5: 結果確認**
stdout に `TWEET_URL` / `REPLY_URL` / `VERIFY_TWEET` / `VERIFY_REPLY` が出力される。

---

## 終了コード

| code | 意味 | 対応 |
|---|---|---|
| 0 | 投稿成功 | TWEET_URL を Discord に報告 |
| 1 | 予期せぬエラー | エラー内容を Discord に報告、**リトライしない** |
| 2 | プロトコル違反（ハッシュタグ・プレースホルダURL等） | 内容修正のうえ再実行 |
| 3 | 認証失敗（Cookie 失効） | `.env` 更新 → `node setup-cookies.js` |
| 4 | レートリミット | 1時間以上待機後に再実行 |
| 5 | チャレンジ要求（reCAPTCHA） | ブラウザで手動解除 |
| 6 | ロック競合（他プロセスが投稿中） | 完了を待ってから再実行 |

---

## ファイル構成

```
C:\Users\sawas\.openclaw\workspace\tools\x-poster\
├── post-to-x.js       # Playwright投稿本体（ロック・ログ・検証・リトライ）
├── validate.js        # 投稿プロトコル検証
├── post-to-x.bat      # 呼び出し用バッチ
├── setup-cookies.js   # .envからCookie JSON生成
├── x-twitter-cookies.json  # Cookie（.gitignore済）
└── logs/
    ├── post-YYYYMMDD.log   # JSONL構造化ログ（30日で自動削除）
    ├── .post.lock          # PID+取得時刻（10分超過でstale自動解除）
    └── verify-*.png        # 投稿後検証スクショ
```

---

## 技術的注意点

1. `/compose/post` は使わない → `x.com/home` のツイートボックスを使う
2. `#layers` オーバーレイが `ポストする` ボタンをブロックする場合は `pointerEvents:none` で回避
3. `Escape` キーは押さない（「ポストを保存しますか？」ダイアログが出る）
4. テキスト入力は `navigator.clipboard.writeText()` → `Ctrl+V` でペースト
5. ボタンのselector: `x.com/home` → `tweetButtonInline` / リプライフォーム → `tweetButton`
6. `post-to-x-pon.bat` は**DISABLED**（Cookieパスをリプライ本文として投稿するバグあり）

---

## Cookie管理

**取得手順**: Chrome で X にログイン → F12 → Application → Cookies → `auth_token` と `ct0` をコピー → `.openclaw/.env` の `AUTH_TOKEN` / `CT0` を更新 → `node setup-cookies.js` を実行。

Cookie は 25 日超過で警告（`cookie_stale` イベント）、失効時は exit 3 で返る。

---

## cronジョブ構成（@KURAOpenclaw向け）

| ジョブ名 | 時刻 | テーマ |
|---|---|---|
| x-post-ai-latest | 毎日 07:30 JST | AI最新情報 / 生成AI |
| x-post-ai-pc-latest | 毎日 08:00 JST | AI PCハードウェア・新製品 |
| x-post-ai-agent | 毎日 12:00 JST | AIエージェント / マルチエージェント |
| x-post-physical-ai-latest | 毎日 19:00 JST | フィジカルAI / ロボット（本スキル） |
| x-post-ai-finance | 毎日 21:00 JST | AI金融・フィンテック |
| x-dm-welcome-daily | 毎日 22:00 JST | 新フォロワーDMウェルカム |

**起動メッセージ形式**:
```
【X投稿 @KURAOpenclaw - フィジカルAI / ロボティクス最新情報】
1. web_searchで「ロボット AI 最新」「physical AI robotics」等を検索し重要トピック1件選択。失敗時はweb_fetchで直接ニュースサイトを確認（techcrunch/therobotreport/gigazine/itmedia/robotstart）
2. web_fetchでURLを実在確認（404は別ソースへ）
3. 本文作成（180〜270文字・URLは入れない・末尾フレーズは3種ローテーション・ハッシュタグ/絵文字禁止）
4. リプライ作成（600〜1000文字・■見出し＋・箇条書き・参照URL末尾に「参考:URL」）
5. exec: C:\Users\sawas\.openclaw\workspace\tools\x-poster\post-to-x.bat "本文" "リプライ文"
6. 結果をDiscordに報告（exit 2: 内容修正 / exit 3: Cookie更新 / exit 4: 1時間待機 / exit 5: 手動解除 / exit 6: スキップ / exit 1: エラー報告のみ）
7. 【Threadsクロスポスト】X成功後: post-to-threads.bat "threads_main（詳細はリプ欄へを除去・500字以内）" "threads_reply（500字以内）"
```

---

## Stealth Browser Integration (2026-06-26)

This skill's scripts use **stealth-config.js** + **CloakBrowser** (58 C++ patches) automatically.
Fallback: standard Playwright Chromium -> chrome channel -> headed off-screen.
Config: C:\Users\sawas\.openclaw\workspace\tools\x-poster\stealth-config.js