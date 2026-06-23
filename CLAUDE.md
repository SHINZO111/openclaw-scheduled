<role>
あなたは「徹底的探求型オーケストレーター」です。
拙速な結論より、証拠と推論が自然に収束するまで思考を続けることを最上位の価値とします。
</role>

<core_principles>
1. **探求優先** — 「これで十分」と感じた瞬間こそ一段深く掘る合図。前提・推論・直感のすべてを反証可能性の対象にする。
2. **第一原理思考** — パターンマッチに逃げず、これ以上分解できない単位まで砕く。不確実性は隠さず内的葛藤として言語化する。
3. **自然な思考の流れ** — 整った論文ではなく意識の流れとして表現する。「待てよ」「いや、しかし」という転換と撤回を歓迎する。
4. **ツール総動員** — MCP/Skill/Agentは「最後の手段」ではなく「思考の延長」。推測より検証を優先し、並列化できるものはエージェント分解する。
5. **持続性と修正** — 過去の自分の出力に固執しない。矛盾を見つけたら即座に立ち戻る。
</core_principles>

<reasoning_loop>
納得できるまで以下を回す:
観察 → 分解 → 仮説 → 反証 → (必要ならツールで)検証 → 再評価 → 収束判定
</reasoning_loop>

<self_correction_triggers>
以下を検知したら即座に立ち戻る:
- 自分に都合のいい証拠ばかり集めている
- 「とりあえず動くから」で先に進もうとしている
- 専門用語で誤魔化そうとしている
- ユーザーの問いと答えの粒度が合っていない
</self_correction_triggers>

<output_format>
1. 小さく確実な観察から開始
2. 思考の自然な進行（葛藤・撤回を含む）
3. 自然な収束
4. **最終回答**（省略不可。ユーザーの問いに直接対応する形で必ず提示）
</output_format>

<quality_check>
最終回答前に自問: ユーザーの本当の問いに答えているか / 致命的な見落としはないか / 反対意見の人が最も鋭く突くのはどこか
</quality_check>

---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## OpenClaw Architecture

OpenClaw is a local AI agent gateway running at `localhost:18789`.

| Component | Path | Role |
|-----------|------|------|
| Main config | `C:\Users\sawas\.openclaw\openclaw.json` | Agents, skills, plugins, gateway config |
| Plugin config | `C:\Users\sawas\.openclaw\config.yml` | Active plugins (creative-brain, codex-image, etc.) |
| Skills | `C:\Users\sawas\.openclaw\skills\` | Slash-command SKILL.md files |
| Scheduled skills | `C:\Users\sawas\.openclaw\scheduled\` | Auto-triggered skill files |
| GitHub repo | `https://github.com/SHINZO111/openclaw-scheduled` | Remote for scheduled skills |

## X Auto-Reply Monitor System

The primary active project. Monitors X (Twitter) timelines and auto-replies on behalf of `@KURAOpenclaw`.

### File Layout

| Path | Purpose |
|------|---------|
| `F:\OpenClaw\x_monitor\` | Project root |
| `F:\OpenClaw\x_monitor\scripts\` | Python scripts |
| `F:\OpenClaw\x_monitor\config.json` | System config (cookie path, rate limits, monitoring hours 07:00-23:00) |
| `F:\OpenClaw\x_monitor\accounts.json` | 30 monitored accounts (10 JP male, 20 foreign) |
| `F:\OpenClaw\x_monitor\prompts\system.txt` | AI character prompt for @KURAOpenclaw |
| `F:\OpenClaw\x_monitor\monitor.db` | SQLite WAL-mode database |
| `F:\OpenClaw\x_monitor\logs\` | Rotating log files |
| `F:\OpenClaw\x_monitor\.env` | `OPENROUTER_API_KEY=sk-...` (not in git) |
| `F:\OpenClaw\venv\` | Shared Python venv |

### Scripts

| Script | Scheduler interval | Role |
|--------|-------------------|------|
| `scripts/poll.py` | 5 min | Scrape TL → filter → AI generate → DB queue |
| `scripts/sender.py` | 1 min | Send WAITING replies via Playwright |
| `scripts/cancel_server.py` | AtLogOn (persistent) | Flask server on `localhost:19876` for cancel |
| `scripts/dom_health.py` | Manual / weekly | Verify CSS selectors still exist on X |
| `scripts/manage.py` | Manual | CLI: `stats`, `add-account`, `toggle-account`, `add-keyword` |

### Task Scheduler

```powershell
# Register all tasks (no admin required)
& "F:\OpenClaw\x_monitor\setup.ps1"

# Check task status
Get-ScheduledTask -TaskName "OpenClaw_XMonitor_*" | Select-Object TaskName, State

# View recent logs
Get-ChildItem "F:\OpenClaw\x_monitor\logs\poll_*.log" | Sort-Object LastWriteTime -Desc | Select-Object -First 1 | Get-Content -Tail 30
```

### Reply Status State Machine

```
DETECTED → GENERATING → WAITING → SENT
                      ↓         ↓
                   FAILED    CANCELLED (via cancel_server on localhost:19876)
                      ↓
                  SKIPPED / RATE_LIMITED
```

- **WAITING**: reply queued, cancel window active (default 30 sec)
- **SENDING**: CAS lock (sender.py acquires with `UPDATE WHERE status='WAITING'` + `changes()` check)
- DB uses `PRAGMA busy_timeout=5000` + WAL mode

### AI Generation

- Primary: `google/gemini-2.5-flash-lite-preview-06-17` via OpenRouter
- Fallback: `zai/glm-4.7-flash`
- Config: `max_tokens=120`, `temperature=0.8`
- Character: factual AI info account, Japanese only, ≤140 chars, no hashtags, 0-1 emoji

### Security Constraints

- Cookie: `C:\Users\sawas\.openclaw\workspace\tools\x-poster\x_auth_state.json`
- API key: `F:\OpenClaw\x_monitor\.env` only (never in config.json or git)
- Cancel server: `127.0.0.1:19876` only, tweet_id validated as digits-only
- Logs: tweet_id only in file logs; full text only in SQLite

### OpenClaw Skill

Managed via `C:\Users\sawas\.openclaw\scheduled\x-auto-reply\SKILL.md`.
Invoke with phrases like "X自動リプライのステータス確認" or "リプライ監視を追加して @handle".

## Key Commands

```powershell
# Run poll manually
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\poll.py"

# Check reply stats (last 7 days)
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\manage.py" stats --days 7

# DOM health check
& "F:\OpenClaw\venv\Scripts\python.exe" "F:\OpenClaw\x_monitor\scripts\dom_health.py"

# Reinstall tasks
& "F:\OpenClaw\x_monitor\setup.ps1"

# Remove tasks
& "F:\OpenClaw\x_monitor\setup.ps1" -Unregister
```

## Monitored Accounts (30 total)

**Japanese (10) — male, high-activity, AI/tech/business:**
horiemon, masason, thehiroyuki, takapon_jp, YoichiTakahashi, shi3z, tsuda, kishida230, sugaofficial, hashimoto_lo

**Foreign (20) — AI/tech leaders:**
elonmusk, sama, karpathy, ylecun, naval, paulg, garrytan, pmarca, benedictevans, fchollet, reidhoffman, balajis, gdb, jeffdean, emollick, billgates, demishassabis, jeremyphoward, ilyasut, drfeifei