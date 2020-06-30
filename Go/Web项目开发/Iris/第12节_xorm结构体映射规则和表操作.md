## xorm结构体映射规则和表操作
##### @author：Davie
##### 版权所有：北京千锋互联科技有限公司

上节内容我们学习了基本的xorm框架的知识和基础配置的相关信息。本节课内容我们继续学习相关的知识和相关操作。
### 名称映射规则
名称映射规则主要负责结构体名称到表名和结构体field到表字段的名称映射。
在xorm框架中由core.IMapper接口的实现者来管理，xorm内置了三种IMapper实现：**core.SnakeMapper**,**core.SameMapper**和**core.GonicMapper**。

* SnakeMapper：支持struct为驼峰式命名，表结构中为下划线命名之间的转换。该种规则为xorm默认的Maper；
* SameMapper：映射规则支持结构体名称和对应的表名称以及结构体field名称与对应的表字段名称相同的命名；
* GonicMapper：该映射规则和驼峰式命名类似，但是对于特定词支持性更好，比如ID将会翻译成id，而不是驼峰式的i_d。

默认的名称映射规则为SnakeMapper，如果开发者需要改变时，可以使用创建的数据库引擎对象进行如下设置：

```
engine.SetMapper(core.SameMapper{})
```
另外，可以设置表名和表字段分别为不同的映射规则：
```
engine.SetTableMapper(core.SameMapper{})
engine.SetColumnMapper(core.SnakeMapper{})
```
### 使用Tag的映射规则
如果所有的命名都是按照IMapper的映射来操作的，那当然是最理想的。但是如果碰到某个表名或者某个字段名跟映射规则不匹配时，我们就需要别的机制来改变。
xorm提供了如下几种方式来进行：
* 如果结构体拥有**TableName() string**的成员方法，那么此方法的返回值即是该结构体对应的数据库表名。
* 通过**engine.Table()**方法可以改变struct对应的数据库表的名称，通过sturct中field对应的Tag中使用**xorm:"'column_name'"**可以使该field对应的Column名称为指定名称。这里使用两个单引号将Column名称括起来是为了防止名称冲突，因为我们在Tag中还可以对这个Column进行更多的定义。如果名称不冲突的情况，单引号也可以不使用。

### Column属性定义
我们在field对应的Tag中对Column的一些属性进行定义，用于对我们的项目中的数据库表字段进行设置和限定。定义的方法基本和我们写SQL定义表结构类似。如下所示：

```
type User struct {
    Id   int64
    Name string  `xorm:"varchar(25) notnull unique 'usr_name'"`
}
```
xorm中对数据类型有自己的定义，具体的Tag规则如下，另Tag中的关键字均不区分大小写：

| name | 当前field对应的字段的名称  |
| --- | --- | --- |
| pk | 是否是Primary Key | 
| name | 当前field对应的字段的名称 |
| pk   | 是否是Primary Key       |
| autoincr | 是否是自增 |
| [not ]null 或 notnull | 是否可以为空 |
| unique | 是否是唯一 |
| index | 是否是索引 |
| extends | 应用于一个匿名成员结构体或者非匿名成员结构体之上 | 
| - | 这个Field将不进行字段映射 |
| -> | Field将只写入到数据库而不从数据库读取 |
| <- | Field将只从数据库读取，而不写入到数据库 |
| created | Field将在Insert时自动赋值为当前时间 |
| updated | Field将在Insert或Update时自动赋值为当前时间 |
|deleted | Field将在Delete时设置为当前时间，并且当前记录不删除 |
| version | Field将会在insert时默认为1，每次更新自动加1 |
| default 0或default(0) | 设置默认值，紧跟的内容如果是Varchar等需要加上单引号 |
| json | 表示内容将先转成Json格式 |

### 字段映射规则
除了上述表名的映射规则和使用Tag对字段进行设置以外，基础的Go语言结构体数据类型也会对应到数据库表中的字段中，具体的一些数据类型对应规则如下：

| Go语言数据类型 | xorm 中的类型 |
| -------------| -------------|
| implemented Conversion | Text |
| int, int8, int16, int32, uint, uint8, uint16, uint32 | Int |
| int64, uint64 | BigInt |
| float32 | Float |
| float64 | Double |
| complex64, complex128 | Varchar(64) |
| []uint8 | Blob |
| array, slice, map except []uint8 | Text |
| bool | Bool |
| string | Varchar(255) |
| time.Time | DateTime |
| cascade struct | BigInt |
| struct | Text |
| Others | Text |

### 表基本操作
* 创建表：CreateTables(),参数为一个或多个空的对应Struct的指针。
* 判断表是否为空：IsTableEmpty()
* 判断表是否存在：IsTableExist()
* 删除表：DropTables()，参数为一个或多个空的对应Struct的指针或者表的名字。

### 基本和统计操作
查询和统计主要使用Get, Find, Count, Rows, Iterate这几个方法，以及条件查询Where。

具体的编程使用方法我们在视频和程序中会给大家详细使用，这是我们实战项目的重点内容。

