#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

"""服务器端"""

import socket

server = socket.socket()
server.bind(('localhost', 6969))    # 绑定监听端口
server.listen() # 开始监听


print("我要开始等电话了")
# conn就是客户端连过来而在服务器端为其生成的一个连接实例
conn, addr = server.accept() # 等电话打进来
print(conn, addr)


print("电话来了")
data = conn.recv(1024)
print("recv:", data)

conn.send(data.upper())

server.close()