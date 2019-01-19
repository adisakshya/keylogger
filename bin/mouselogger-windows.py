from pynput.mouse import Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "mouse_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('"{0}", {1}'.format(button, (x, y)))

def on_scroll(x, y, dx, dy):
    logging.info('"{0}", {1}'.format('Button.scroll', (x, y)))

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
