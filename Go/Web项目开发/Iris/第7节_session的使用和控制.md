## Session的使用和控制
#### @author：Davie
#### 版权所有：北京千锋互联科技有限公司

在实际的项目开发中，我们会经常有业务场景使用到Session功能。在iris框架中，也为我们提供了方便使用，功能齐全的Session模块。Session模块的源码目录为kataras/iris/sessions包。

##### Session与Cookie的区别
在学习web开发过程中，我们总会和session和cookie打交道。本节课我们学习sesion相关的知识，因此有必要先通过讲解对比一下session和cookie的区别：

* 首先是两者的相同点。session和cookie两者都是用来存储客户的状态信息的手段。在登录、注册等动作后，可以存储相关账户的状态信息，方便程序后续跟踪及使用。
* 其次是不同点，讨论两者的不同点我们从几个角度来总结。首先是两者的存储位置。Cookie是存储在客户端浏览器上，方便客户端请求时使用；Session存储的相关信息存储在服务器端，用于存储客户端连接的状态信息。
* 其次，从可以存储的数据类型来看。Cookie仅仅支持存储字符串string一种数据类型，Session支持int、string、bool等多种数据类型，Session支持的数据类型更全更多。

##### Session对象创建
在实际的程序开发中，iris框架中可以非常方便的创建一个新的session对象。如下所示，即是session的创建：

```
...
sessionID := "mySession"
//session的创建
sess := sessions.New(sessions.Config{
		Cookie: sessionID,
})
```

##### 支持的数据类型
在上文中，我们说过session支持的数据类型要比cookie多，我们来看一下iris框架中的session所支持存储的数据类型：

```
//String：字符串类型
session.GetString()
//Int：无符号整形 及系列相关单位的同类型
session.GetInt()
//Boolean：布尔值类型
session.GetBoolean()
//Float：单精度数值类型 及系列相关单位的同类型
session.GetFloat()
//interface{}：接口 即任意数据结构类型
session.GetFlash()
```
上述代码块，即列出了iris框架中所支持存储的数据类型。我们在接下来的本节课程内容中，将会演示如何进行具体使用。

##### Session的存储和使用

##### Session与数据库结合使用