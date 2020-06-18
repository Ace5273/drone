from tello import RcDrone, KeyboardRcDrone
import keyboard

tello = KeyboardRcDrone()
# tello = KeyboardRcDrone() \
#         .set_keys('c','v','a','d','w','s')
#         # .set_right_listeners

# keyboard.on_release_key('i',lambda a: tello.set_speed(tello.speed + 10))
# keyboard.on_release_key('u',lambda a: tello.set_speed(tello.speed - 10))
# keyboard.on_release_key('t',lambda a: tello.takeoff())
# keyboard.on_release_key('w',lambda a: tello.wifi('Drone','12345678'))
# # keyboard.on_release_key('s',lambda a: tello.rc(forward_backward=50))
# # keyboard.on_release_key('a',lambda a: tello.rc(left_right=-50))
# keyboard.on_release_key('1',lambda a: tello.command())
# keyboard.on_release_key('l',lambda a: tello.land())
# keyboard.on_release_key('b',lambda a: tello.get_battery())

while True:
    try:
        pass
    except KeyboardInterrupt:
        tello.sock.close()
        break