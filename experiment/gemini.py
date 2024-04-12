from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
load_dotenv()
key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-pro")