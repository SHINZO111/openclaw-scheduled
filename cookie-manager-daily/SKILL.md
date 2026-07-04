---
name: cookie-manager-daily
description: 毎日06:00 JST - X投稿Cookieの有効期限チェックと自動更新
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの読み取りは不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

**前提条件**: Playwright chromiumバイナリ（`C:\Users\sawas\AppData\Local\ms-playwright\`）が存在すること。なければ即終了（ダウンロードを試みない）。

---

## Step 1: Cookie状態確認

```powershell
$cookiePath = "C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json"
$node = "C:\Program Files\nodejs\node.exe"
$script = "C:\Users\sawas\.openclaw\workspace\tools\cookie-manager.js"
& $node $script check
```

判定基準:
- ファイルが存在しない → 新規作成プロセス開始
- 25日以上経過 → **有効期限切れ**（Step 2へ）
- 7日以上経過 → **警告状態**（Step 2へ）
- 7日未満 → 正常（Step 3で通知して終了）

## Step 2: Cookie更新（有効期限切れ・警告時のみ）

```powershell
& $node $script refresh
```

更新にはユーザーの手動ログインが必要。ブラウザが自動で開かれるのでログイン後閉じる。

## Step 3: Discord通知

| 状態 | メッセージ |
|---|---|
| 🟢 正常 | `Cookie状態正常 - 経過[N]日 / 残り[N]日` |
| 🟡 警告 | `Cookie警告 - 経過[N]日 / 近日中に更新が必要` |
| 🔴 期限切れ | `Cookie有効期限切れ - 直ちに更新が必要 / node cookie-manager.js refresh` |
| ✅ 更新成功 | `Cookie更新成功 - 新トークン[N]個取得 / 25日延長` |
| ❌ 更新失敗 | `Cookie更新失敗 - [エラー内容] / 手動対応が必要` |

ログ: `C:\Users\sawas\.openclaw\workspace\tools\cookie-manager.log`