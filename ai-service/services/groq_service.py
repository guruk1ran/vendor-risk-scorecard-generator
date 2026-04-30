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

        # ✅ Step 1: Try direct JSON parse
        try:
            return json.loads(content)
        except:
            pass

        # ✅ Step 2: Extract JSON array safely
        json_match = re.search(r'\[.*\]', content, re.DOTALL)

        if json_match:
            json_text = json_match.group()

            # Clean formatting
            json_text = json_match.group()
            # remove new lines
            json_text = json_text.replace("\n", " ").replace("\r", "")

            # remove trailing commas
            json_text = re.sub(r',\s*}', '}', json_text)
            json_text = re.sub(r',\s*]', ']', json_text)

            print("=== CLEAN JSON ===")
            print(json_text)

        try:
            return json.loads(json_text)
        except Exception as e:
            print("JSON PARSE ERROR:", e)
            return [
            {
            "action_type": "Fix",
            "description": "AI returned invalid JSON, fallback triggered",
            "priority": "Medium"
            }
         ]

    except Exception as e:
        return {
            "error": "AI failure",
            "details": str(e)
        }