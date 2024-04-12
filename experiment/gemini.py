<<<<<<< HEAD
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
load_dotenv()
key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-pro")
=======
import google.generativeai as genai
import os
from dotenv import load_dotenv()
load_dotenv()
Gemini_API = os.getenv(GOOGLE_API_KEY)
genai.configure(api_key=Gemini_API)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('What are you?')
print(response.text)
>>>>>>> 560c58cabefd08f6339a47a2e361103e743e44b0
