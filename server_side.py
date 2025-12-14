import turtle 
import socket
import threading
import numpy as np

class mainClass():
    def __init__(self):
        self.dX = 0
        self.dY = 0

        self.ignit()

    def start_turtle(self):
        self.screen = turtle.Screen()
        self.arrow = turtle.Turtle()

        self.screen.mainloop()

    def start_server(self):
        socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_server.bind(('192.168.1.6',45404))
        socket_server.listen(1)

        client, _ = socket_server.accept()

        buffer = ""

        while True:
            command = client.recv(1024)

            if command != b'':
                cmd = command.decode()
                buffer += cmd
                if len(buffer) > 18:
                    buffer = ''

                print(len(buffer))

                cmdf = cmd.split('\n')[0]

                if cmdf == 'up':
                    self.dY += np.pi*5
                if cmdf == 'down':
                    self.dY -= np.pi*5
                if cmdf == 'right':
                    self.dX += np.pi*5
                if cmdf == 'left':
                    self.dX -= np.pi*5
                
                self.arrow.goto(self.dX,self.dY)
    

    def ignit(self):
        self.thread1 = threading.Thread(target=self.start_server)   
        self.thread2 = threading.Thread(target=self.start_turtle)

        self.thread1.start()
        self.thread2.start()

clss = mainClass()
