from flask import Flask

# Import blueprints
from routes.ai_routes import ai_routes
from routes.recommend_routes import recommend_bp

app = Flask(__name__)

# ✅ Register blueprints with prefix
app.register_blueprint(ai_routes, url_prefix="/ai")
app.register_blueprint(recommend_bp, url_prefix="/ai")

# ✅ Health check route
@app.route("/")
def home():
    return {"message": "AI Service is running 🚀"}

# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)