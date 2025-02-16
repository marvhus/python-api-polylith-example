# source .venv/bin/activate && ipython -i development/martin.py && deactivate

from marvhus import service_users, log

logger = log.get_logger("Martin's REPL environment")
logger.info("Hello!")

