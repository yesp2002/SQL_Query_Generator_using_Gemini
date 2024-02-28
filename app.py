from dotenv import load_dotenv
load_dotenv() ##Load all environmental variables

import streamlit as st 
import os
import sqlite3

import google.generativeai as genai

## Configure our API key 

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


#Function to load Google Gemini Model and provide query as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt[0] + question)
    return response.text

## Function to retrieve query from the sql database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    """You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the studenst studying in Data Scinece class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS = "Data Science";
    also the sql code should not have ''' in beginning or end and sql word in the output. Here is the question: \n
    """
]

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


st.set_page_config(page_title = "I can Retrieve any SQL query")
st.header("Gemini App to Retrieve SQL data")

question = st.text_input("Input :", key = "input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    st.write("SQL Query : "+ response)
    data = read_sql_query(response, "student.db")
    print(data)
    for row in data:
       st.write(row)
    