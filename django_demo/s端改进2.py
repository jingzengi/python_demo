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
        # 1.1 接收浏览器发出来的http协议的信息
        recv_data = conn.recv(1024)

        # 1.2 对HTTP协议的消息加以处理
        ll = recv_data.decode('utf-8').split('\r\n')
        head_ll = ll[0].split(' ')
        environ = {}
        environ['PATH_INFO'] = head_ll[1]
        environ['method'] = head_ll[0]

        # 将请求处理的结果environ交给application，得到返回值
        res = app(environ)

        # 3 向浏览器返回消息
        # 3.1 返回响应首行
        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(b'Content-Type: text/html \r\n\r\n')
        # 3.2 返回响应体
        conn.send(res)
        conn.close()

def app(environ):   # 代表application
    # 处理业务逻辑
    return b'<h1>hello world</h1><img src="https://www.baidu.com/img/bd_Log1.png"></img>'

if __name__ == '__main__':
    make_server('127.0.0.1', 8018, app)