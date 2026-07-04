---
name: viral-amplifier-daily
description: バズ投稿緊急増幅プロトコル — 毎日14:00に投稿エンゲージメントを確認し、バズシグナル検出時に増幅コンテンツを自動生成してSHINZOに通知する
---

> **[Discord report requirement]** The `message` tool errors if `target` is omitted. When reporting, always specify `target: "discord:1489796417449889844"` (guild: 1489796417449889842 / channel: general) explicitly.
> ⛔ **[SYSTEM CONSTRAINT] cronツール絶対禁止**: `cron.run` / `cron.list` / `cron.forceRun` / `cron.update` 等は使用不可。自己自身がcronジョブとして動作中。失敗時はDiscordに報告してセッション終了のみ。

**[EXEC-DIRECTIVE]** このプロンプトにすべての手順が含まれています。外部ファイルの読み取りは不要。直接タスクを開始。

⚠️ **スケジュール実行の必須ルール**: 失敗・中断しても必ず何らかのメッセージを返して終了すること（空レスポンスはシステムエラー）。

---

# viral-amplifier-daily — バズ投稿緊急増幅プロトコル v1.0
実行時刻: 毎日 20:00 JST

---

## Step 0: 実行前確認

以下を Read して現在のコンテキストを把握:
- `C:\Users\sawas\.openclaw\workspace\memory\x-performance-log.md` → 直近の投稿パフォーマンスデータ
- `C:\Users\sawas\.openclaw\workspace\memory\cron-logs\viral-amplifier-daily.md` → 過去の増幅実績

---

## Step 1: バズシグナル検出

`x-performance-log.md` から直近24〜48時間以内のエンゲージメントデータを取得。

**バズ判定基準（1つ以上で判定）:**

| シグナル | バズ閾値（4時間後） |
|---------|------------|
| いいね | 30件以上 |
| RT | 10件以上 |
| インプレッション | 3000以上 |
| リプライ | 5件以上 |

データがない場合: 「データ不足 — 計測待ち」として記録し、Step 2をスキップしてStep 3の通知のみ実行。

---

## Step 2: バズ検出時 — 増幅コンテンツ生成

### 2-A: リプライ追加投稿案（補足スレッド）
バズ投稿を深掘りする補足リプライを3案（各140文字以内、ハッシュタグ禁止（本体投稿プロトコル準拠）:
- **案1: データ深掘り** — バズ投稿で言及した数字/事実の詳細
- **案2: 実践Tips** — 実際に使う方法
- **案3: 問いかけ** — フォロワーの意見を引き出す

### 2-B: 関連スレッド展開案
バズ投稿と同一テーマで3〜5ツイートのスレッド1本（各120文字以内）:
- 構成: 要約 → 背景 → 詳細1 → 詳細2 → まとめ＋CTA

### 2-C: 翌朝フォローアップ投稿案
バズの余熱を活かした翌朝投稿（翌日7:30想定）1本:
- 「昨日の投稿でこんな反応が〜」という引用スタイルでもOK

---

## Step 3: 結果をログファイルに記録

`C:\Users\sawas\.openclaw\workspace\memory\cron-logs\viral-amplifier-daily.md` に追記:
```markdown
## ViralAmplification_YYYYMMDD
- 検出日時: YYYY-MM-DD HH:MM
- バズ投稿: [投稿内容の冒頭30文字]
- 検出シグナル: いいね[N]件 / RT[N]件 / IMP[N]
- 生成コンテンツ: リプライ3案・スレッド1本・フォロー投稿1本
```

`x-performance-log.md` にバズパターンを追記（どんなトピック・表現がバズりやすいかの蓄積）。

---

## Step 4: SHINZOへの通知レポート

```
🔥 バズシグナル検出 — viral-amplifier-daily [YYYY-MM-DD]

【バズ投稿】[投稿内容の冒頭60文字]...
【検出シグナル】いいね[N]件 / RT[N]件 / IMP[N]

【増幅コンテンツ 3点セット（確認後に投稿してください）】

▼ リプライ補足案（推奨: 今すぐ投稿）
案1: [内容] 案2: [内容] 案3: [内容]

▼ スレッド展開案（推奨: 今日中に投稿）
1/ [内容] 2/ [内容] 3/ [内容] 4/ [内容] 5/ [内容]

▼ 翌朝フォローアップ案（推奨: 明日7:30）
[内容]

⚠️ 実際の投稿はSHINZOが確認・判断してください。
```

バズ未検出の場合:
```
✅ viral-amplifier-daily [YYYY-MM-DD]
バズシグナル: 検出なし（平常運転）
直近最高エンゲージメント: [データあれば記載、なければ「計測データ蓄積中」]
```

---

## 重要ルール
- **実際のX投稿は絶対に自動送信しない** — コンテンツ生成・通知のみ
- 生成したコンテンツはSHINZOの判断を経て投稿する
- バズ判定基準は月次で見直す