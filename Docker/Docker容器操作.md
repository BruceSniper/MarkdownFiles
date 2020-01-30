# Docker容器操作

### 查看容器

* 查看 ***正在运行*** 的容器：

`docker ps`

![avatar](https://github.com/BruceSniper/MarkdownFiles/raw/master/Docker/img/5.jpg)

| 列名称 | 列含义 |
| --- | --- |
| CONTAINER ID | 容器的 ID |
| IMAGE | 创建容器时所使用的镜像 |
| COMMAND | 运行容器中的软件执行的命令 |
| CREATED | 容器的创建时间 |
| STATUS | 容器的状态 : UP 表示运行状态 Exited 表示关闭状态 |
| PORTS | 宿主机端口和容器中软件的端口的对应关系(映射) |
| NAMES | 容器的名称 |

* 查看所有的容器（包含了正在运行的容器以及之前启动过的容器）：

`docker ps -a`

* 查看最后一次运行的容器

`docker ps -l`

* 查看停止的容器

`docker ps -f status=exited`

### 创建与启动容器

##### 创建容器参数介绍

创建容器的时候我们需要使用如下命令进行容器的创建：

`docker run`

在创建容器的时候我们需要使用一下参数，其中常用的参数如下：

| 参数名称 | 参数含义 |
| --- | --- |
| -i | 启动容器 |
| -t | 容器创建成功以后我们就可以进入到容器中 |
| -d | 表示让容器在后台进行运行 |
| --name | 用来指定我们创建容器的名称 |
| -v | 用来指定目录映射 ——> 指定宿主机的某一个目录和容器中某一个目录的对应关系 |
| -p | 用来指定端口映射 ——> 指定宿主机的某一个端口和容器中运行的软件端口的对应关系 |

> 我们刚才在介绍参数的时候有一个 -d 和 -t。-d 表示让容器在后台运行起来 , -t 表示创建好容器以后我们就指定进行到容器中进入到容器中以后我们就可以输入命令和容器进行交互.既然如此那么也就是说容器我们可以分为两类: 
> 1.交互式容器 
> 2.守护式容器


##### 创建交互式容器

创建一个交互式容器并取名为itcast_docker_centos：

`docker run -it --name=itcast_docker_centos centos /bin/bash`

使用 ps 命令查看容器的状态：

`docker ps`

* 其中STATUS中的“Up”表示正在运行

使用exit退出容器

`exit`

然后再查看容器的状态：

`docker ps -a`

此时STATUS显示状态为“Exited”，容器关闭了
这就是交互式容器的特点：
**当我们退出容器以后，容器就关闭了**

##### 创建守护式容器
创建一个守护式容器：如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。命令如下（容器名称不能重复）：

`docker run -di --name=centos8 centos`

我们创建好容器以后，这个容器是以后台的方式运行的，那么我们需要操作容器就需要登录到容器中，可以使用如下命令进行登录：

```docker
docker exec -it container_name ( container_id) /bin/bash
例：
docker exec -it centos8 /bin/bash
```

输入`exit`命令退出后，使用`docker ps -a`查看容器状态，发现容器还是处于运行状态
所以守护式容器的特点是：
**即使我们退出容器以后，容器还是处于运行状态**


### 停止与启动容器

* 关闭容器

```docker
docker stop $CONTAINER_NAME/ID
例：
docker stop mycentos2
```

* 启动已关闭的容器

```docker
docker start $CONTAINER_NAME/ID
例：
docker start mycentos1
```