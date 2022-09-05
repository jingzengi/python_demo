#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/9/4 22:07

import socket

def make_server(ip, port, app):  # 代表服务
    # 处理套接字通信相关事宜
    sock = socket.socket()
    sock.bind((ip, port))
    sock.listen(5)
    print('Starting development server at http://%s:%s' %(ip, port))
    while True:
        conn, addr = sock.accept()

        # 1 接收浏览器发来的请求信息
        recv_data = conn.recv(1024)
        # print(recv_data.decode('utf-8'))


        # 2 将请求信息直接转交给appliantion处理，得到返回值
        res = app(recv_data)

        # 3 向浏览器返回消息
        conn.send(res)

        conn.close()

def app(environ):   # 代表application
    # 处理业务逻辑
    return b'hello world'

if __name__ == '__main__':
    make_server('127.0.0.1', 8008, app)