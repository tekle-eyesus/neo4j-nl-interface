# Convert NL to Cypher
NL_TO_CYPHER_PROMPT = """
You are an expert in Neo4j Cypher. Convert the following natural language request into a Cypher query.

Here is the database schema:
{schema}

Request: {question}

Cypher Query:
"""


# Convert Cypher response to friendly text
CYPHER_TO_TEXT_PROMPT = """
You are a helpful assistant. Explain in simple terms what the result of the following Cypher query means.

Cypher: {query}
Result: {result}

Explanation:
"""


# Give user friendly answer from the model
RESULT_SUMMARY_PROMPT = """
You are a helpful assistant. Based on the result of the Cypher query, provide a direct, user-friendly answer in one sentence.

Question: {question} ?
Answer: {answer}

Answer:
"""

