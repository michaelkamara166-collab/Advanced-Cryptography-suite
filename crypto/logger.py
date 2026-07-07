import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/crypto.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log(message):
    logging.info(message)
