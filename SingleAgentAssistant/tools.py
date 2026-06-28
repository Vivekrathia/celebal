import ast
import operator
import re


# -------------------------
# Safe Calculator Tool
# -------------------------

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def calculator(expression: str):

    try:
        node = ast.parse(expression, mode="eval").body
        return _evaluate(node)

    except Exception:
        return "Invalid mathematical expression"


def _evaluate(node):

    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return OPERATORS[type(node.op)](left, right)

    elif isinstance(node, ast.UnaryOp):

        operand = _evaluate(node.operand)

        return OPERATORS[type(node.op)](operand)

    else:
        raise TypeError("Unsupported expression")


# -------------------------
# Keyword Extraction Tool
# -------------------------

STOPWORDS = {
    "the",
    "is",
    "are",
    "was",
    "were",
    "a",
    "an",
    "and",
    "or",
    "of",
    "to",
    "in",
    "on",
    "for",
    "with",
    "this",
    "that",
    "it",
    "be",
    "as",
    "at",
    "by",
    "from",
    "into",
    "about",
    "can",
    "will"
}


def extract_keywords(text: str):

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    keywords = []

    for word in words:

        if word not in STOPWORDS and len(word) > 2:
            keywords.append(word)

    # remove duplicates while preserving order
    return list(dict.fromkeys(keywords))