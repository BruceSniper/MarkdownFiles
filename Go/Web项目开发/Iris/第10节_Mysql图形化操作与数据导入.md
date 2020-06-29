## mysql图形化操作与数据导入
##### @author：Davie
##### 版权所有：北京千锋互联科技有限公司

#### 数据库存储技术
数据库（Database）是按照数据结构来组织、存储和管理数据的仓库。每个数据库都有一个或多个不同的API用于创建，访问，管理，搜索和复制所保存的数据。我们也可以将数据存储在文件中，但是在文件中读写数据速度相对较慢。所以，现在我们使用关系型数据库管理系统（RDBMS）来存储和管理的大数据量。所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。
RDBMS 即关系数据库管理系统(Relational Database Management System)的特点：
* 1、数据以表格的形式出现
* 2、每行为各种记录名称
* 3、每列为记录名称所对应的数据域
* 4、许多的行和列组成一张表单
* 5、若干的表单组成database

#### RDBMS术语
在我们开始学习MySQL 数据库前，让我们先了解下RDBMS的一些术语：
* **数据库:** 数据库是一些关联表的集合。
* **数据表:** 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
* **列:** 一列(数据元素) 包含了相同的数据, 例如邮政编码的数据。
* **行：**一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
* **冗余：**存储两倍数据，冗余降低了性能，但提高了数据的安全性。
* **主键：**主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
* **外键：**外键用于关联两个表。
* **索引：**使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
* **复合键：**复合键（组合键）将多个列作为一个索引键，一般用于复合索引。

MySQL 为关系型数据库(Relational Database Management System), 这种所谓的"关系型"可以理解为"表格"的概念, 一个关系型数据库由一个或数个表格组成, 如图所示的一个表格:
![数据库表结构](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_table.png)

* **表头(header):** 每一列的名称;
* **列(col):** 具有相同数据类型的数据的集合;
* **行(row):** 每一行用来描述某条记录的具体信息;
* **值(value):** 行的具体信息, 每个值必须与该列的数据类型相同;
* **键(key):** 键的值在当前列中具有唯一性。

#### mysql简介与安装
###### mysql简介
MySQL是一个关系型数据库管理系统，由瑞典MySQL AB公司开发，目前属于Oracle公司。MySQL是一种关联数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。
MySQL有很多优点受到企业和个人开发者的欢迎，比如说：
* MySQL是开源的，所以你不需要支付额外的费用。
* MySQL支持大型的数据库。可以处理拥有上千万条记录的大型数据库。
* MySQL使用标准的SQL数据语言形式。
* MySQL可以运行于多个系统上，并且支持多种语言。这些编程语言包括 C、C++、Python、Java、Perl、PHP、Eiffel、Ruby 和 Tcl 等。
* MySQL支持大型数据库，支持5000万条记录的数据仓库，32位系统表文件最大可支持4GB，64位系统支持最大的表文件为8TB。
* MySQL是可以定制的，采用了GPL协议，你可以修改源码来开发自己的MySQL系统。

