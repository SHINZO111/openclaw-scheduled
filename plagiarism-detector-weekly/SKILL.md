---
name: plagiarism-detector-weekly
description: |
  @KURAOpenclaw の過去7日間のX投稿ログをスキャンし、参照元記事との類似度を確認。
  剽窃リスクが高い投稿をDiscordに週次報告する。
  以下のフレーズで起動：
  - 「剽窃チェック実行」「plagiarism check」「週次コンテンツ品質確認」
---

> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。失敗時はメッセージを返してセッション終了のみ。

**[EXEC-DIRECTIVE]** 外部ファイルの探索は不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること。

---

## 実行手順（毎週月曜 08:00 JST）

**Step 1: 投稿ログ収集**
`C:\Users\sawas\.openclaw\workspace\tools\x-poster\logs\post-*.log` を過去7日分読み込み、`event: post_success` のエントリから `mainHead` / `tweetUrl` / `ts` を抽出。

**Step 2: 投稿本文と参照URLを取得**
`tweetUrl` がある場合は `web_fetch` で本文全体を取得し、本文中の `http://https://` で始まるURLを参照元として抽出。web_fetch 失敗時はそのエントリをスキップ。

**Step 3: 参照元記事との比較**
各参照元URLを `web_fetch` で取得（失敗したらSKIP）し、投稿本文の5語以上の固有フレーズが参照元にそのまま含まれるか確認。含まれる場合は「類似度高（要確認）」フラグ。

**Step 4: 重複投稿チェック**
過去7日のログ内で同じ参照URLが複数回使われていないか確認。

**Step 5: レポートをメッセージとして返す**
```
【週次剽窃リスクチェック - YYYY/MM/DD】
■ チェック対象: N件（YYYY/MM/DD〜YYYY/MM/DD）
■ 類似度高（要確認）: N件
  - [ts] 本文冒頭: XXX... | 参照元: URL
■ 同一ソース複数投稿: N件 | URL → N回使用
■ 正常: N件 | スキップ（取得失敗）: N件
総合判定: 問題なし / 要確認あり
```

ログなし時: 「過去7日のログなし」と返して終了。
全スキップ時: 「X側のBot制限によりツイート本文取得不可。スキップ件数: N」と返して終了。
