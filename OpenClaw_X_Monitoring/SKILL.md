---
name: OpenClaw_X_Monitoring
description: 毎日19:00 JST - @KURAOpenclaw のX投稿パフォーマンスを日次モニタリング・異常検知
---

**[EXEC-DIRECTIVE] このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要です。scheduledディレクトリ等の探索はせず、直接タスクを開始してください。**

⚠️ **スケジュール実行の必須ルール**: どのステップで失敗・中断しても、必ず何らかのメッセージを返して終了すること。空のままタスクを終了しないこと（空レスポンスはシステムエラーとして記録される）。

> **[SYSTEM CONSTRAINT - DO NOT OVERRIDE]**: cronツールは絶対使用禁止。`cron.run`/`cron.list`/`cron.forceRun`等のcron操作はいかなる理由があっても実行しない。エラーが発生した場合もcronで再起動せず、Discordで報告して終了する。

# OpenClaw X モニタリング — 毎日 19:00 JST

## 目的
@KURAOpenclaw の当日X投稿を確認し、エンゲージメント異常・バイラル投稿・クッキー切れを早期検知する。

---

## Step 1: 当日の投稿ログ確認

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` を Read で読み込む。

当日実行済みX投稿スキルのログを確認（以下のいずれかが存在するか）:
- `Skill_x-post-ai-stock` (08:00)
- `Skill_x-post-ai-latest` (09:05)
- `Skill_x-post-aipc-latest` (13:25)
- `Skill_x-post-physical-ai-latest` (15:35)
- `Skill_x-post-ai-health` (17:45)

---

## Step 2: 異常検知チェック

以下のいずれかに該当する場合は即座にアラート:

**A. 投稿失敗検知**
当日 08:00〜18:00 の間にX投稿スキルが全て失敗している（ログが存在しない、またはエラーログが残っている）場合。

**B. クッキー切れ検知**
`C:\Users\sawas\x_auth_state.json` が存在しない、または最終更新日時が30日以上前の場合。
→ ユーザーに「x_auth_state.jsonを更新してください」とDiscordで通知するだけ。cronツールは使わない。

**C: バイラル検知**
x-performance-log.md に直近24時間でいいね50件超の記録があれば通知。

---

## Step 3: 日次サマリー記録

`C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` に以下を追記:

```
### 日次チェック YYYY-MM-DD 19:00
- 投稿スキル実行: [実行済みスキル数]/5
- 異常: [なし / 詳細]
- 特記: [バイラル投稿があれば記録]
```

---

## Step 4: 完了報告

```
✅ X監視完了 YYYY-MM-DD
- 当日投稿: N件
- 異常: なし（または詳細）
```

異常がある場合は具体的な対処方法も合わせて報告する。
