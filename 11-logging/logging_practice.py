'''
What is logging? 
Logging = writing messages to a file (or console) so you can see what your program did later.  
Instead of using print() everywhere, you use `logging` because:

- you can control what shows (debug, info, warning, error)
- messages go to file automatically
- you can turn levels on/off without changing code
- looks professional in real projects
'''
### Quick comparison
#print("user logged in")` → only you see it now  
#logging.info("user logged in")` → saved in file forever, timestamped, level-controlled

### Step 1 – super basic logging )

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("program started")
logging.warning("battery low")
logging.error("file not found")
logging.debug("this is hidden unless you change level")



### Step 2 – different levels (you decide what to show)
logging.debug("detailed info for developers")
logging.info("normal useful message")
logging.warning("something might be wrong")
logging.error("something bad happened")
logging.critical("program will crash soon!!!")
# levels from low to high:
# debug < info < warning < error < critical
#default level = warning- debug & info won’t show unless you set `level=logging.DEBUG`



### Step 3 – real useful example 
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()   # also show in console
    ]
)
def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        print("Cannot divide by zero")

divide(10, 2)   # works
divide(10, 0)   # error logged



### Step 4 – named logger 
import logging

logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("my_app.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

logger.addHandler(handler)

logger.info("app started")
logger.warning("low memory")


''' quick cheat sheet 

| level       | when to use                              | example                 |
|-------------|------------------------------------------|-------------------------|
| debug       | detailed steps (for developers)          | entering function x     |
| info        | normal important events                  | user logged in          |
| warning     | something unexpected but not fatal       | old file format         |
| error       | something failed but program continues   | file not found          |
| critical    | serious problem- program may stop       | database connection lost |

'''
### practice 
import logging

logging.basicConfig(
    filename="game.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("player started game")
logging.info("score is now 100")
logging.warning("low health")
logging.error("enemy not found")

print("check game.log file")
