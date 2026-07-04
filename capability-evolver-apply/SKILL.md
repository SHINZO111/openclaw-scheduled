---
name: capability-evolver-apply
description: 毎日 - capability-evolverエンジンを実行し、GEPプロトコルに従って実際にパッチを自動適用する（git安全網付き・自律進化）。失敗時は完全ロールバック。
---

> ⛔ **[SYSTEM CONSTRAINT] cronツール禁止**: `cron.*` 系ツールは使用不可。自己がcronジョブとして動作中。失敗時もDiscordへ報告して終了するのみ。
> ⚠️ **必須**: 失敗・中断・例外が起きても、必ず最後に結果メッセージを返して終了すること。

# 🧬 Capability Evolver — Auto Apply（自律進化・実適用）

このスキルは capability-evolver エンジンを実行し、生成されたGEP進化プロンプトに**実際に従ってコードを書き換える**。git をロールバック安全網として使い、検証に通った変更だけを残す。

## 作業対象と絶対制約

- **作業ディレクトリ**: `C:\Users\sawas\.openclaw\skills\capability-evolver` のみ（git管理下）。ここ以外は書き換えない。
- **改変禁止パス（evolverコア）**: `src/`, `index.js`, `package.json`, `package-lock.json`, `assets/gep/genes.json`, `assets/gep/capsules.json`, `.env`, `run-evolver.cmd`。これらは人手レビュー対象。触れない。
  - 例外: `node index.js solidify` がこれらの監査ファイル（genes/capsules/events）を**自動更新**するのは許可。手動編集のみ禁止。
- **新スキル生成**: 許可。ただし作成先は evolver リポ配下 `skills/<name>/`（= `C:\Users\sawas\.openclaw\skills\capability-evolver\skills\<name>\`）に限定。最低 `index.js` + `SKILL.md` + `package.json` を含め、`node -e "require('./skills/<name>')"` でimport検証すること。
- **ブラスト半径上限**: 20ファイル / 5000行。超える見込みなら適用せず中止・報告。
- **EVOLVE_ALLOW_SELF_MODIFY=false** を尊重（evolver自身のロジックは進化対象外）。

## 手順

### Step 1: スナップショット（ロールバック点）

PowerShellツールで以下を実行する:
```powershell
Set-Location 'C:\Users\sawas\.openclaw\skills\capability-evolver'
git add -A
git commit -m "evolve: pre-cycle snapshot" --allow-empty
git rev-parse HEAD   # → これを SNAPSHOT として記憶
```

### Step 2: 進化プロンプト生成

PowerShellツールで実行:
```powershell
Set-Location 'C:\Users\sawas\.openclaw\skills\capability-evolver'
node index.js run
```
- 生成された最新プロンプトを特定: `C:\Users\sawas\.openclaw\memory\evolution\gep_prompt_*.txt` のうち最終更新が最新のもの。Readで全文を読む。

### Step 3: パッチ適用
- GEPプロンプトの指示（Mutation→PersonalityState→EvolutionEvent→Gene→Capsule の5オブジェクトモデル、選択されたGene/戦略、blast radius制約）に従う。
- **最小・可逆**な変更を Edit / Write で適用する。上記「改変禁止パス」には一切触れない。
- 直近8サイクル履歴と同じ intent+signal+gene の繰り返しは避ける（プロンプト内の指示に従う）。

### Step 4: 検証（必須ゲート）
- プロンプト／選択Geneの `validation` 配列のコマンドをPowerShellツールで実行（例: `node -e "require('./src/evolve'); require('./src/gep/solidify'); console.log('ok')"`）。
- 新スキルを作った場合は `node -e "const s=require('./skills/<name>'); console.log(Object.keys(s))"` もPowerShellツールで実行。
- **すべて成功** したら Step 5。1つでも失敗、または途中で例外 → Step 6（ロールバック）。

### Step 5: 固化＆コミット（成功時）

PowerShellツールで実行:
```powershell
Set-Location 'C:\Users\sawas\.openclaw\skills\capability-evolver'
node index.js solidify
git add -A
git commit -m "evolve: <intent> <短い要約>"
```

### Step 6: ロールバック（失敗時）

PowerShellツールで実行:
```powershell
Set-Location 'C:\Users\sawas\.openclaw\skills\capability-evolver'
git reset --hard <SNAPSHOT>
git clean -fd skills
```
- 結果は FAILED として報告。

### Step 7: 報告（成否いずれでも必須）
Discordへ1行で報告（cron delivery=announce が本文を配信する）。フォーマット:
```
[capability-evolver-apply] result=SUCCESS|FAILED | intent=REPAIR|OPTIMIZE|INNOVATION | files=N lines=N | summary=<実際の変更内容を具体的に1文>
```
- 「完了しました」等の汎用文は禁止。何をどう変えたか具体的に書く。

## 失敗・例外時の最終保証
どのStepで失敗しても、必ず `git reset --hard <SNAPSHOT>`（取得済みなら）を試み、FAILED理由を添えて報告メッセージを返してセッションを終了する。沈黙終了は禁止。
