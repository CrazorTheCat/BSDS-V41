import time
import socket

import Configuration
from Classes.Connection import Connection


class ServerConnection:
    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if Configuration.settings["DisableNagle"] == True:
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print("Listening for new connection...")
        while True:
            time.sleep(0.1)
            self.server.listen()
            socket, address = self.server.accept()
            print("New connection with address", address[0], "on port", address[1])
            Connection(socket, address).start()