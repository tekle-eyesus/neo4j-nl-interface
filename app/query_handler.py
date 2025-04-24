from neo4j import GraphDatabase
from config.settings import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
import re


def clean_cypher_query(query: str) -> str:
    print("ROW QUERY \n",query)
    # Remove triple backticks at start/end (if any)
    query = re.sub(r"^```|```$", "", query.strip())

    # Replace all line breaks with spaces
    query = query.replace('\n', ' ').replace('\r', ' ')

    # Collapse multiple spaces into one
    query = re.sub(r'\s+', ' ', query)

    # Remove trailing semicolon (optional but common)
    query = re.sub(r';\s*$', '', query)
    print("CLEANED CYPHER \n",query.strip())  # AFTER THE CYPHER CLEANED
    return query.strip()


class Neo4jQueryHandler:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def run_query(self, cypher_query: str):
        with self.driver.session() as session:
            cleaned_query = clean_cypher_query(cypher_query)
            result = session.run(cleaned_query)
            return [record.data() for record in result] # return the result as list

    def close(self):
        self.driver.close()
