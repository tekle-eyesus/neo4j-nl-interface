# Convert NL to Cypher
NL_TO_CYPHER_PROMPT = """
You are an expert in Neo4j Cypher. Convert the following natural language request into a Cypher query.

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
