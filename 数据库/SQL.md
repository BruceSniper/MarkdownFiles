# SQL
> *Structured Query Langugge*

SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持SQL语言进行操作，也就是说可以通过SQL操作 oracle,sql server,mysql,sqlite 等等所有的关系型数据库

* SQL语句主要分为：
    * **DQL(Data Query Language)：数据查询语言，用于对数据进行查询，如select**
    
    * **DML(Data Manipulation Language)：数据操作语言，对数据进行增加、修改、删除，如insert、update、delete**
    
    * TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback

    * DCL(Data Control Language)：数据控制语言，用来定义数据库的访问权限和安全级别，及创建用户（授权与权限回收）。如 grant、 revoke 等

    * DDL(Data Definition Language)：数据定义语言，用来定义数据库对象：数据库，表，列等。如 create, drop,alter 等

    * CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor

* **对于web程序员来说，重点是数据的增删查改，必须熟练地编写DQL，DML，能够编写DDL完成数据库、表的操作** ，其他了解即可

