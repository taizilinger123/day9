#!/usr/bin/env python
# coding:utf-8

import socket

def handle_request(client):
    buf = client.recv(1024)
    # str(1)
    # list((111,))
    # bytes('asdf')
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    f = open('index.html','r',encoding='utf-8')
    data = f.read()
    f.close()
    import time
    r = str(time.time())
    data.replace('@@@@@',r)
    client.send(data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()