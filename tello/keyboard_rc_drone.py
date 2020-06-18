from .rc_drone import RcDrone
from keyboard import on_press_key, on_release_key

class KeyboardRcDrone(RcDrone):
    
    speed=10

    # def __init__(self,address: str='', port: int = 9000, drone_address: str = '192.168.10.1', drone_port: int=8889):
    #     pass

    def set_keys(self, up=None, down=None, left=None, right=None, forwards=None, backwards=None):

        if up:
            on_press_key(up, lambda a: self.set_rc_val(y_axis=self.speed))
            on_release_key(up, lambda a: self.stop_y_axis())
        
        if down:
            on_press_key(down, lambda a: self.set_rc_val(y_axis=-self.speed))
            on_release_key(down, lambda a: self.stop_y_axis())
            
        
        if left:
            on_press_key(left, lambda a: self.set_rc_val(x_axis=self.speed))
            on_release_key(left, lambda a: self.stop_x_axis())
        
        if right:
            on_press_key(right, lambda a: self.set_rc_val(x_axis=-self.speed))
            on_release_key(right, lambda a: self.stop_x_axis())
        
        if forwards:
            on_press_key(forwards, lambda a: self.set_rc_val(z_axis=self.speed))
            on_release_key(forwards, lambda a: self.stop_z_axis())
        
        if backwards:
            on_press_key(backwards, lambda a: self.set_rc_val(z_axis=-self.speed))
            on_release_key(backwards, lambda a: self.stop_z_axis())
        
        return self
    
    def set_speed(self, speed):
        self.speed = speed
        print(f'Speed: {speed}')
