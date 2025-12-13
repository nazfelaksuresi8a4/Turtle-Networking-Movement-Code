import socket 
import tkinter as tk 
import turtle as animator

class MainUi():
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.screen = None

        self.window = tk.Tk('Start Host')
        self.ip_entry = tk.Entry() #ip
        self.port_entry = tk.Entry() #port
        self.apply = tk.Button(text='Başlat')

        self.iterator = [self.ip_entry,self.port_entry,self.apply]

        for widget in self.iterator:
            widget.pack(ipadx=20,ipady=20)

        self.apply.bind(sequence='<Button>',func=self.indexer)

        self.window.mainloop()
    
    def indexer(self,event):
        if self.ip_entry != '' and self.port_entry != '':
            self.mainwindow = MainWindow(self.ip_entry.get(),self.port_entry.get())

        else:
            self.mainwindow = MainWindow(None,None)

        self.mainwindow.StartServer()

class MainWindow():
    def __init__(self,ip,port):
        super().__init__()
        self.flag = False
        self.client_flag = False
        self.loading_flag = True
        self.e0socketConnectionError = None

        self.ip = ip
        self.port = port
        self.Screen = animator.Screen()
        self.Arrow = animator.Turtle(shape='classic',visible=True)

        self.arX = 0
        self.arY = 0

        self.localhost = socket.socket(socket.AF_INET)
        self.localhost.connect(('8.8.8.8',53))
        self.localip,self.localport = self.localhost.getsockname()
        self.localhost.close()

        print(self.localip,self.localport)
    
    def StartServer(self):
        try:
            self.socket_server = socket.socket(socket.SOCK_DGRAM)

            if len(self.ip) > 5 and len(self.port) == 6:
                self.socket_server.bind((str(self.ip),int(self.port)))
                
            else:
                self.socket_server.bind((str(self.localip),int(self.localport)))

            if self.socket_server is not None:
                self.flag = True
            else:
                self.flag = False

        except Exception as e0:
            self.e0socketConnectionError = e0
            print(self.e0socketConnectionError)
        
        finally:
            if self.flag == True:
                if len(self.ip) > 5 and len(self.port) == 6:
                    print(f'current ip addr: {self.ip}, current port addr: {self.port}')
                
                else:
                    print(f'current ip addr: {self.localip}, current port addr: {self.localport}')

                self.listen()
            
            else:
                print(f'Socket Connection error: {self.e0socketConnectionError}')

    def listen(self):
        print('Socket ready')
        self.client,self.client_addr = None,None
        self.socket_server.listen(12)

        print('Command listening.....')
        while self.client_flag:
            self.client,self.client_addr = self.socket_server.accept()
            print(f'Conection detected, client information: {self.client.getsockname()}')
            self.client_flag = False

        if self.client is not None and self.client_addr is not None:
            while True:
                command = self.client.recv(1024).decode()
                if command != '':
                    try:
                        if command == 'up':
                            self.arY += 1
                        
                        if command == 'down':
                            self.arY -= 1
                        
                        if command == 'right':
                            self.arX += 1
                        
                        if command == 'left':
                            self.arX -= 1
                    except Exception as e0TurtleMovementXY:
                        print(e0TurtleMovementXY)
                    
                    finally:
                        self.Arrow.goto(self.arX,self.arY)

                else:
                    pass
                        


if __name__ == "__main__":
    app = MainUi()
