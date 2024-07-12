from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import sqlite3

load_dotenv() # Import all environment variables

## COnfigure API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## FUnction to load Google Gemini Model and provide SQL Query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel(model_name='gemini-pro')
    response = model.generate_content([prompt, question]) 
    return response.text


## FUnction to retrieve query from the sql database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()

    for row in rows:
        print(row)
    return rows


## Define the prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS. 
    \n\nFor example, \nExample1- How many entries of records are present?, 
    the SQL command will be something like this- SELECT COUNT(*) FROM STUDENT ;
    \nExample2- Tell me all the student studying in Data Science class?,
    the SQL command will be something like this- SELECT * FROM STUDENT where CLASS="Data Science" ;
    also the SQL code should not have ''' in the beginning or end and sql word in the output.
    """
]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retreive SQL Data")

question = st.text_input("Input:",key="input")

submit = st.button("Ask the question")


## If submit is clicked
if submit:
    response = get_gemini_response(question, prompt[0])
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)



























