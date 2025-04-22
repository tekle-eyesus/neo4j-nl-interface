from app.query_handler import Neo4jQueryHandler
from app.llm_utils import generate_cypher, generate_explanation

def handle_user_input(user_input: str):
    cypher_query = generate_cypher(user_input)

    db = Neo4jQueryHandler()
    result = db.run_query(cypher_query)
    db.close()

    explanation = generate_explanation(cypher_query, str(result))
    return {
        "cypher_query": cypher_query,
        "result": result,
        "explanation": explanation
    }
