import socket 
import time
client = socket.socket(socket.SOCK_DGRAM)
client.connect(('192.168.1.6',45404))

index = 0

for i in range(120):
    if index < 4:
        client.send('up\n'.encode())
    if index > 4:
        client.send('down\n'.encode())
    if index > 6:
        client.send('right\n'.encode())
    if index > 8:
        client.send('left\n'.encode())

    time.sleep(0.2)

    index += 1
