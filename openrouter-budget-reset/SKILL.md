---
name: openrouter-budget-reset
description: 毎週月曜06:00 JST - OpenRouterガードレール予算を$13/週（¥2000）にリセット
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

# OpenRouter 予算リセット

## 目的
毎週月曜にOpenRouterのガードレール予算を$13/週（≈¥2000）にリセットして、週次予算上限を維持する。

## 設定値（変更時はここを更新）
- **リセット先URL**: `https://openrouter.ai/workspaces/default/guardrails/a458613b-2803-450d-826d-e765a25248c2/edit`
- **予算上限**: $13（週次）
- **ガードレールID**: `a458613b-2803-450d-826d-e765a25248c2`（変更時は更新）

> ⚠️ **[BROWSER-AUTOMATION-REQUIRED]**: このタスクは `mcp__playwright__` ブラウザ操作を必要としますが、**isolated cron セッションでは mcp__playwright__ は使用できません**。以下の手順で手動実行またはCoworkセッションでの実行を要求してください。

## Step 1: 自動実行の可否確認

まず `mcp__Claude_in_Chrome__navigate` が使用可能か確認する:
- 使用可能 → Step 1b（Chrome MCPで自動実行）へ
- 使用不可（isolated cron）→ Step 1c（手動実行要求）へ

### Step 1b: Chrome MCPで自動実行
```
mcp__Claude_in_Chrome__navigate(url="https://openrouter.ai/workspaces/default/guardrails/a458613b-2803-450d-826d-e765a25248c2/edit")
```
ページが表示されたら Credit Limit フィールドを「13」に更新して保存する。

### Step 1c: 手動実行要求（isolated cronの場合）
以下のメッセージをユーザーに通知してタスクを終了する:

```
⚠️ OpenRouter予算リセット — 手動実行が必要です

ブラウザ操作が必要なため自動実行できません。
以下のURLを開いてCredit Limitを $13 に設定してください:

https://openrouter.ai/workspaces/default/guardrails/a458613b-2803-450d-826d-e765a25248c2/edit

ガードレールID: a458613b-2803-450d-826d-e765a25248c2
設定値: $13/週
```

alerts.mdに手動実行要求として記録して終了。

## Step 2: 予算値を変更（Step 1bの場合のみ）

Credit Limitフィールドをクリアして「13」を入力。
フィールドが見つからない場合:
→「OpenRouterのUI構造が変更された可能性。手動で https://openrouter.ai/workspaces/default/guardrails/ を確認してください」と報告して終了。

## Step 3: 保存して確認（Step 1bの場合のみ）

Saveボタンをクリックして保存確認。

保存確認:
- ✅ 「Saved」「保存しました」等のメッセージが表示された → 成功
- ❌ エラーメッセージが表示された → 内容を記録して報告

## Step 4: 完了報告とログ記録

```powershell
$logLine = "$(Get-Date -Format 'yyyy-MM-dd HH:mm') | OpenRouter予算リセット完了 | $13/週 | ガードレールID: a458613b"
Add-Content "C:\Users\sawas\.openclaw\workspace\memory\alerts.md" -Value $logLine -Encoding UTF8
```

報告メッセージ:
```
✅ OpenRouter予算リセット完了
予算上限: $13/週（≈¥2000）
実行日時: YYYY-MM-DD HH:MM JST
ガードレールID: a458613b-2803-450d-826d-e765a25248c2
```

## エラーハンドリング

| 状況 | 対処 |
|------|------|
| ログイン必要 | 手動ログインを促す通知を表示して終了 |
| UI構造変更 | 手動確認を促す通知を表示して終了 |
| 保存エラー | エラー内容をalerts.mdに記録して通知 |
| タイムアウト | 30秒以内に完了しない場合は失敗として記録 |