正是MySQL易用，功能强大，免费的特点使mysql得到广泛应用，目前mysql已经成为最流行的关系型数据库管理系统，在web应用方面mysql是最好的关系数据库管理系统应用软件之一。
###### mysql安装
MySQL官方网站：[https://www.mysql.com](https://www.mysql.com)
MySQL下载网站：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
可以通过上面的链接访问MySQL官方网站和下载页面，选择MySQL版本进行下载，如下图是macOS系统的下载页面：
![MySQL下载](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_download.png)
下载后，可以直接进行点击安装，安装过程可以一直使用默认设置进行安装。参考资料如下：
* windows系统安装过程可参考：[https://zhinan.sogou.com/guide/detail/?id=316512902564](https://zhinan.sogou.com/guide/detail/?id=316512902564)
* macOS系统安装过程可参考：[https://jingyan.baidu.com/article/c843ea0b96f01877931e4a1d.html](https://jingyan.baidu.com/article/c843ea0b96f01877931e4a1d.html)

###### mysql服务查看
MySQL安装好以后，可以通过查看服务来查看MySQL的的运行状况，如下是查看方式：
* macOS的mysql服务在系统偏好设置中可以查看,如下图：
![mac中mysql服务](http://7xtcwd.com1.z0.glb.clouddn.com/mac_mysqlservice.png)
* windows系统下的mysql服务的查看方法：使用win（就是那个旗帜图案的按键）+R，弹出框中输入：services.msc。就会弹出服务窗口，在窗口中就可以查看mysql服务内容：
![mac中mysql服务](http://7xtcwd.com1.z0.glb.clouddn.com/windows_mysqlservice.png)

MySQL服务安装完成并启动后，即可使用。但是我们安装的是社区服务版，并没有图形界面供我们来操作，此时我们只能通过命令行中用户名+密码的形式来访问数据库，并实现对数据库的操作。
每次都是用命令行来执行操作数据库，效率和易用性都会受到较大影响。因此，我们希望能够有工具，帮助我们通过图形化界面的方式来操作MySQL数据库，我们通常使用的工具是navicat。

###### 登陆mysql
MySQL安装完成后，可以通过命令行工具及终端命令登陆MySQL服务，操作数据库。具体的命令如下：
* 在macOS中，可以通过终端中的命令进行登陆，登陆命令如下：

    ```
    mysql -u root -h localhost -p 
    ```
参数解释：
    + -u：用户名，这里用户名指默认的root
    + -h：主机名或者服务器IP，这里是localhost
    + -p：密码，初始密码为空，也可以自己设定新密码

    ![mac中启动mysql服务](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_login.png)

* 在windows中，可以直接打开开始->程序->MySQL->MySQL Command Line工具，就可以登陆mysql进行操作了。
    ![window中启动mysql服务](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_windows.png)

###### 端口和主机
mysql默认的端口为**3306**，本机主机名为**localhost**。

#### navicat安装与操作

###### navicat简介
Navicat for MySQL是一套管理和开发MySQL或MariaDB的理想解决方案，支持单一程序，可同时连接到MySQL和MariaDB。这个功能齐备的前端软件为数据库管理、开发和维护提供了直观而强大的图形界面，给MySQL或MariaDB新手以及专业人士提供了一组全面的工具。Navicat for MySQL 可连接到任何本机或远程 MySQL 和 MariaDB 服务器。它可以用于 MySQL 数据库服务器版本3.21或以上和 MariaDB 5.1或以上，并支持大部分功能，包括表、视图、函数或过程、事件等。
###### 下载与安装
下载地址：[https://www.navicat.com.cn/](https://www.navicat.com.cn/)
Navicat for MySQL软件支持Windows、macOS、Linux版本，学习本节内容的同学可以自行下载并进行安装。如下是navicat的主界面：
![navicat主界面](http://7xtcwd.com1.z0.glb.clouddn.com/navicat_index.png)

#### 数据库连接实例配置
打开navicat以后，可以创建MySQL数据库连接，并配置相关的参数，测试链接数据库能否成功。连接数据库操作所需要的参数配置包括：**连接名**、**主机名**、**端口**、**用户名**、**密码**等几项参数。
![数据库服务器连接实例](http://7xtcwd.com1.z0.glb.clouddn.com/connect_test.png)
数据库连接实例操作数据库
![连接实例](http://7xtcwd.com1.z0.glb.clouddn.com/open_database.png)

#### 数据库创建
navicat支持通过图形化界面创建新的数据库，操作方便，步骤简单。通过填写数据库名称即可完成创建，此时有一点需要格外注意，数据库编码需要选择**“utf8"**编码，因为通常情况下应用程序都是**utf8**编码。两者要保证一致，否则会出问题。具体如下图所示：
![创建新数据库](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_createdatabase.png)

#### 数据的导入与导出
利用navicat，也是可以对数据库表进行导出，以及将数据导入到数据表中。具体操作如下：
* 数据库导出数据
![数据库导出功能](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_export.png)
这里navicat支持提供两种导出方式，分别为：**导出数据库表创建语句**、**导出数据库数据**。该功能是将数据库表及数据导出成SQL语句。除此之外，navicat还支持导出数据成为文件，比如csv格式的文件，见下图：
![导出数据](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_exportfile.png)
* 外部数据导入到数据库
navicat也支持将外部数据导入到数据库表中，步骤与导出相反。见下图所示：
![导入数据](http://7xtcwd.com1.z0.glb.clouddn.com/mysql_importfile.png)
