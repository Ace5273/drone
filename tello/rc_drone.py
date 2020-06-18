from .base_drone import BaseDrone

class RcDrone(BaseDrone):

    x_axis = 0
    y_axis = 0
    z_axis = 0
    yaw = 0
    
    # def __init__(self,address: str='', port: int = 9000, drone_address: str = '192.168.10.1', drone_port: int=8889):
    #     pass

    def set_left_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(x_axis = -1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(x_axis = 0)

        return self
    
    def set_right_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(x_axis = 1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(x_axis = 0)

        return self
    
    def set_up_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(y_axis = -1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(y_axis = 0)

        return self
    
    def set_down_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(y_axis = 1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(y_axis = 0)

        return self
    
    def set_forwards_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(z_axis = -1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(z_axis = 0)

        return self
    
    def set_backwards_listeners(self, on_press=None, on_release=None):
        
        if on_press:
            on_press = lambda: self.set_rc_val(z_axis = 1)
        
        if on_release:
            on_release = lambda: self.set_rc_val(z_axis = 0)

        return self

    def set_rc_val(self, x_axis=None, y_axis=None, z_axis=None, yaw=None):

        if x_axis:
            self.x_axis = x_axis
        
        if y_axis:
            self.y_axis = y_axis
        
        if z_axis:
            self.z_axis = z_axis

        if yaw:
            self.yaw = yaw

        self.rc()

    def rc(self):
        self.send(f'rc {self.x_axis} {self.z_axis} {self.y_axis} {self.yaw}')