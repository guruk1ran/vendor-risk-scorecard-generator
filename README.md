# Vendor Risk Scorecard Generator

📌 Project Overview
This project is an AI-powered system to generate vendor risk scorecards.
It evaluates vendor data and provides risk insights using AI services.

## Tech Stack
* Python (Flask)
* AI Integration (Groq API - upcoming)
* REST APIs

## 📁 Folder Structure

ai-service/
  ├── routes/        # API routes
  ├── services/      # Business logic
  ├── prompts/       # AI prompt templates
  ├── app.py         # Main Flask app
  ├── requirements.txt
  ├── Dockerfile
```

## 🚀 Setup Instructions

1. Clone the repository:

git clone <repo-url>
cd vendor-risk-scorecard-generator/ai-service

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
python app.py

4. Open browser:
http://127.0.0.1:5000/

## ✅ Current Status (Day 1)

* Flask app setup completed
* Basic route working
* Folder structure created



## 🚀 Day 2 – Prompt Engineering

### 📌 Task Completed
- Designed primary prompt template for vendor risk analysis
- Implemented structured input format using placeholders
- Defined strict JSON output format

### 🧪 Testing
- Tested prompt with 5 real-world vendor inputs
- Verified outputs for:
  - Risk level classification (Low / Medium / High)
  - Logical reasoning
  - Meaningful recommendations

### ⚙️ Improvements Made
- Added strict rule-based logic for consistency:
  - No compliance → High risk
  - Fraud/Data leak → High risk
  - Strong compliance (ISO/SOC2/HIPAA) + no incidents → Low risk
  - Compliance + incidents → Medium risk
- Introduced rule priority (incidents override compliance)
- Ensured deterministic output (temperature = 0)

### ✅ Final Outcome
- All 5 test cases produce consistent and logical results
- Output strictly follows JSON format
- Prompt behavior is stable and predictable

### 📁 Files Created
- `prompts/vendor_prompt.txt`
- `services/prompt_loader.py`
- `test_prompt.py`





