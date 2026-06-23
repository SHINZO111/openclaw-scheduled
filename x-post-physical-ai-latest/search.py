import os
import json
from datetime import datetime, timedelta
from anthropic import Anthropic

def search_brave(query, time_range="48h"):
    """Brave Searchで検索"""
    client = Anthropic(api_key=os.environ.get("BRAVE_API_KEY"))

    messages = [
        {
            "role": "user",
            "content": f"""Search for {query} news from the last {time_range}.

Return ONLY a JSON array of up to 20 relevant news items with the following structure:
[
  {{
    "title": "News title",
    "url": "Article URL",
    "snippet": "Brief description",
    "publishedAt": "ISO timestamp"
  }}
]

Requirements:
- Focus on robotics, physical AI, humanoid robots, Boston Dynamics, Tesla Optimus, autonomous robots
- Only include recent news (last {time_range})
- Return URLs only if they are actual news articles (not social media, blog posts, or other non-news content)
- Prioritize major news outlets and tech publications"""
        }
    ]

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=messages
    )

    content = response.content[0].text
    # Extract JSON from response
    import re
    json_match = re.search(r'\[[\s\S]*\]', content)
    if json_match:
        return json.loads(json_match.group())
    return []

if __name__ == "__main__":
    query = 'robotics AI 2026 OR humanoid robot OR Boston Dynamics Tesla robot OR フィジカルAI ロボット OR 自律ロボット 最新'
    results = search_brave(query, "48h")
    print(json.dumps(results, ensure_ascii=False, indent=2))
