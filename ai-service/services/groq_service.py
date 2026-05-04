import json
import re
from groq import Groq
import os
import time
from services.health_service import record_response_time
from services.cache_service import get_cache, set_cache, generate_key
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt, vendor, risk_score):
    try:
        # 🔑 STEP 1: Generate cache key
        cache_key = generate_key(vendor, risk_score)

        # ⚡ STEP 2: Check Redis cache
        cached = get_cache(cache_key)
        if cached:
            return cached

        print("🚀 CALLING AI")

        # ⏱ STEP 3: Track response time
        start = time.time()

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        end = time.time()
        record_response_time(end - start)

        content = response.choices[0].message.content
        print("\n=== RAW AI RESPONSE ===\n", content)

        # ✅ STEP 4: Extract JSON
        json_match = re.search(r'(\{.*\}|\[.*\])', content, re.DOTALL)

        if not json_match:
            raise ValueError("No JSON found in AI response")

        json_text = json_match.group()

        # ✅ STEP 5: Clean JSON
        json_text = json_text.replace("\n", " ")
        json_text = re.sub(r',\s*}', '}', json_text)
        json_text = re.sub(r',\s*]', ']', json_text)

        print("\n=== CLEAN JSON ===\n", json_text)

        # ✅ STEP 6: Convert to Python
        parsed = json.loads(json_text)

        # 🔥 STEP 7: Store in Redis
        set_cache(cache_key, parsed)

        # ✅ STEP 8: Return result
        if isinstance(parsed, dict):
            return parsed
        elif isinstance(parsed, list):
            return parsed
        else:
            raise ValueError("Unexpected JSON format")

    except Exception as e:
        print("\n=== ERROR ===\n", str(e))

        # ✅ Fallback response
        return [
            {
                "action_type": "Review",
                "description": "AI response invalid, fallback triggered",
                "priority": "Medium"
            }
        ]