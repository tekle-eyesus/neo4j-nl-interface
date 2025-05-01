import gradio as gr
from app.controller import handle_user_input
def clean_query_format(query: str) -> str:
    """
    Cleans markdown formatting (```cypher ... ```) from a Cypher query string.
    Returns the raw query.
    """
    lines = query.strip().splitlines()
    cleaned_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(cleaned_lines).strip()
def query_interface(user_input):
    try:
        response = handle_user_input(user_input)

        # Clean formatting: display each section separately without markdown symbols
        cypher_query = clean_query_format(response['cypher_query'])
        raw_result = response['result']
        explanation = response['explanation']
        answer = response['answer']

        return cypher_query, raw_result, explanation, answer
    except Exception as e:
        return "Error generating Cypher query.", {}, "N/A", f"❌ Error: {str(e)}"

def launch_app():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("<h1 style='text-align: center;'>Neo4j Natural Language Interface</h1>")
        gr.Markdown("<p style='text-align: center;'>Ask questions about your graph database in plain language.</p>")

        with gr.Row():
            user_input = gr.Textbox(
                lines=2,
                label="Ask something about your graph DB",
                placeholder="Ask something about your graph DB...",
                scale=2
            )

        submit_btn = gr.Button("Submit", variant="primary")

        with gr.Column():
            model_answer_output = gr.Textbox(label="Model Answer", lines=3, interactive=False)
            cypher_query_output = gr.Code(label="Generated Cypher Query", language="sql")
            raw_result_output = gr.JSON(label="Raw Result")
            explanation_output = gr.Textbox(label="Explanation", lines=6, interactive=False)

        submit_btn.click(
            fn=query_interface,
            inputs=user_input,
            outputs=[cypher_query_output, raw_result_output, explanation_output, model_answer_output]
        )

    demo.launch()
