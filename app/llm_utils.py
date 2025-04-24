# from langchain.llms import LlamaCpp
from langchain_community.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from config.settings import LLAMA_MODEL_PATH
from models.prompt_templates import NL_TO_CYPHER_PROMPT, CYPHER_TO_TEXT_PROMPT, RESULT_SUMMARY_PROMPT


def load_llama():
    return LlamaCpp(
        model_path=LLAMA_MODEL_PATH,
        temperature=0.1,
        max_tokens=512
    )

llm = load_llama()

def generate_cypher(question: str, schema: str):
    prompt = PromptTemplate.from_template(NL_TO_CYPHER_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"question": question, "schema": schema})


def generate_explanation(query: str, result: str):
    prompt = PromptTemplate.from_template(CYPHER_TO_TEXT_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"query": query, "result": result})


def generate_answer(question: str, result: str):
    prompt = PromptTemplate.from_template(RESULT_SUMMARY_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"question": question, "answer": result})

