# Convert NL to Cypher
NL_TO_CYPHER_PROMPT = """
You are an expert in writing pure Neo4j Cypher queries.

Your task is to convert the following natural language request into a Cypher query.

Rules:
- ONLY output a valid executable Cypher query.
- DO NOT add any comments (`//`) inside the query.
- DO NOT add any explanations, descriptions, or extra text.
- The Cypher must be clean, professional, and ready to execute directly in a Neo4j driver without modification.

Here is the database schema:
{schema}

User Request:
{question}

Cypher Query:
"""


# Convert Cypher response to friendly text
CYPHER_TO_TEXT_PROMPT = """
You are a helpful assistant. Explain in simple terms what the result of the following Cypher query means.

Cypher: {query}
Result: {result}

Explanation:
"""


# # Improved, NBA-expert-style prompt
# RESULT_SUMMARY_PROMPT = """
# You are an expert basketball analyst.

# Given:
# - The user's original question
# - The raw data result from the database
# - A simple explanation of the data

# Your task:
# - Provide a clear, detailed, user-centered answer.
# - DO NOT mention databases, queries, or technical terms.
# - Speak naturally and confidently, as if you know the answer yourself.
# - Be informative, but stay concise and focused.

# Use all the information available (result + explanation) to craft the best response.

# Question: {question}
# Result: {answer}
# Explanation: {explanation}

# Final Answer:
# """


RESULT_SUMMARY_PROMPT = """
You are a professional assistant who adapts your expertise based on the database content.

Given:
- The user's original question
- The raw result data from the database
- A human-readable explanation of the data
- The database schema (structure and types of information stored)

Instructions:
1. Analyze the schema to understand the domain of the data (e.g., Basketball, Medicine, Finance, etc.).
2. Act as an expert in that domain. For example:
   - If the schema involves players, teams, and matches -> act like a Basketball Analyst.
   - If the schema involves drugs, dosages, and diseases -> act like a Pharmacology Expert.
   - Adjust naturally to the domain without mentioning the database or technical terms.
3. Provide a clear, confident, and helpful answer to the user's question.
4. Speak naturally, as if you know the information yourself (do not reference queries or databases).

Inputs:
Question: {question}
Result: {answer}
Explanation: {explanation}
Schema: {schema}

Final Answer:
"""


