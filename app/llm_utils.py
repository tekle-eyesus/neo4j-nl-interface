from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from models.prompt_templates import NL_TO_CYPHER_PROMPT, CYPHER_TO_TEXT_PROMPT, RESULT_SUMMARY_PROMPT
import os
from dotenv import load_dotenv

load_dotenv() 

# load the Gemini Model
def load_gemini():
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", 
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

llm = load_gemini()

def generate_cypher(question: str, schema: str):
    prompt = PromptTemplate.from_template(NL_TO_CYPHER_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"question": question, "schema": schema})

def generate_explanation(query: str, result: str):
    prompt = PromptTemplate.from_template(CYPHER_TO_TEXT_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"query": query, "result": result})

def generate_answer(question: str, result: str, explanation:str, schema:str):
    prompt = PromptTemplate.from_template(RESULT_SUMMARY_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"question": question, "answer": result, "explanation":explanation,"schema": schema})
