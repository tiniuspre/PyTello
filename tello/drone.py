import socket
import threading
import pickle

class Tello:
    def __init__(self, tello_ip: str='192.168.10.1', rc: bool=False):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.local_ip, self.local_port))

        self.rc = rc
        self.tello_ip = tello_ip
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)

        self.command()

    def send_command(self, command: str):
        self.socket.sendto(command.encode('utf-8'), self.tello_address)

    def command(self):
        self.send_command('command')

    def command_rc(self, forward_back, left_right, up_down, yaw):
        if rc:
            self.send_command(f'rc {left_right} {forward_back} {up_down} {yaw}')
