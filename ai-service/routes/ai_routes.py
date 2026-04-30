import json
from flask import Blueprint, request, jsonify
from services.prompt_loader import load_prompt

ai_routes = Blueprint("ai_routes", __name__)

# ✅ Test route
@ai_routes.route("/test", methods=["GET"])
def test():
    return {"message": "AI route working"}


# ✅ ADD THIS
@ai_routes.route('/describe', methods=['POST'])
def describe_vendor():
    data = request.get_json()

    # 1. Validate input
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    vendor_name = data.get("vendor_name")
    compliance = data.get("compliance")
    incidents = data.get("incidents")
    country = data.get("country", "Unknown")
    industry = data.get("industry", "Unknown")
    revenue = data.get("revenue", "Unknown")

    if not vendor_name:
        return jsonify({"error": "vendor_name is required"}), 400

    # 2. Load prompt
    prompt_template = load_prompt()

    # 3. Prepare prompt
    final_prompt = prompt_template.format(
    vendor_name=vendor_name,
    country=country,
    industry=industry,
    revenue=revenue,
    compliance=compliance,
    incidents=incidents
)

    # 4. Call Groq
    from services.groq_service import call_groq
    response = call_groq(final_prompt)

    # 5. Return response
    try:
        parsed_response = json.loads(response)
    except:
        parsed_response = {
        "risk_level": "Unknown",
        "reasons": response,
        "recommendations": "Parsing failed"
    }
    return jsonify({
    "risk_level": parsed_response.get("risk_level"),
    "reasons": parsed_response.get("reasons"),
    "recommendations": parsed_response.get("recommendations"),
    "generated_at": "auto"
})
