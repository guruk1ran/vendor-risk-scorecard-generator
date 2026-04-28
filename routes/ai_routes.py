from flask import Blueprint, request

ai_routes = Blueprint("ai_routes", __name__)

@ai_routes.route("/test-prompt", methods=["POST"])
def test_prompt():
    data = request.json

    with open("prompts/prompt.txt", "r") as file:
        prompt = file.read()

    final_prompt = prompt.format(
        vendor_name=data.get("vendor_name"),
        location=data.get("location"),
        issues=data.get("issues"),
        compliance=data.get("compliance")
    )

    return {"generated_prompt": final_prompt}