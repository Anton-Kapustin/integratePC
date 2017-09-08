# -*- coding: utf-8 -*-

import socket, threading, json
from Commands import Commands

class SRV:
    def __init__(self, commands):

        self.LOG_TAG = "SRV: "
        self.threadingBroadcast()
        self.count = 0
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try: 
            print(self.LOG_TAG + "bind")
            self.sock.bind(('', 18030))
            print(self.LOG_TAG + "binded")            
        except OSError as msg:
            print(self.LOG_TAG + str(msg))
        
        self.receiveData = ""
        self.data = ""
        self.commands = commands


    def broadcastSrv(self):
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print(self.LOG_TAG + "Создан сокет")
        hostName = socket.gethostname()
        message = 'integrate, name: ' + hostName
        print(self.LOG_TAG + message)
        udp_sock.sendto(message.encode('utf-8'), ('255.255.255.255', 18032))
        print(self.LOG_TAG + "Отправлен")
        udp_sock.close()

    def threadingBroadcast(self):
        thread = threading.Thread(target=self.broadcastSrv, args=())
        print(self.LOG_TAG + "Запуск в отдельном потоке")
        thread.start()
        print(self.LOG_TAG + "Запущено")
        threading.Timer(10, self.threadingBroadcast).start()

    def start(self):
    
        self.connection = True
        print(self.LOG_TAG + "Ожидание подключения")
        self.sock.listen(10)
        conn, addr = self.sock.accept()
        thread = threading.Thread(target=self.communicate, args=(conn, addr))
        thread.start()

    def communicate(self, conn, addr):
        print(self.LOG_TAG + str(addr))
        # conn.settimeout(5)
        print(self.LOG_TAG + "Подключение установлено")
        count = 0
        while True:
            try:
                self.receiveData = conn.recv(1024).decode('utf-8')
                print(self.LOG_TAG + self.receiveData)
                print(self.LOG_TAG + " read: " + str(count))
                if not self.receiveData:
                    break
                else:
                    if type(self.receiveData) is list:
                        print(self.LOG_TAG + "list object! " + self.receiveData[0])
                    elif "\n" in self.receiveData:
                        print(self.LOG_TAG + "Неверный запрос")
                        break
                    else:
                        self.data = self.receiveData

            except OSError as msg:
                print(self.LOG_TAG + str(msg))
            count += count
        print(self.LOG_TAG + "Получено: " + self.data)
        self.commands.analyze(self.data, addr[0])
        conn.close()
        print(self.LOG_TAG + "Соединение разорвано")
        self.count += 1
        print(self.LOG_TAG + str(self.count))

    def stop(self):
        self.connection = False
        self.conn.close()
        self.sock.close()
        print(self.LOG_TAG + "Сервер остановлен")

if __name__ == "__main__":
    sock = SRV()
