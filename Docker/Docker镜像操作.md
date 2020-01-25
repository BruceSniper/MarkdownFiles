# Docker镜像操作

### 列出镜像
列出宿主机上所有的镜像：

> `docker images`    




### 搜索镜像
> `docker search 镜像名称`

例：搜索tomcat镜像：

![avatar](https://github.com/BruceSniper/MarkdownFiles/raw/master/Docker/img/4.jpg)

每一列的含义：

| 列名 | 含义 |
| ---- | ---- |
| NAME | 仓库名称 |
| DESCRIPTION | 镜像描述 |
| STARS | 综合评分,反应一个镜像的受欢迎程度 |
| OFFICIAL | 是否官方 |
| AUTOMATED | 自动构建，表示该镜像由 Docker Hub 自动构建流程创建的 |

### 拉取镜像

官方 Docker Hub 网址：https://hub.docker.com/  速度太慢，不常用

使用国内镜像地址：https://docker.mirrors.ustc.edu.cn

在Centos中，用vi进行编辑：
> `vi /etc/docker/daemon.json`

在配置文件中加入下载地址信息：

> ```
> {
>        "registry mirrors": ["https://docker.mirrors.ustc.edu.cn]
>  }
> ```


重启docker：

> `systemctl restart docker`


##### 拉取镜像

> `docker pull 镜像名称`

### 删除镜像

我们可以删除指定的镜像也可以删除所有的镜像

> `docker rmi 镜像名称/镜像ID`

删除所有镜像：
> ```docker rmi `docker images -q`：删除所有镜像```


> ```
> `docker images -q` 获取所有镜像的ID
> ```