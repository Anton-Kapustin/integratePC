import json
import socket


class client:
    LOG_TAG = "client: "
    conn = None

    def conneсtion():
        print(client.LOG_TAG + "Подключение к серверу")
        client.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.conn.connect(('192.168.88.12', 18031))
            print(client.LOG_TAG + "Подключено")
        except socket.error as msg:
            print(client.LOG_TAG + str(msg))

        except TimeoutError as msg:
            print(client.LOG_TAG + "Timeout")

    def sending(str):
        client.conn.send((json.dumps(str)).encode('utf-8'))
        # client.conn.send(str.encode('utf-8'))
        # client.conn.sendall(str.encode('utf-8'))
        print(client.LOG_TAG + "Отправлено : ")

    def closing():
        client.conn.close()
        print(client.LOG_TAG + "Соединение закрыто")
