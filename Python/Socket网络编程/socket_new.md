# Socket

### 创建socket

在 Python 中 使用socket 模块的函数 socket 就可以完成：

```python
import socket
socket.socket(AddressFamily, Type)
```

**说明：**
函数 socket.socket 创建一个 socket，该函数带有两个参数：

* Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET

* Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

创建一个tcp socket（tcp套接字）

```python
import socket

# 创建tcp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()
```

创建一个udp socket（udp套接字）

```python
import socket

# 创建udp的套接字
# AF_INET代表ipv4，SOCK_DGRAM代表udp协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()
```

说明：

* 套接字使用流程 与 文件的使用流程很类似
    1.创建套接字
    2.使用套接字收/发数据
    3.关闭套接字

### udp网络程序-发送、接收数据

##### 1. udp网络程序-发送数据

创建一个基于udp的网络程序流程很简单，具体步骤如下：
    1. 创建客户端套接字
    2. 发送/接收数据
    3. 关闭套接字

![avatar](https://github.com/BruceSniper/MarkdownFiles/raw/master/Python/Socket网络编程/img/1.jpg)

```python
#coding=utf-8

from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
# '192.168.1.103'表示目的ip地址
# 8080表示目的端口
dest_addr = ('192.168.1.103', 8080)  # 注意 是元组，ip是字符串，端口是数字

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 关闭套接字
udp_socket.close()
```

##### 2. udp网络程序-发送、接收数据

```python
#coding=utf-8

from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
dest_addr = ('192.168.236.129', 8080)

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

# 6. 显示对方发送的数据
# 接收到的数据recv_data是一个元组
# 第1个元素是对方发送的数据
# 第2个元素是对方的ip和端口
print(recv_data[0].decode('gbk'))
print(recv_data[1])

# 7. 关闭套接字
udp_socket.close()
```

##### 3. udp绑定信息

* 会变的端口号
* 每重新运行一次网络程序，上图中红圈中的数字，不一样的原因在于，这个数字标识这个网络程序，当重新运行时，如果没有确定到底用哪个，系统默认会随机分配
* 记住一点：这个网络程序在运行的过程中，这个就唯一标识这个程序，所以如果其他电脑上的网络程序如果想要向此程序发送数据，那么就需要向这个数字（即端口）标识的程序发送即可

**绑定示例**

```python
#coding=utf-8

from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
local_addr = ('', 7788) #  ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_socket.bind(local_addr)

# 3. 等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024) #  1024表示本次接收的最大字节数

# 4. 显示接收到的数据
print(recv_data[0].decode('gbk'))

# 5. 关闭套接字
udp_socket.close()
```

