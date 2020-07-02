from mpu6050 import mpu6050
from tello import RcDrone
from math import fabs
from gpiozero import Button
import smbus

class HandRemoteSerivce():
    
    drone : RcDrone = None
    mpu : mpu6050 = None

    # The prev states
    prev_acc = None
    prev_gyro = None

    min_acc = 1.5
    min_gyro = 6.3

    drone_velocity = None

    def __init__(self):
        # self.init_drone()
        self.init_mpu()
        self.reset_drone_velocity()

    def init_drone(self):
        self.drone = RcDrone()
        print('Drone intialized')
    
    def init_mpu(self):
        self.mpu = mpu6050(0x68)

        # These were my values to intialize
        # to each their own
        self.mpu.set_x_accel_offset(-3707.84719999997)
        self.mpu.set_y_accel_offset(1535.716800000001)
        self.mpu.set_z_accel_offset(1369.4265000000087)
        self.mpu.set_x_gyro_offset(555.0092749999922)
        self.mpu.set_y_gyro_offset(-48.365825000000285)
        self.mpu.set_z_gyro_offset(-6.769650000000018)

        # Setting up the ranges of the self.mpu 
        self.mpu.set_accel_range(self.mpu.ACCEL_RANGE_16G)
        self.mpu.set_gyro_range(self.mpu.GYRO_RANGE_250DEG)

        print('Mpu intialized')
    
    def add_acc_difffrence_to_velocity(self):

        # Get the current acc data
        curr_acc = self.mpu.get_accel_data()
        acc_x = curr_acc['x'] - self.prev_acc['x']
        acc_y = curr_acc['y'] - self.prev_acc['y']
        acc_z = curr_acc['z'] - self.prev_acc['z']

        if fabs(acc_x) < self.min_acc:
            acc_x = 0

        if fabs(acc_y) < self.min_acc:
            acc_y = 0
        
        if fabs(acc_z) < self.min_acc:
            acc_z = 0
        
        # Added drone velocity
        self.drone_velocity['x'] += acc_x
        self.drone_velocity['y'] += acc_y
        self.drone_velocity['z'] += acc_z

        # Set the curr acc to prev acc
        self.prev_acc = curr_acc

    def add_gyro_difffrence_to_velocity(self, curr_gyro, prev_gyro, min_gyro):
        
        # Get the current gyro data
        curr_gyro = self.mpu.get_gyro_data()
        gyro_x = curr_gyro['x'] - self.prev_gyro['x']
        # gyro_y = curr_gyro['y'] - prev_gyro['y']
        # gyro_z = curr_gyro['z'] - prev_gyro['z']

        if fabs(gyro_x) < self.min_gyro:
            gyro_x = 0

        # if fabs(gyro_y) < min_gyro:
        #     gyro_y = 0
        
        # if fabs(gyro_z) < min_gyro:
        #     gyro_z = 0
        
        # Added the drone gyro velocity
        self.drone_velocity['yaw'] += gyro_x

        # Set the prev gyro
        self.prev_gyro = curr_gyro
    
    def reset_drone_velocity_in_axis(self, axis):
        self.drone_velocity[axis] = 0
    
    def reset_drone_velocity(self):
        print(self.drone_velocity)
        self.prev_acc = {'x': 0, 'y': 0, 'z':0}
        self.prev_gyro = {'x': 0, 'y': 0, 'z':0}
        self.drone_velocity = {'x': 0, 'y': 0, 'z':0, 'yaw':0}