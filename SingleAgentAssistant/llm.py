import ollama


MODEL_NAME = "qwen3:8b"


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model
    and return the generated response.
    """

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"LLM Error: {str(e)}"