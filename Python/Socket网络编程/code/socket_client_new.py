#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

'''客户端'''
import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象，需要赋值
client.connect(('localhost', 6969))

while True:
    msg = input(">>:").strip()

    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))    # send的内容不能为空

    data = client.recv(1024)    # 限定接受数据字节大小
    print("recv:", data.decode())
client.close()