# Import required modules
import logging
from pynput.mouse import Listener

# Path to directory for storing mouselogs - User home (~) directory
log_dir = "~/"

logging.basicConfig(filename=(log_dir + "mouse_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

#  Event - Click
def on_click(x, y, button, pressed):
    if pressed:
        logging.info('"{0}", {1}'.format(button, (x, y)))

# Event - Scroll
def on_scroll(x, y, dx, dy):
    logging.info('"{0}", {1}'.format('Button.scroll', (x, y)))

# Collect events
with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
