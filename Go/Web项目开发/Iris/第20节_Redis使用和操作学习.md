## Redis介绍安装和使用
###### @author：Davie
###### 版权所有：北京千锋互联科技有限公司

### Redis的操作和使用
在安装好redis以后，我们这里给大家讲一下redis操作的一些知识。
Redis支持的数据类型：**string**，**hash**，**list**，**set**，**sorted set**
我们来练习一下redis的使用：

* **字符串String：**string类型是redis最基本的类型，一个key对应一个value。redis的string可以包含任何数据，比如jpg图片，或者序列化的对象，都可以存储。string类型最大的能够存储512MB。

    1）存储String操作：**set key value**
    2）获取String操作：**get key**
* **哈希Hash：**Redis Hash是一个（key=>value)对集合。
    1）设置hash操作：**hmset keyname  field1 "hello" field2 "world"**
    2）获取hash操作：**hget keyname field1**
    
* **列表List：**按照插入顺序保存字符串列表，有顺序，支持push操作。
1）添加list字符操作：**lpush keyname value1**
2）获取list字符操作：**lrange keyname start stop ** ( 既包含start，也包含stop）

* **Set（集合）：**Redis中的Set是string类型的无序集合。集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1）
    1）添加操作：**sadd setname value1 value2 ....**
    2）获取操作：**smember setname**
    
* **zset（sorted set：有序集合）：**zset和set一样，都是存储string类型的集合，且都不允许重复；但是区别是zset是为每一个元素都关联一个double类型的分数，并使用该分数对集合成员进行从小到大的排序。
    1）添加元素操作：**zadd key score member**
    2）获取zset元素：**zrangebyscore key score**
    


