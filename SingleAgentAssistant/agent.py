from router import Router
from tools import calculator, extract_keywords
from llm import ask_llm
from logger import log_query


class Agent:

    def __init__(self):
        self.router = Router()

    def process(self, query: str) -> dict:

        # Determine intent
        intent = self.router.route(query)

        # ---------------- Calculator ----------------
        if intent == "calculator":

            expression = (
                query.lower()
                .replace("calculate", "")
                .replace("solve", "")
                .replace("compute", "")
                .strip()
            )

            result = calculator(expression)

            response = {
                "intent": "calculator",
                "tool": "Calculator",
                "query": query,
                "result": result,
                "status": "success"
            }

        # ---------------- Keywords ----------------
        elif intent == "keywords":

            text = (
                query.lower()
                .replace("extract keywords", "")
                .replace("keywords", "")
                .replace("extract", "")
                .strip()
            )

            keywords = extract_keywords(text)

            response = {
                "intent": "keywords",
                "tool": "Keyword Extractor",
                "query": query,
                "keywords": keywords,
                "status": "success"
            }

        # ---------------- General ----------------
        else:

            answer = ask_llm(query)

            response = {
                "intent": "general",
                "tool": "Qwen3",
                "query": query,
                "response": answer,
                "status": "success"
            }

        # Log every request
        log_query(query, intent)

        return response