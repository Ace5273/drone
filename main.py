
from time import sleep
import asyncio
from gpiozero import Button
from signal import pause
from hand_remote import HandRemoteSerivce

button = Button(18)

# This is a simple sign function
sign = lambda x: (1, -1)[x < 0]

def main():
    print('main')
    hand_remote_service = HandRemoteSerivce()

    button.when_deactivated = hand_remote_service.reset_drone_velocity

    # # The accleration movement
    # prev_acc = {'x': 0, 'y': 0, 'z':0}
    # curr_acc = {'x': 0, 'y': 0, 'z':0}
    # min_acc = 1.5

    # # The angular movement
    # prev_gyro = {'x': 0, 'y': 0, 'z':0}
    # curr_gyro = {'x': 0, 'y': 0, 'z':0}
    # min_gyro = 6.3
    button.hold_repeat = True
    button.hold_time = 0.1
    button.when_held = lambda: print('active')
    sleep(0.1)
    # await asyncio.sleep(0.1)
    while True:
        prev_acc = curr_acc
        curr_acc = hand_remote_service.mpu.get_accel_data()
        prev_gyro = curr_gyro
        curr_gyro = hand_remote_service.mpu.get_gyro_data()
        # print(curr_gyro)

        if button.is_active:
            hand_remote_service.add_acc_difffrence_to_velocity(curr_acc, prev_acc, min_acc)
            hand_remote_service.add_gyro_difffrence_to_velocity(curr_gyro, prev_gyro, min_gyro)

        sleep(0.1)
        # await asyncio.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
        # asyncio.get_event_loop().run_until_complete(main())
    
    # Literally any exception
    except KeyboardInterrupt:
        print("exit")