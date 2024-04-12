import google.generativeai as genai
import os
from dotenv import load_dotenv()
load_dotenv()
Gemini_API = os.getenv(GOOGLE_API_KEY)
genai.configure(api_key=Gemini_API)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('What are you?')
print(response.text)
