import logging
import os
from datetime import datetime

# Base directory = project root (relative to this file)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Log directory
logs_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has been set up.")
    print("Log file created at:", LOG_FILE_PATH)
