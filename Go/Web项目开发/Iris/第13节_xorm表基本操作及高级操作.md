## xorm表基本操作及高级操作
##### author：Davie
##### 版权所有：北京千锋互联科技有限公司

在上节内容中，我们介绍了xorm框架表结构的映射规则和表结构的操作。本节课，继续来深入学习表结构基本操作和高级查询的相关功能。
### 表结构基本操作
对表结构的操作最常见的操作是查询和统计相关的方法，我们首先来看相关实现：
* 条件查询
    + Id值查询：参数接收主键字段的值。例如：
        
        ```
        var user User
        engine.Id(1).Get(&user)
        ```
    以上Id方法的使用，相当于如下sql语句：
    ```
    select * from user where id = 1
    ```
    如果数据库表结构是复合主键，则在使用Id时进行主键分别指定，比如以下案例：
    ```
engine.Id(core.PK(1,"davie").Get(&user)
    ```
    以上该句代码表示的即是查询多个复合主键的情况,core.PK中传入的参数顺序应该与结构体定义中的主键顺序一致，否则匹配会出错。对应的sql语句如下：
    ```
    select * from user where id = 1 and name = 'davie'
    ```
    + Where条件查询
    Where条件查询与Sql语句中的where条件查询功能一致。我们通过案例来查看Where的使用方法，如下所示：
    ```
    engine.Where(" user_name = ? and pwd = ? ", 'davie', '123').Get(&admin)
    ```
    如上xorm引擎操作即是如下sql语句的功能：
    ```
    select * from admin where user_name = 'davie' and pwd = '123'
    ```
    + And条件查询 
    And条件查询功能与Where语句的使用方式类似相同，作为并列条件和约束条件进行结果查询。使用方式如下：
    ```
    engine.Id(1).And(" user_name = ?",'davie").Get(&user)
    ```
    以上的And方法并列查询就相当于如下的sql语句：
    ```
    select * from user where id = 1 and user_name = 'davie' 
    ```
    + Or条件查询
    Or条件查询的意思是或者的意思，与编程语言中的 “ || ”功能相同，在查询时，如果有多个条件使用了Or语句，则对于同一条数据而言，只要符合其中一个条件，就会被查询出来。具体的使用方法和对应的sql语句如下：
    ```
    engine.Id(1).Or("user_name = ?",'davie').Get(&user)
    ```
    如上的Or操作语句对应如下sql语句：
    ```
    select * from user where id = 1 or user_name = davie
    ```
    + Sql条件查询
    除了上述Id、Where、And、Or等方法的使用外，xorm同样支持执行原生的sql语句，方便更愿意使用原生SQL语句的开发者。
    ```
    engine.SQL(" select * from user where id = 1 nad user_name = 'davie')
    ```
    + 排序条件查询
    在数据库查询时，会涉及到查询结果的排序问题。常规操作支持两种排序：**正排序**和**逆排序**。
    在xorm中的实现与sql语句中的两种排序方式基本相同，分别定义为Asc方法和Desc方法。或者使用OrderBy方法对自定义的排序的字段进行指定。
    注意：上述三个方法的参数都是string类型，用于指定表格字段。
    + In多值范围查询
    In方法的多值范围查询，是用于某个字段中的条件查询，该方法需要两个参数：第一个参数为指定查询的字段，第二个参数为字段多取值内容。我们同样给出如下案例：
    ```
engine.In('user_name','davie','pony','jack').Find()
    ```
    + Cols特定字段查询
    Cols方法可以接受一个或者多个特点的表字段名称，用来表示限定于操作特定的表字段。依然通过案例来说明：
    
        ```
        engine.Cols("user_name","status").Find(&admins)
        //select user_name, status from admin
        ```
        上述Cols操作表示的sql语句就是注释所对应的sql语句，表示从admin表中，查询特定的user_name, status两个字段，并将查询后的集合进行返回。
        ```
        engine.Cols("user_name","status").Update(&admin)
        //update admin set user_name = admin.User_name  and status = admin.Status
        ```
    我们可以看到，除了Find方法外，还可以调用Update方法，这里即表示更新表结构中的某条数据，且仅仅对该条数据的user_name和status两个字段进行更新，这正是由Cols方法的参数限定的。
    + AllCols操作所有字段
        除了上述的Cols指定一个或者多个字段以外，还可以通过AllCols方法来操作表所有字段，用法与Cols使用方法一致，我们不再赘述。
    + MustCols操作限定字段
        MustCols意为操作必须对某些字段起作用，该方法的使用和Update方法相结合的情况较多。
    
### 增删改查操作
说了这么多条件查询的内容，我们还没有介绍基本的表记录的增删改查操作呢。如下我们一一进行介绍：
* 增加记录操作
增加一条记录可以使用Insert方法完成。该方法接收一个参数，用于传入实际我们要保存的数据对象的结构体对象类型。如下所示：

    ```
var user
...
engine.Insert(&user)
    ```
* Delete删除记录操作
删除数据使用Delete方法来进行操作，但是我们在删除的时候要知道删除具体哪一条数据，因此在Delete操作前，需要使用我们之前讲过的Id操作将数据进行定位查找出来，我们举例如下：
    ```
    user := new(User)
    count,err := engine.Id(id).Delete(user)
    ```
    第一个返回值count表示删除的记录数，第二个参数为错误返回值，当删除失败时，err不为nil。
* Update修改记录操作
我们已经讲过MustCols的操作是用来限定必须影响某些表字段的操作的；这里再次我们强调，我们通常和Update操作放在一起来修改数据，作数据的更新操作。
    ```
    admin := new(Admin)
    admin.Status = "1"
    count,err := engine.Id(id).Update(user)
    ```
以上的Update方法是用来更新全部的数据记录，如果是限定更新某个或者某几个字段，可以和Cols结合使用。
* 查询记录操作

    查询方法有两个，分为查询单条数据和查询多条数据。单条数据的查询使用Get方法、多条数据的查询使用Find方法。
    
### Count表结构统计功能
在进行表数据查询时，我们时长需要统计数据的条数，比如数据一共多少条，用来做分页处理；再比如统计用户数量，也需要使用到计数功能。框架提供给我们Count方法来实现数据统计功能，如下是一个简单的案例：
```
admin := new(Admin)
count,err := engine.Count(admin)
```
### 事务处理
同其他数据库框架一样，xorm也是支持事物操作的。在有需要的批量操作数据时，事务的使用往往是必要的。在xorm中，事务操作和Session联系在一起。一共三个步骤，分别为：创建session对象，Begin表示事务开始执行，Commit表示提交事务。中间为具体的数据库操作。
###### 创建事务
```
session := engine.NewSession()
defer session.Close()
```
###### 事务开始
```
err := session.Begin()
//事务相关操作
```
###### 事务提交
```
err = session.Commit()
if err != nil{
    panic(err.Error())
}
```
###### 事务回滚
当在执行事务过程中遇到任何错误时，应该及时停止事务，将已经执行的进行回滚。回滚使用的方法是Rollback方法, 只是在执行出现错误时进行回滚操作。
```
...
if err != nil {
    session.Rollback()
    return 
}
```

中间的事务相关操作，与我们的正常的数据库操作相同，支持开发者根据自己需求进行多种操作。比如插入数据和更改输入：
* 事务插入数据

    ```
admin := Admin{Name: "Davie", Status: "1"}
_, err = session.Insert(&admin)
    ```
* 事务修改数据

    ```
    admin := Admin{ Name:"Davie"}
    count,err := session.Id(2).Update(&admin)
    if err != nil {
        seesion.Rollback()
        return
    }
    ```
