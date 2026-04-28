from flask import Blueprint

ai_routes = Blueprint("ai_routes", __name__)

@ai_routes.route("/test", methods=["GET"])
def test():
    return {"message": "AI route working"}