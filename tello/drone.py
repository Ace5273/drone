from multipledispatch import dispatch 
from .base_drone import BaseDrone

class Drone(BaseDrone):

    def up(self, x):
        self.send(f'up {x}')

    def down(self, x):
        self.send(f'down {x}')

    def left(self, x):
        self.send(f'left {x}')

    def right(self, x):
        self.send(f'right {x}')

    def forward(self, x):
        self.send(f'forward {x}')

    def back(self, x):
        self.send(f'back {x}')

    def cw(self, x):
        self.send(f'cw {x}')

    def ccw(self, x):
        self.send(f'ccw {x}')

    @dispatch(int,int,int,int)
    def go(self, x, y, z, speed):
        self.send(f'go {x} {y} {z} {speed}')

    @dispatch(int,int,int,int,int,int,int)
    def curve(self, x1, y1, z1, x2, y2, z2, speed):
        self.send(f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed}')

    @dispatch(int,int,int,int, int)
    # pylint: disable=function-redefined
    def go(self, x, y, z, speed, mid):
        self.send(f'go {x} {y} {z} {speed} {mid}')

    @dispatch(int,int,int,int,int,int,int,int)
    # pylint: disable=function-redefined
    def curve(self, x1, y1, z1, x2, y2, z2, speed, mid):
        self.send(f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed} {mid}')

    def jump(self, x, y, z, speed, yaw, mid1, mid2):
        self.send(f'jump {x} {y} {z} {speed} {yaw} {mid1} {mid2}')

    def speed(self, x):
        self.send(f'speed {x}')

    def rc(self, left_right=0, forward_backward=0, up_down=0, yaw=0):
        self.send(f'rc {left_right} {forward_backward} {up_down} {yaw}')

    def mon(self):
        self.send('mon')

    def moff(self):
        self.send('moff')

    def mdirection(self, x):
        self.send(f'mdirection {x}')
