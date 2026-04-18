import os
import logging
from datetime import datetime

# log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# folder path (ONLY folder)
LOG_DIR = os.path.join(os.getcwd(), "logs")

# create folder
os.makedirs(LOG_DIR, exist_ok=True)

# full file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("networksecurity")