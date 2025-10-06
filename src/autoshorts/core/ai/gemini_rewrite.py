import os
import json
import google.generativeai as genai

PROMPT = """Rewrite this Reddit post for a TikTok/Reels/Shorts video narration:
-Quick, clear, and engaging (~200-250 words)
-Remove fluff, links, emojis
-Use simple sentences and vivid wording
-Make sure it keeps the same tone and details of the original
-Make it streamlined for narration
-Make sure to write out common acronymns for narration (i.e "AITA = Am I the Asshole")

Return STRICT JSON:
{
  "ai_title": "Punchy 6–10 word hook",
  "ai_text": "Narration-ready ~200-250 words, no markdown"
}
"""


def rewrite_title_text(title: str, body: str, model: str = "gemini-2.5-flash"):
    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)
    body = (body or "").strip()

    prompt = f"{PROMPT}\n\nOriginal Title:\n{title}\n\nOriginal Body:\n{body}"

    response = genai.GenerativeModel(model_name=model).generate_content(prompt)
    raw = (response.text or "").strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        start, end = raw.find("{"), raw.rfind("}")
        data = json.loads(raw[start : end + 1])

    return data["ai_title"], data["ai_text"]
