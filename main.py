from tello.drone import Tello, TelloRcControl
import keyboard

drone = TelloRcControl()

while True:
    drone.get_send_action(keyboard.read_key())