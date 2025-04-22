from neo4j import GraphDatabase
from config.settings import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class Neo4jQueryHandler:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def run_query(self, cypher_query: str):
        with self.driver.session() as session:
            result = session.run(cypher_query)
            return [record.data() for record in result]

    def close(self):
        self.driver.close()
