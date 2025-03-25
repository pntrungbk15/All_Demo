import streamlit as st

from langchain_community.document_loaders import WebBaseLoader
from chain import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm: Chain, portfolio: Portfolio, clean_text):
    st.title("📧 Mail Generator")
    url_input = st.text_input("Enter a URL: ", value="https://careers.nike.com/en/senior-lead-technology-service-management/job/R-50101")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job['skills']
                links = portfolio.query_links(skills)
                email = llm.write_email(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f'An error occurred: {e}')


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio("app_1/resource/my_portfolio.csv")
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)