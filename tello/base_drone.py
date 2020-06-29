from socket import socket, AF_INET,SOCK_DGRAM
from threading import Thread
from abc import ABC, abstractclassmethod

class BaseDrone(ABC):
    sock : socket = None
    tello_address = None

    def __init__(self,address: str='', port: int = 9000, drone_address: str = '192.168.10.1', drone_port: int=8889):

        # Save the tello address
        self.tello_address=(drone_address, drone_port)

        # Set the socket and bind it to a port
        self.sock=socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((address, port))

        # recive messages that comes from the threading
        Thread(target=self.recv).start()

    def send(self, msg):
        self.sock.sendto(msg.encode(encoding="utf-8") , self.tello_address)
    
    def recv(self):
        print("recv")
        # self.command()
        while True: 
            try:
                data, _ = self.sock.recvfrom(1518)
                print(f'\nDrone: {data.decode(encoding="utf-8")}\n')
                # print(server)
            except Exception:
                print("Error ocurred")
                break
    
    def command(self):
        self.send('command')

    def takeoff(self):        
        self.send('takeoff')

    def land(self):
        self.send('land')
    
    def stop(self):
        self.send('stop')
    
    def flip(self, x):
        self.send(f'flip {x}')

    def streamon(self):
        self.send('streamon')

    def streamoff(self):
        self.send('streamoff')

    def emergency(self):
        self.send('emergency')
    
    def wifi(self, ssid, passwod):
        self.send(f'wifi {ssid} {passwod}')
    
    def ap(self, ssid, passwod):
        self.send(f'ap {ssid} {passwod}')
    
    def get_speed(self):
        self.send('speed?')

    def get_battery(self):
        self.send('battery?')

    def get_time(self):
        self.send('time?')

    def get_wifi(self):
        self.send('wifi?')

    def get_sdk(self):
        self.send('sdk?')

    def get_sn(self):
        self.send('sn?')

