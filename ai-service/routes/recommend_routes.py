from flask import Blueprint, request, jsonify
from services.groq_service import get_ai_response
from services.prompt_loader import load_prompt

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/ai/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json

        if not data or 'vendor' not in data:
            return jsonify({"error": "Vendor input required"}), 400

        vendor = data['vendor']
        risk_score = data.get('risk_score', 'Unknown')

        # ✅ Load prompt from file
        template = load_prompt("recommend_prompt.txt")

        # ✅ Fill dynamic values
        prompt = template.format(
            vendor=vendor,
            risk_score=risk_score
        )

        # Call AI
        result = get_ai_response(prompt)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500