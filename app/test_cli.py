from app.controller import handle_user_input

def cli_ui():
    print("\n")
    print("🧠 Natural Language to Neo4j CLI")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Ask something about your graph DB: ")
        if user_input.lower() == "exit":
            break

        print("\nProcessing...")
        response = handle_user_input(user_input)

        # print("\n🔹 Generated Cypher Query:")
        # print(response["cypher_query"])

        # print("\n🔸 Raw Result:")
        # print(response["result"])

        print("\n🤖 Model Answer:")
        print(response["answer"])  # why it is returning the result always :)

        # print("\n📘 Explanation:")
        # print(response["explanation"])
        print("\n" + "-"*50 + "\n")

