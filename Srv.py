# -*- coding: utf-8 -*-

import socket
from Commands import Commands

class SRV:
    def __init__(self, commands):
        self.LOG_TAG = "SRV: "
        self.count = 0
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try: 
            print(self.LOG_TAG + "bind")
            self.sock.bind(('', 18030))
            print(self.LOG_TAG + "binded")            
        except OSError as msg:
            print(self.LOG_TAG + str(msg))
        
        self.data = ""
        self.commands = commands
        # self.start()

    def start(self):

        self.connection = True
        # while self.connection:
        print(self.LOG_TAG + "Ожидание подключения")
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        conn.settimeout(5)
        print(self.LOG_TAG + "Подключение установлено")
        while True :
            try:
                self.data = conn.recv(1024).decode('utf-8')
            except OSError as msg:
                print(self.LOG_TAG + str(msg))
            print(self.LOG_TAG + self.data)
            if "end" in self.data:
                break
            elif "null" in self.data:
                break
            # elif "\n" in self.data:
            #     break
            else:
                print(self.LOG_TAG + "Анализ: " + self.data)
                if type(self.data) is list:
                    print(self.LOG_TAG + self.data[0])
                self.commands.analyze(self.data)

            print(self.LOG_TAG + "Получено: " + self.data)
        conn.close()
        print(self.LOG_TAG + "Соединение разорвано")
        self.count += 1
        print(self.count)

    def stop(self):
        self.connection = False
        self.conn.close()
        self.sock.close()
        print(self.LOG_TAG + "Сервер остановлен")

