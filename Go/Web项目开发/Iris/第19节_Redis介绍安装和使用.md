## Redis介绍安装和使用
###### @author：Davie
###### 版权所有：北京千锋互联科技有限公司

### Redis介绍
我们日常的开发，数据都需要进行持久化存储，常见的持久化存储有很多种，比如数据库，文件，计算机内存，甚至云服务器等都是持久化存储数据的方式。而就数据库而言，经常又会被人们分为关系型数据库和非关系型数据库。在我们的项目中，关系型数据库我们使用的是mysql，关系型数据库中存储的数据主要是一些核心业务数据；另外，在我们的项目中，还有一部分数据可能是不太可能变化的，比如应用中的地区数据，城市列表，或者说每天的应用人数的增加量的统计等，这些数据对时效性要求不是特别的高，因此，这个时候我们为了提高应用程序的存储效率，提高程序性能，我们会把一些数据变化不太明显，不经常变的数据存放在Redis数据库中。

那么为什么放在Redis数据库中就能提高存储效率呢？Redis数据库是一种非关系型数据库，其存储形式就是key-value格式进行存储。支持的方式也比较多，memory，disk，file等持久化存储都可以实现。key-value型数据库的特点就是可以直接根据key能够定位得到对应的值，因此，相较于关系型数据库的表结构查询的方式，非关系型数据库执行效率非常高，而且我们通常的会把数据存放在内存中，而内存的读写速度又是最快的。所以，就能够满足我们高流量，高并发的需要。

### Redis数据库安装
* Mac 系统
首先安装brew
1.brew install redis
2.将redis-server设置成环境变量：
vim .bash_profile
alias redis=/usr/local/Cellar/redis/5.0.0/bin/redis-server
注意：配置文件和路径修改成自己的配置
3.执行redis，开启redis服务
![](http://7xtcwd.com1.z0.glb.clouddn.com/redis_mac.png)

* Windows系统
1.下载Redis：https://github.com/MicrosoftArchive/redis/releases（或者见压缩包文件）
2.下载的文件是可以直接安装运行的msi文件
3.点击msi文件，依次步骤如下：
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis.png)
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis2.png)
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis3.png)
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis4.png)
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis5.png)
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis6.png)
等待安装
![](http://7xtcwd.com1.z0.glb.clouddn.com/windows_redis7.png)


    安装完毕。接下来我们来验证redis服务是否安装并启动成功：
1）首先找到自己安装redis的安装目录：
![](http://7xtcwd.com1.z0.glb.clouddn.com/redis_install.png)
2）打开cmd终端，并进入到redis安装目录：
![](http://7xtcwd.com1.z0.glb.clouddn.com/redis_start.png)
3）执行redis-cli.exe文件，如下：
![](http://7xtcwd.com1.z0.glb.clouddn.com/redis_running.png)
出现上面的画面，表示安装成功。

* 进入redis终端：**redis-cli**
