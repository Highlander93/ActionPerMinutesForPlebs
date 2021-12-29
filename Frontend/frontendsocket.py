import threading
from socket import socket

from Frontend import windowhandler


def on_new_client(clientsocket):
    msg = clientsocket.recv(1024)
    windowhandler.update_apm_counter(msg.decode())


def start_frontend_socket():
    frontend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    frontend_socket.bind(('', 4334))
    frontend_socket.listen(5)
    while True:
        (clientsocket, address) = frontend_socket.accept()

        start_new_thread = threading.Thread(target=on_new_client, args=clientsocket)
        start_new_thread.start()

    frontend_socket.close()
