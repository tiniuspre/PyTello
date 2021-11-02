from tello.drone import Tello
from time import sleep

drone = Tello()

drone.send_command('takeoff')
sleep(2)
drone.send_command('land')