# Natural Language Interface to Neo4j

This project provides a conversational interface to query a Neo4j graph database using natural language. Built with **Gradio** and integrates with **LangChain** and **Neo4j**.

---

## ⚙️ Features

- Natural language to Cypher conversion
- Clean conversational UI (Gradio)
- Works with any Neo4j schema (domain-agnostic)
- Schema-aware Cypher generation using LLM

---

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```
Before running the app, create a .env file in the project root directory with the following variables:
```bash
# Neo4j configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_neo4j_password

# Gemini (Google) API key
GOOGLE_API_KEY=your_google_api_key
```
## ⚙️ How to run
```bash
python main.py
```

