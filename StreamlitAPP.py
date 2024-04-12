import os 
import json 
import traceback
import pandas as pd
import streamlit as st 
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

load_dotenv()

with open(r'Response.json','r') as file:
    RESPONSE_JSON = json.load(file)

st.title('MCQs Generating Application')

with st.form("user_inputs"):
    upload_file = st.file_uploader("Upload PDF or text material")
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=15)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity level of questions", max_chars=20, placeholder='Simple')
    button = st.form_submit_button('Create MCQs')

    if button:
        with st.spinner('loading...'):
            try:
                text = read_file(upload_file)
                response = generate_evaluate_chain.invoke({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                })
                
                if isinstance(response, dict):
                    quiz = response.get('quiz', None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index += 1
                            st.table(df)
                            st.text_area(label='Review', value=response['review'])
                        else:
                            st.error('Error in table data')
                    else:
                        st.write(response)
                else:
                    st.error('Error: Response is not a dictionary')
                    
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

