
from mpu6050 import mpu6050
from tello import RcDrone
from time import sleep
from math import fabs
import asyncio

loop = asyncio.get_event_loop()

# This is a simple sign function
sign = lambda x: (1, -1)[x < 0]

# The objects
drone = None
mpu = None



def init_drone():
    drone = RcDrone()
    print('Drone intialized')

def init_mpu():
    mpu = mpu6050(0x68)

    # These were my values to intialize
    # to each their own
    mpu.set_x_accel_offset(-3707.84719999997)
    mpu.set_y_accel_offset(1535.716800000001)
    mpu.set_z_accel_offset(1369.4265000000087)
    mpu.set_x_gyro_offset(555.0092749999922)
    mpu.set_y_gyro_offset(-48.365825000000285)
    mpu.set_z_gyro_offset(-6.769650000000018)

    # Setting up the ranges of the mpu 
    mpu.set_accel_range(mpu.ACCEL_RANGE_16G)
    mpu.set_gyro_range(mpu.GYRO_RANGE_2000DEG)

    print('Mpu intialized')

async def print_info():
    # x = input()
    while True:
        print('print_info')
        await async_sleep(2)

async def print_info2():
    # x = input()
    while True:
        print('print_info2')
        await asyncio.sleep(2)

async def main(**args):
    print('main')
    await asyncio.gather(print_info(), print_info2())
    # init_drone()
    # init_mpu()
    # print_info()
    # while True:
    #     print('check1')
    #     await async_sleep(2)
        # sleep(1)
        # x = input()
        # print(x)
        # if(x == 'c'):
        #     loop.stop()

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    
    # Literally any exception
    except KeyboardInterrupt:
        print("exit")