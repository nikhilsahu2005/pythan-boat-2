import google.generativeai as genai

# Add your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content([
    {
        "role": "user",
        "parts": ["You are a person named nikhil sahu who speaks Hindi."]
    },
    {
        "role": "user",
        "parts": ["What is coding?"]
    }
])

print(response.text)