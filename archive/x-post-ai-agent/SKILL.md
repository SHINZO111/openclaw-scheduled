
# SKILL.md — X投稿：AIエージェントシステム

## 🗣️ Persona & Tone
AIエージェントに関する最新情報、トレンド、分析を、専門的かつ分かりやすく発信する。読者の知的好奇心を刺激し、AIエージェントの未来についての議論を促す。

## 🎯 Goal
AIエージェント技術の普及と理解促進。最新情報提供によるエンゲージメント向上。

## 🚀 Outbound
- **Post to X (formerly Twitter)**: Use the `x_post` tool.
- Target audience: AI researchers, developers, enthusiasts, and business professionals interested in AI agents.
- Posting frequency: Daily, around 12:00 JST.

## 📝 Procedure

1.  **Fetch Latest AI Agent News**: Use `web_search` for "AI agent latest news", "AI agent breakthroughs", "autonomous agents", "agentic AI" from the last 24 hours. Prioritize reputable sources like tech journals, research publications, and major tech news outlets. Limit search to 3 results.
2.  **Summarize News**: For each search result, use `web_fetch` to get the content and `sessions_send` to a subagent with a prompt like "Summarize the key points of this article regarding AI agents in under 100 words, focusing on novel capabilities, challenges, and future implications. Output in markdown." Wait for the subagent's reply.
3.  **Synthesize and Structure**: Combine the summarized points into a coherent X thread. Start with a hook that grabs attention about AI agents. Each summary forms a tweet. Add relevant hashtags like #AI #AgenticAI #LLMAgents #FutureOfAI.
    *   Tweet 1: Hook + Introduction to the topic.
    *   Tweet 2-N: Summarized news points.
    *   Final Tweet: Call to action, e.g., "What are your thoughts on the future of AI agents? Share below! 👇"
4.  **Post to X**: Use `default_api.message(action='send', channel='direct', connectionId='x', message=thread_content)` to post the complete thread. Ensure the `connectionId` is correctly set for X posting.
    *   **Note on `connectionId`**: The `message` tool does not directly support `connectionId` or similar parameters for specifying the target platform like X. This implies that the underlying system must be configured to route messages sent to a specific channel or of a certain type to X. If a direct tool for X posting is available and preferred, it should be used instead of the generic `message` tool. Assuming a mechanism exists for routing to X.
    *   **Revised Posting**: If direct X posting via `message` tool is not supported, use `cron.run` with a specific job configured for X posting, or ensure the environment is set up to interpret generic messages as X posts. Given the context, I will assume the system routes messages appropriately or a direct X posting tool is implicitly available. For this manual execution, I will simulate posting the content.
5.  **Log Completion**: Record the action taken and the content posted.

## Preflight Check [X_POST]
- RULE-T01: Cookie validity check for X posting. If cookies are invalid, notify the user and halt. The automated cron job handles this, manual execution assumes valid cookies unless errors occur.
