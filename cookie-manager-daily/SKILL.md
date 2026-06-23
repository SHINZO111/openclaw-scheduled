---
name: cookie-manager-daily
description: 毎日06:00 JST - X投稿Cookieの有効期限チェックと自動更新
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

## 前提条件
- Playwright chromiumバイナリが存在すること（C:\Users\sawas\AppData\Local\ms-playwright\ 配下）
- バイナリが存在しない場合、このジョブは即座に失敗終了すること（ダウンロードを試みない）

あなたはX投稿Cookie自動管理エージェントです。以下の手順を実行してください。

## タスク: Cookieの状態チェックと必要に応じた更新

### Step 1: Cookie状態の確認

まず、現在のCookieファイルの状態を確認します。

1. **Cookieファイルの存在確認**
   - ファイルパス: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json`
   - ファイルが存在しない場合は、新規作成プロセスを開始

2. **Cookieの有効期限チェック**
   - Cookieファイルの作成日時を確認
   - 25日以上経過している場合は「有効期限切れ」と判定
   - 7日以上経過している場合は「警告状態」と判定

3. **Cookie内容の検証**
   - 認証トークン（auth_token, ct0）が含まれているか確認
   - Cookieの形式が正しいか確認

### Step 2: 必要に応じたCookieの更新

Cookieが有効期限切れまたは警告状態の場合は、更新プロセスを開始します。

1. **ブラウザの起動**
   - Playwrightを使用してブラウザを起動
   - Xのログインページにアクセス

2. **手動ログインの促し**
   - ユーザーに手動でXにログインしてもらう
   - ログイン完了後、ブラウザを閉じる

3. **Cookieの取得と保存**
   - 更新されたCookieを取得
   - 認証トークンを含むCookieのみをフィルタリング
   - ファイルに保存

### Step 3: 結果の記録と通知

1. **結果の記録**
   - Cookieの状態をログに記録
   - 更新が必要だった場合は、その理由と結果を記録

2. **通知の送信**
   - Cookieの状態をDiscordに通知
   - 更新が必要だった場合は、その内容を通知

## 実行コマンド

以下のコマンドを使用してCookie管理を実行します：

```powershell
# Cookie状態のチェック
$node = "C:\Program Files\nodejs\node.exe"
$script = "C:\Users\sawas\.openclaw\workspace\tools\cookie-manager.js"
& $node $script check

# Cookieの更新（必要な場合）
& $node $script refresh

# Cookie状態の詳細表示
& $node $script status
```

## 通知メッセージのフォーマット

### 正常時（Cookieが有効）
```
🟢 Cookie状態正常
- 経過日数: [日数]日
- 有効期限: [残り日数]日
- 認証トークン: 正常
```

### 警告時（7日以内に期限切れ）
```
🟡 Cookie警告
- 経過日数: [日数]日
- 有効期限: [残り日数]日
- 認証トークン: 正常
- 対策: 近日中に更新が必要です
```

### 緊急時（有効期限切れ）
```
🔴 Cookie有効期限切れ
- 経過日数: [日数]日
- 認証トークン: 無効または不足
- 対策: 直ちに更新が必要です
- コマンド: node cookie-manager.js refresh
```

### 更新成功時
```
✅ Cookie更新成功
- 更新日時: [日時]
- 新しい認証トークン: [数]個取得
- 有効期限: 25日延長
```

### 更新失敗時
```
❌ Cookie更新失敗
- エラー内容: [エラーメッセージ]
- 手動での更新が必要です
- コマンド: node cookie-manager.js refresh
```

## 自動化の仕組み

1. **定期実行**: 毎日06:00 JSTに自動実行
2. **状態監視**: Cookieの有効期限を常時監視
3. **自動更新**: 有効期限切れ前に自動更新（ユーザー手動操作が必要）
4. **ログ記録**: すべての操作をログに記録
5. **通知**: 状態変化をDiscordに通知

## エラーハンドリング

1. **ファイル不存在**: 新規作成プロセスを開始
2. **形式不正**: エラーを記録しユーザーに通知
3. **認証失敗**: 手動更新を促す
4. **ネットワークエラー**: リトライ機構

## 保守・管理

1. **ログファイル**: `C:\Users\sawas\.openclaw\workspace\tools\cookie-manager.log`
2. **設定ファイル**: `C:\Users\sawas\.openclaw\workspace\tools\cookie-manager.js`
3. **Cookieファイル**: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x-twitter-cookies.json`

## 注意事項

- Cookieの更新にはユーザーの手動操作が必要
- 更新中はブラウザが自動で開かれる
- ログイン後はブラウザを閉じる必要がある
- 定期実行は自動だが、手動での実行も可能

---

このスキルにより、X投稿サービスの安定性が向上し、有効期限切れによる投稿失敗を防ぐことができます。