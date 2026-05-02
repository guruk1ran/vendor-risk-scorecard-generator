from services.groq_service import get_ai_response
from services.prompt_loader import load_prompt
from datetime import datetime

def generate_report(vendor, risk_score):
    try:
        prompt = load_prompt("report_prompt.txt") \
            .replace("{vendor}", vendor) \
            .replace("{risk_score}", risk_score)

        result = get_ai_response(prompt)

        if not isinstance(result, dict):
            result = {}

        # Normalize fields (ensure lists/dicts)
        key_items = result.get("key_items", [])
        if not isinstance(key_items, list):
            key_items = []

        recs = result.get("recommendations", [])
        if not isinstance(recs, list):
            recs = []

        # 🔥 FINAL NORMALIZED RESPONSE (ORDER FIXED)
        response = {
            "title": result.get("title", "Vendor Risk Report"),
            "summary": result.get("summary", ""),
            "overview": result.get("overview", ""),
            "key_items": key_items,
            "recommendations": recs
        }

        return response

    except Exception as e:
        return {
            "error": "Report generation failed",
            "details": str(e),
            "title": "",
            "summary": "",
            "overview": "",
            "key_items": [],
            "recommendations": []
        }