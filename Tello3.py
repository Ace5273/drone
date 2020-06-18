from tello import RcDrone
import keyboard

tello = RcDrone() \
        .set_left_listeners(keyboard.on_press_key) \
        # .set_right_listeners

# keyboard.on_release_key('c',lambda a: tello.command())
# keyboard.on_release_key('t',lambda a: tello.takeoff())
# keyboard.on_release_key('w',lambda a: tello.rc(forward_backward=-50))
# keyboard.on_release_key('s',lambda a: tello.rc(forward_backward=50))
# keyboard.on_release_key('a',lambda a: tello.rc(left_right=-50))
# keyboard.on_release_key('d',lambda a: tello.rc(left_right=50))
# keyboard.on_release_key('l',lambda a: tello.land())
# keyboard.on_release_key('b',lambda a: tello.get_battery())

while True:
    try:
        pass
    except KeyboardInterrupt:
        tello.sock.close()
        break