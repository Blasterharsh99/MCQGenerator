Gemini_API = 'AIzaSyBH1sCJQnppP-PxGbfoKeCyVm2huottElA'
import google.generativeai as genai
import os

genai.configure(api_key=Gemini_API)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('What are you?')
print(response.text)