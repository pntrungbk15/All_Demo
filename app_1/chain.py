import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text: str):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke({"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
            return res if isinstance(res, list) else [res]
        except OutputParserException:
            raise OutputParserException(
                "Context too bif. Unable to parse jobs.")

    def write_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are {your_name}, a skilled AI & Software Engineer specializing in {your_specializations}. 
            With extensive experience in {your_key_experiences}, you have successfully developed and deployed 
            AI-driven solutions, optimizing business operations and enhancing efficiency. 

            Your job is to write a cold email to the client regarding the job mentioned above, describing how your expertise 
            aligns with their needs. Highlight your technical skills, past projects, and how you can contribute to their objectives. 
            Also, include the most relevant ones from the following links to showcase your portfolio: {link_list}.

            Remember, you are {your_name}, an AI & Software Engineer.  
            Do not provide a preamble.

            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": job, "your_name": "Phạm Ngọc Trung",
                                 "your_specializations": "New Ocean Group", "your_key_experiences": "4 years.", "link_list": links})
        return res.content


if __name__ == "__main__":
    chain = Chain()