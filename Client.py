import json
import socket

class Client:

    def __init__(self):
        self.LOG_TAG = "Client: "

    def conneсtion(self, ip):
        print(self.LOG_TAG + "Подключение к серверу")
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conn.connect((ip, 18030))
            print(self.LOG_TAG + "Подключено")
        except socket.error as msg:
            print(self.LOG_TAG + str(msg))

        except TimeoutError as msg:
            print(self.LOG_TAG + "Timeout")

    def sending(self, str):
        self.conn.send((json.dumps(str)).encode('utf-8'))
        # self.conn.send(str.encode('utf-8'))
        print(self.LOG_TAG + "Отправлено : ")

    def closing(self):
        self.conn.close()
        print(self.LOG_TAG + "Соединение закрыто")
