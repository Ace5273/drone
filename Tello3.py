from mpu6050 import mpu6050
from tello import RcDrone, KeyboardRcDrone
from time import sleep
from math import fabs


        # if math.fabs(x) < self.gyro_limit:
        #     x = 0
        
        # if math.fabs(y) < self.gyro_limit:
        #     y = 0
        
        # if math.fabs(z) < self.gyro_limit:
        #     z = 0
        
        #         if math.fabs(x) < self.acc_limit:
        #     x = 0
        
        # if math.fabs(y) < self.acc_limit:
        #     y = 0
        
        # if math.fabs(z) < self.acc_limit:
        #     z = 0

sign = lambda x: (1, -1)[x < 0]

mpu = mpu6050(0x68)
tello = RcDrone()
mpu.set_x_accel_offset(-3707.84719999997)
mpu.set_y_accel_offset(1535.716800000001)
mpu.set_z_accel_offset(1369.4265000000087)
mpu.set_x_gyro_offset(555.0092749999922)
mpu.set_y_gyro_offset(-48.365825000000285)
mpu.set_z_gyro_offset(-6.769650000000018)

mpu.set_accel_range(mpu.ACCEL_RANGE_16G)
mpu.set_gyro_range(mpu.GYRO_RANGE_2000DEG)

def is_acc_move(acc,prev_acc, axis= 'x', limit=1):
    movement = fabs(acc[axis] - prev_acc[axis])
    return movement > limit*3

def is_gyro_move(gyro,prev_gyro, axis= 'x', limit=40):
    # movement = fabs(gyro['x'] - prev_gyro['x'])+fabs(gyro['y'] - prev_gyro['y'])+fabs(gyro['z'] - prev_gyro['z'])
    movement = fabs(gyro[axis] - prev_gyro[axis])
    return movement > limit

acc = mpu.get_accel_data()
gyro = mpu.get_gyro_data()

# sleep(5)
print('started')
tello.command()
tello.takeoff()

sleep(1)
# tello.command()

did_move = False

while True:
    (prev_acc,prev_gyro,acc,gyro) = (acc,gyro,mpu.get_accel_data(),mpu.get_gyro_data())
    (prev_did_move, did_move) = (did_move,is_gyro_move(gyro,prev_gyro, limit=120))
    print(did_move)
    # prev_acc = acc
    # prev_gyro = gyro
    # print(acc)
    # print(gyro)
    # print(is_acc_move(**acc))
    
    if did_move and not prev_did_move:
        tello.set_rc_val(yaw=sign(gyro['x']) * 30)
    # elif tello.yaw != 0:
    #     tello.stop_yaw()

    sleep(0.1)
    try:
        pass
    except KeyboardInterrupt:
        tello.land()
        sleep(1)
        tello.sock.close()
        break