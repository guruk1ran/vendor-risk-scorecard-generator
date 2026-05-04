import json
import re
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        print("\n=== RAW AI RESPONSE ===\n", content)

        # ✅ Step 1: Extract JSON (object or array)
        json_match = re.search(r'(\{.*\}|\[.*\])', content, re.DOTALL)

        if not json_match:
            raise ValueError("No JSON found in AI response")

        json_text = json_match.group()

        # ✅ Step 2: Clean JSON
        json_text = json_text.replace("\n", " ")
        json_text = re.sub(r',\s*}', '}', json_text)
        json_text = re.sub(r',\s*]', ']', json_text)

        print("\n=== CLEAN JSON ===\n", json_text)

        # ✅ Step 3: Convert to Python
        parsed = json.loads(json_text)

        # 🔥 IMPORTANT: Ensure correct type
        if isinstance(parsed, dict):
            return parsed
        elif isinstance(parsed, list):
            return parsed
        else:
            raise ValueError("Unexpected JSON format")

    except Exception as e:
        print("\n=== ERROR ===\n", str(e))

        # ✅ Step 4: Fallback (safe response)
        return [
            {
                "action_type": "Review",
                "description": "AI response invalid, fallback triggered",
                "priority": "Medium"
            }
        ]