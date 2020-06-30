## xorm框架知识介绍
##### @author：Davie
##### 版权所有：北京千锋教育科技有限公司

### xorm框架介绍
xorm是一个简单而强大的Go语言ORM库. 通过它可以使数据库操作非常简便。
通过xorm框架，开发者可以方便的使用各种封装好的方法来代替原生的sql语句。这样就降低了我们开发者使用数据库的门槛。本节内容，我们将通过xorm相关知识的学习，来逐步掌握在代码中如何操作数据库。
读者也可以通过相关的学习文档进行xorm框架的学习，如下是xorm框架相关的学习文档：

* xorm的Github仓库地址：[https://github.com/go-xorm/xorm](https://github.com/go-xorm/xorm)
* xorm说明文档地址：[http://xorm.io/docs](http://xorm.io/docs)

### 支持数据库驱动列表
同其他对象关系映射框架一样，xorm也支持连接、操作多种数据库，包括：mysql、mymysql、postgres、tidb、sqlite、mssql、oracle(测试）。具体的每一种数据库类型的驱动安装如下：

* Mysql: [Mysql: github.com/go-sql-driver/mysql](github.com/go-sql-driver/mysql)
* MyMysql: [github.com/ziutek/mymysql/godrv](github.com/ziutek/mymysql/godrv)
* Postgres: [github.com/lib/pq](github.com/lib/pq)
* Tidb: [github.com/pingcap/tidb](github.com/pingcap/tidb)
* SQLite: [github.com/mattn/go-sqlite3](github.com/mattn/go-sqlite3)
* MsSql: [github.com/denisenkom/go-mssqldb](github.com/denisenkom/go-mssqldb)
* MsSql: [github.com/lunny/godbc](github.com/lunny/godbc)
* Oracle: [github.com/mattn/go-oci8](github.com/mattn/go-oci8) (试验性支持)

### xorm安装
```
go get xorm.io/xorm
```
### mysql连接示例
本节内容中，我们将以连接mysql为案例，演示xorm的相关操作。

* 创建引擎

```
engine, err := xorm.NewEngine(driverName, dataSourceName)
```
如上通过xorm.NewEngine方法创建一个数据库操作引擎，该方法需要两个参数：driveName和dataSourceName。在mysql引擎连接中，两个参数如下：
```
driverName := "mysql"
dataSrouceName := "用户名:密码@/数据库名称?charset=utf8"
```

另外，需要格外注意一点，需要在使用数据库引擎创建的地方导入对应的数据库引擎驱动，比如本节内容中的mysql数据库，引擎导入语句如下：
```
_ "github.com/go-sql-driver/mysql"
```

### mysql连接配置
* **设置自动同步结构体到数据库**
xorm框架的engine数据库引擎，提供了engine.Sync()方法，允许开发者将自定义的结构体同步到数据库中。
随着xorm框架不断更新和迭代，在Sync方法的基础上，又提供了Sync2方法，用于将结构体同步更新到数据库中。Sync2方法主要的特性是：
    + 自动检测和创建表
    + 自动检测和新增表中的字段名
    + 自动检测创建和删除索引
    + 自动转换varchar字段类型到text字段类型
    + 自动警告字段的默认值
  
    ```
    err = engine.Sync2(new(model.Permission), new(model.City), new(model.Admin), new(model.AdminPermission), new(model.User))
    ```
如上是Sync2方法的使用方法
* **其他设置**
    + 是否显示SQL语句（开发调试时使用）
    
        ```
        engine.ShowSQL(true)
        ```
    + 设置数据库最大连接数
    
        ```
        engine.SetMaxOpenConns(10)
        ```
    
    + 设置最大空闲连接数量：默认是2  
        ```
        engine.SetMaxIdleConns(5)
        ```
    
    本节课我们介绍了xorm框架的基本内容和学习文档，以及如何连接mysql数据库，并进行相关设置的内容。下节课我们将学习xorm框架如何具体实现数据库的操作相关的方法。