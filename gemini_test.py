from google import genai

# Replace with the API key your TA will give you
API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

prompt = """
Extract symptoms and possible diagnosis from this clinical note:

Patient reports persistent fatigue, low mood, and difficulty sleeping for two months.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print(response.text)
