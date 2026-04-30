# Vendor Risk Scorecard Generator – AI Service

## 📌 Overview
This AI service analyzes vendor risk based on input data and generates structured insights using AI.

## 👩‍💻 Role

**AI Developer 1**

Responsible for:
* Prompt design
* API development
* AI integration
* Structured response generation

## Work Summary

### ✅ Day 1

* Setup Flask project structure
* Created folders: `routes/`, `services/`, `prompts/`
* Configured `app.py` entry point
* Added dependencies (`requirements.txt`)

### ✅ Day 2

* Designed and refined prompt template
* Tested with multiple real inputs
* Ensured consistent AI outputs

### ✅ Day 3

* Implemented POST API: `/ai/describe`
* Features:
  * Input validation
  * Prompt loading
  * Groq AI integration
  * Structured JSON response

## API Endpoint

### POST `/ai/describe`

### Request
json
{
  "vendor_name": "ABC Corp",
  "country": "India",
  "industry": "Finance",
  "revenue": "10M",
  "compliance": "ISO27001",
  "incidents": "None"
}

### Response

json
{
  "risk_level": "Low",
  "reasons": "Compliance status is ISO27001 and no past incidents",
  "recommendations": [
    {
      "desc": "Perform regular audits",
      "status": "Recommended"
    }
  ],
  "generated_at": "auto"
}

## Tech Stack
* Python
* Flask
* Groq API
* Postman

## Testing
Tested using Postman:

http://127.0.0.1:5000/ai/describe


