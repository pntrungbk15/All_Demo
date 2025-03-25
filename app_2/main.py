import streamlit as st

from langchain_help import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain, db = get_few_shot_db_chain()
    sql_query = chain.invoke({"question": question})

    sql_query = sql_query.strip().strip("SQLQuery:").strip()
    response = db.run(sql_query)
    st.header("Answer")
    st.write(response)
