import re


class Router:

    def __init__(self):

        self.calculator_keywords = [
            "calculate",
            "solve",
            "compute",
            "add",
            "subtract",
            "multiply",
            "divide",
            "plus",
            "minus",
            "times",
            "into",
            "+"
            ,
            "-",
            "*",
            "/",
            "%",
            "^"
        ]

        self.keyword_keywords = [
            "keyword",
            "keywords",
            "extract",
            "important words",
            "key terms"
        ]

    def route(self, query: str) -> str:

        query = query.lower()

        # ---------- Calculator ----------
        if any(word in query for word in self.calculator_keywords):
            return "calculator"

        # Detect expressions like:
        # 25*7
        # (15+2)/4
        if re.search(r"[0-9]+\s*[\+\-\*/%]\s*[0-9]+", query):
            return "calculator"

        # ---------- Keyword Extraction ----------
        if any(word in query for word in self.keyword_keywords):
            return "keywords"

        # ---------- Default ----------
        return "general"