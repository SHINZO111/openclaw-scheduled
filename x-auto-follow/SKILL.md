---
name: x-auto-follow
description: X自動フォロー。毎時（07-23時JST）cron実行、1回8件。
---

## 手順（この順番で実行すること）

**Step 1 — スクリプト実行（必須・最初に行う）**

PowerShellツールで以下のコマンドを「一字一句そのまま」実行する（引用符・呼び出し演算子`&`を省略・変更しない）:
```
& node 'C:\Users\sawas\.openclaw\workspace\tools\x-poster\auto-follow-ai.js' --count 8
```

⚠️ 注意: node.exeはPATHに登録済みのため `node` のみで呼び出す。
`C:\Program Files\nodejs\node.exe` のようにスペースを含むフルパスを`&`無しで（または二重引用符のみで）実行すると
`Unexpected token` エラーになるため、フルパス表記は使用しない。

**Step 2 — 結果ファイル読み込み（絶対パス必須）**

Read ツールで以下を読む:
path = C:\Users\sawas\.openclaw\workspace\tools\x-poster\last_run_result.json

**Step 3 — 終了**

読んだ内容（followedThisRun, followedToday）を返してセッション終了。

⛔ 禁止事項:
- messageツール使用禁止（Discord通知はスクリプトが自動送信済み）
- cronツール使用禁止
- 相対パス使用禁止（last_run_result.json のみは不可）