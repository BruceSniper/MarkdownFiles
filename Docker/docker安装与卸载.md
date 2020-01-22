# Docker在CentOS7安装步骤

使用 yum 命令进行在线安装
> `yum install docker`

输入“y”确认继续安装


### 检查Docker版本

使用如下的命令 查看 Docker 的版本：
> `docker -v`


# Docker卸载

查看 docker 的安装包：

> `yum list installed | grep docker`

![avatar](https://github.com/BruceSniper/MarkdownFiles/raw/master/Docker/img/1.jpg)

删除安装包

> `yum -y remove docker.x86_64`
> `yum -y remove docker client.x86_64`
> `yum -y remove docker common.x86_64`

删除 docker 镜像(可以先进入目录查看文件和运行情况)

> `cd /var/lib/docker/`
>> `ls`
>>> `ll`

> `rm -rf /var/lib/docker/`

再次检查Docker是否已经卸载成功

![avatar](https://github.com/BruceSniper/MarkdownFiles/raw/master/Docker/img/2.jpg)

