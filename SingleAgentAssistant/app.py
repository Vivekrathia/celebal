import json
from agent import Agent


def main():
    print("=" * 60)
    print("🤖 Single Agent Smart Assistant")
    print("Type 'exit' to quit.")
    print("=" * 60)

    agent = Agent()

    while True:
        query = input("\nYou: ").strip()

        if query.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        if not query:
            print("⚠️ Please enter a query.")
            continue

        response = agent.process(query)

        print("\nAssistant:")
        print(json.dumps(response, indent=4))


if __name__ == "__main__":
    main()