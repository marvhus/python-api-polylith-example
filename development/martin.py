# source .venv/bin/activate && ipython -i development/martin.py && deactivate

from example import service_foo, math_utils, log

logger = log.get_logger("Martin's REPL environment")
logger.info("Hello!")

