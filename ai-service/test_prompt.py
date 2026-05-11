from groq import Groq
from services.prompt_loader import load_prompt
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt_template = load_prompt()

def generate_prompt(data):
    return prompt_template.format(**data)

# 5 REAL TEST INPUTS
test_inputs = [
    {
        "vendor_name": "ABC Corp",
        "country": "India",
        "industry": "Finance",
        "revenue": "10M",
        "compliance": "ISO27001",
        "incidents": "None"
    },
    {
        "vendor_name": "XYZ Ltd",
        "country": "Unknown",
        "industry": "Crypto",
        "revenue": "2M",
        "compliance": "None",
        "incidents": "Fraud reported"
    },
    {
        "vendor_name": "SecureTech",
        "country": "USA",
        "industry": "Cybersecurity",
        "revenue": "50M",
        "compliance": "SOC2",
        "incidents": "Minor breach"
    },
    {
        "vendor_name": "FastLogix",
        "country": "China",
        "industry": "Logistics",
        "revenue": "5M",
        "compliance": "Partial",
        "incidents": "Delayed shipments"
    },
    {
        "vendor_name": "HealthPlus",
        "country": "UK",
        "industry": "Healthcare",
        "revenue": "20M",
        "compliance": "HIPAA",
        "incidents": "Data leak"
    }
]

for i, data in enumerate(test_inputs):
    print(f"\n--- Test Case {i+1} ---")

    prompt = generate_prompt(data)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    print(response.choices[0].message.content)