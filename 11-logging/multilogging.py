"""
What does "multiple logging" mean?
You want the same log message to go to "several places" at once, for example:
- to the console (so you see it while developing)
- to a file (so you have permanent record)
- maybe to another file with only errors
- or even send email/slack for critical things (advanced)
"""
### The easiest and most common way
## Use multiple handlers on one logger.
import logging
# create main logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # capture everything
# formatter (how each line looks)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")

# 1. Console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)          # show INFO and higher in console
console.setFormatter(formatter)
logger.addHandler(console)

# 2. General log file (everything)
file_all = logging.FileHandler("app_all.log")
file_all.setLevel(logging.DEBUG)        # save everything
file_all.setFormatter(formatter)
logger.addHandler(file_all)

# 3. Error-only file
file_error = logging.FileHandler("errors_only.log")
file_error.setLevel(logging.ERROR)      # only ERROR and CRITICAL
file_error.setFormatter(formatter)
logger.addHandler(file_error)

# now use it
logger.debug("this goes only to app_all.log")
logger.info("this goes to console + app_all.log")
logger.warning("same as info")
logger.error("this goes to console + both files")
logger.critical("same as error")




### Even simpler version (quick setup)
## If you just want console + one file and don’t want to create logger manually:
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),                # console
        logging.FileHandler("everything.log")   # file
    ]
)

logging.info("hello")
logging.error("oops")



'''Common real patterns people use
Console + debug file + error file (like example above)
Console only in development, file only in production
One file per day (rotating logs)'''
import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    backupCount=30
)



### Different loggers for different modules
logger_db = logging.getLogger("database")
logger_ui = logging.getLogger("ui")



### practice task
import logging
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

file = logging.FileHandler("test.log")
file.setLevel(logging.DEBUG)
logger.addHandler(file)

logger.debug("debug message")
logger.info("info message")
logger.error("error message")
