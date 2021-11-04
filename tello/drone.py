import socket
import threading
from time import sleep


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

    def command_rc(self, forward_back=0, left_right=0, up_down=0, yaw=0):
        if self.rc:
            self.send_command(f'rc {left_right} {forward_back} {up_down} {yaw}')


class TelloRcControl:
    def __init__(self, speed=50):
        self.speed = speed

        self.drone = Tello(rc=True)
        self.drone.send_command('takeoff')


    def get_send_action(self, key_pressed):
        forward_back = 0
        left_right = 0
        up_down = 0
        yaw = 0
        if key_pressed == 'w':
            forward_back = self.speed
        elif key_pressed == 's':
            forward_back = -abs(self.speed)
        if key_pressed == 'a':
            left_right = -abs(self.speed)
        elif key_pressed == 'd':
            left_right = self.speed
        if key_pressed == 'r':
            up_down = self.speed
        elif key_pressed == 'f':
            up_down = -abs(self.speed)
        if key_pressed == 'q':
            yaw = -abs(self.speed)
        elif key_pressed == 'e':
            yaw = self.speed
        self.drone.command_rc(forward_back=forward_back,
                                  left_right=left_right,
                                  up_down=up_down,
                                  yaw=yaw
                                  )