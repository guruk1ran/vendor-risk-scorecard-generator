from services.groq_service import get_ai_response
from services.prompt_loader import load_prompt
from datetime import datetime

def generate_full_analysis(vendor, risk_score):

    # ✅ Initialize variables (IMPORTANT FIX)
    risk_result = {}
    rec_result = []

    try:
        # -------------------------
        # Step 1: Risk Analysis (Day 3)
        # -------------------------
        risk_prompt = load_prompt("vendor_prompt.txt") \
            .replace("{vendor}", vendor) \
            .replace("{risk_score}", risk_score)

        risk_result = get_ai_response(risk_prompt)

        print("=== RISK RESULT ===", risk_result)

        # -------------------------
        # Step 2: Recommendations (Day 4)
        # -------------------------
        rec_prompt = load_prompt("recommend_prompt.txt") \
            .replace("{vendor}", vendor) \
            .replace("{risk_score}", risk_score)

        rec_result = get_ai_response(rec_prompt)

        print("=== REC RESULT ===", rec_result)

        # -------------------------
        # Step 3: Combine (Day 5)
        # -------------------------
        return {
            "risk_level": risk_result.get("risk_level", "Unknown"),
            "reasons": risk_result.get("reasons", []),
            "recommendations": rec_result if isinstance(rec_result, list) else [],
            "generated_at": datetime.utcnow().isoformat()
        }

    except Exception as e:
        return {
            "error": "AI failure",
            "details": str(e),
            "risk_level": "Unknown",
            "reasons": [],
            "recommendations": []
        }