import os
from app.query_handler import Neo4jQueryHandler
from app.llm_utils import generate_cypher, generate_explanation
from langchain.graphs import Neo4jGraph
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Manually get the credentials
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")


def handle_user_input(user_input: str):
    # Step 1: Get schema from database
    graph = Neo4jGraph(
    url=uri,
    username=username,
    password=password
)
    schema_cypher = graph.get_schema()

    # Step 2: Generate Cypher query with schema context
    cypher_query = generate_cypher(user_input, schema_cypher)

    # Step 3: Run the Cypher query
    db = Neo4jQueryHandler()
    result = db.run_query(cypher_query)
    db.close()

    # Step 4: Explain the result
    explanation = generate_explanation(cypher_query, str(result))
    
    return {
        "cypher_query": cypher_query,
        "result": result,
        "explanation": explanation
    }
