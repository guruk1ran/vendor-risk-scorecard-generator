from flask import Flask
from routes.ai_routes import ai_routes

app = Flask(__name__)

app.register_blueprint(ai_routes, url_prefix="/ai")

@app.route("/")
def home():
    return {"message": "AI Service is running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)