#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

'''客户端'''
import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象，需要赋值
client.connect(('localhost', 6969))

client.send(b"Hello World!")    # 转化为byte（英文）
client.send("我要下载a片".encode("utf-8"))   # 中文要转化成utf8格式
data = client.recv(1024)    # 限定接受数据字节大小
print("recv:", data)
client.close()