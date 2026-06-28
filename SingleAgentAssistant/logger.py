import logging
import os


# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")


logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_query(query: str, intent: str):
    """
    Log each user query and detected intent.
    """
    logging.info(f"Query: {query} | Intent: {intent}")