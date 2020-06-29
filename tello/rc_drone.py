from .base_drone import BaseDrone

class RcDrone(BaseDrone):

    # This values shouldn't be touched directly
    x_axis = 0
    y_axis = 0
    z_axis = 0
    yaw = 0
    need_to_update = False

    def stop_x_axis(self):
        self.set_rc_val(x_axis=0)

    def stop_y_axis(self):
        self.set_rc_val(y_axis=0)
    
    def stop_z_axis(self):
        self.set_rc_val(z_axis=0)
    
    def stop_yaw(self):
        self.set_rc_val(yaw=0)

    def set_rc_val(self, x_axis=None, y_axis=None, z_axis=None, yaw=None):

        if x_axis and x_axis != self.x_axis:
            self.x_axis = x_axis
            self.need_to_update = True
        
        if y_axis and y_axis != self.y_axis:
            self.y_axis = y_axis
            self.need_to_update = True
        
        if z_axis and z_axis != self.z_axis:
            self.z_axis = z_axis
            self.need_to_update = True

        if yaw and yaw != self.yaw:
            self.yaw = yaw
            self.need_to_update = True

    def rc(self):
        if self.need_to_update:
            self.send(f'rc {self.x_axis} {self.z_axis} {self.y_axis} {self.yaw}')
            self.need_to_update = False