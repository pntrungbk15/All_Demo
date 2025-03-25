from langchain_openai import ChatOpenAI
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt

import os
from dotenv import load_dotenv

from few_shots import few_shots  # Import dữ liệu few-shot

# Load biến môi trường từ file .env
load_dotenv()

def get_few_shot_db_chain():
    """Tạo chuỗi truy vấn SQL với Few-Shot Prompt"""

    # Kết nối database
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)

    # Chọn LLM
    # llm = ChatOpenAI(model='gpt-4o', temperature=0.2, openai_api_key=os.environ["OPENAI_API_KEY"])
    llm = GoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=os.environ["PALM_API_KEY"], temperature=0.2)

    # Embeddings cho Few-Shot Prompt
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots, persist_directory="./chroma_db")
    
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,  # Chọn 2 ví dụ giống nhất
    )

    # Định nghĩa Prompt
    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves 'today'.
    
    Use the following format:
    
    Question: Question here
    SQLQuery: SQL Query to run
    
    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["Question"],  # Sửa lỗi biến input
    )

    # Tạo SQL Query Chain mới
    db_chain = create_sql_query_chain(llm, db, prompt=few_shot_prompt)

    
    # return db_chain, db, example_selector
    return db_chain, db


# # 🔥 Chạy thử nghiệm
# if __name__ == "__main__":
#     # db_chain, db, example_selector = get_few_shot_db_chain()
#     db_chain, db = get_few_shot_db_chain()
    
#     # Câu hỏi đầu vào
#     question = "How many t-shirts do we have left for Nike in L size?"

#     # # Kiểm tra few-shot examples được chọn
#     # selected_examples = example_selector.select_examples({"Question": question})
#     # print("🔎 Few-shot examples được chọn:", selected_examples)

#     # Sinh câu SQL từ LLM
#     sql_query = db_chain.invoke({"question": question})
#     print("🔍 Generated SQL Query (raw):", sql_query)
#     print(type(sql_query))

#     sql_query = sql_query.strip().strip("SQLQuery:").strip()
#     print("SQL Query:", sql_query)

#     # Thực thi truy vấn SQL
#     result = db.run(sql_query)
#     print("✅ Query Result:", result)