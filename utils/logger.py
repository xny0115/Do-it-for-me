# utils/logger.py
import logging
import os

log_path = "logs"
os.makedirs(log_path, exist_ok=True)

logger = logging.getLogger("difm")
logger.setLevel(logging.INFO)

fh = logging.FileHandler(os.path.join(log_path, "difm.log"), encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
