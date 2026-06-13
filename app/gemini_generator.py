from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

prompt = """
Generate 10 indian customer records.
Use ONLY these fields:

- customer_id
- name
- age
- email

Rules:
- Customer_id should start from 1
- Age between 18 and 60
- Gmail addresses only

Return JSON only.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)

with open(
    "outputs/gemini_generated_data.json",
    "w"
) as file:

    file.write(response.text)

print("JSON file created successfully")

import json
import pandas as pd

# Convert Gemini response to Python list
clean_text = response.text

clean_text = clean_text.replace("```json", "")
clean_text = clean_text.replace("```", "")
clean_text = clean_text.strip()

data = json.loads(clean_text)

# Create CSV
df = pd.DataFrame(data)

df.to_csv(
    "outputs/gemini_generated_data.csv",
    index=False
)

print("CSV file created successfully")