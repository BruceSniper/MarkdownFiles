## GoWeb开发_Iris框架
#### @author：Davie
#### 版权所有：北京千锋互联科技有限公司

### Golang介绍
Go语言是谷歌推出的一种全新的编程语言，可以在不损失应用程序性能的情况下降低代码的复杂性。谷歌首席软件工程师罗布派克(Rob Pike)说：我们之所以开发Go，是因为过去10多年间软件开发的难度令人沮丧。  
谷歌资深软件工程师罗布·派克(Rob Pike)表示，“Go让我体验到了从未有过的开发效率。”派克表示，和今天的C++或C一样，Go是一种系统语言。他解释道，“使用它可以进行快速开发，同时它还是一个真正的编译语言，我们之所以现在将其开源，原因是我们认为它已经非常有用和强大。”  

Golang语言的一些的功能：  

* 具有现代的程序语言特色，如垃圾回收，帮助程序设计师处理琐碎和重要的内存管理等问题。Go的速度也非常快，几乎和C或C++程序一样快，且能够快速制作程序。
* 该软件是专为构建服务器软件所设计（如Google的Gmail），Google认为Go还可应用到其他领域，包括在浏览器内执行软件，取代JavaScript的角色。  
* Go也可解决现今的一大挑战：多核心处理器。一般电脑程序通常依序执行，一次进行一项工作，但多核心处理器更适合并行处理许多工作。

相较于其他语言，Golang之所以发展迅速，与该语言特有的特色密不可分：  

* 简洁 快速 安全
* 并行 有趣 开源
* 内存管理，数组安全，编译迅速

### Iris简介
Iris是一款Go语言中用来开发web应用的框架，该框架支持编写一次并在任何地方以最小的机器功率运行，如Android、ios、Linux和Windows等。该框架只需要一个可执行的服务就可以在平台上运行了。  

Iris框架以简单而强大的api而被开发者所熟悉。iris除了为开发者提供非常简单的访问方式外，还同样支持MVC。另外，用iris构建微服务也很容易。  

在iris框架的官方网站上，被称为速度最快的Go后端开发框架。在Iris的网站文档上，列出了该框架具备的一些特点和框架特性，列举如下：  

1）聚焦高性能   
2）健壮的静态路由支持和通配符子域名支持  
3）视图系统支持超过5以上模板  
4）支持定制事件的高可扩展性Websocket API  
5）带有GC, 内存 & redis 提供支持的会话  
6）方便的中间件和插件  
7）完整 REST API  
8）能定制 HTTP 错误  
9）源码改变后自动加载  
等等还有很多特性，大家可以参考Iris官方文档。在GoWeb开发的诸多框架中，各个维度的性能比较如下：
 
 ![Iris与其他语言的框架性能对比](http://7xtcwd.com1.z0.glb.clouddn.com/Go语言性能对比.png)
 
 ![GoWeb各框架开发效率对比](http://7xtcwd.com1.z0.glb.clouddn.com/Go语言web框架对比.png)
 
 
### Iris框架学习渠道
在学习Iris框架过程时，我们需要有相应的配套资料才能够完成我们的学习。下面是学习Iris框架过程中可能会用到的资料。  

1) Iris官网：[https://iris-go.com/](https://iris-go.com/)  
2) Iris框架源码地址：[https://github.com/kataras/iris](https://github.com/kataras/iris)  
3) Iris框架中文学习文档： [https://studyiris.com/doc/](https://studyiris.com/doc/) 
 
当然，还有其他相关资料，比如说xorm框架等，这些我们在后面的课程文档中学习到以后再做解释和说明。  

### Iris框架安装
**环境要求：**iris框架要求golang版本至少为1.8。各位同学可以通过打开终端，执行：go version 命令来查看自己机器的go环境版本。 
 
安装Iris框架非常简单，使用go语言的全局安装第三方代码的命令get即可。安装Iris框架的命令如下：    

```  
go get -u github.com/kataras/iris
```

在本地终端中执行如上的安装命令，等待命令执行成功，即表示Iris源码下载安装完成。安装完成Iris框架以后，能够在本地机器的GoPath环境目录中的src/github.com/目录下找到iris框架对应的包名，如下图所示：  

![Iris框架源码安装图片](http://7xtcwd.com1.z0.glb.clouddn.com/Iris源码结构.png)

如图所示的kataras/iris所在的目录就是iris框架的源码，如上图所示即是安装成功。  

### 源码案例
在iris源码安装完成以后，iris框架为开发者提供了自己学习的实战案例，供开发者自行学习。iris提供的案例在iris框架目录中的_example目录下，在学习时可以进行参考。

接下来我们就可以开始学习iris的相关内容，进行代码开发了。

### Iris构造服务实例  
在安装完成Iris的源码后，我们就开始来编写最简单的一个Iris的服务。在Iris中，构建并运行一个服务实例需要两步：  

* 1、通过iris.New()方法可以实例化一个应用服务对象app  
* 2、通过Run方法开启端口监听服务，运行服务实例

如下是一个最简单的服务案例Demo

```
package main

import "github.com/kataras/iris"

func main() {
	//1.创建app结构体对象
	app := iris.New()
	//2.端口监听
	app.Run(iris.Addr(":7999"), iris.WithoutServerError(iris.ErrServerClosed))

	////application.Run(iris.Addr(":8080"))//第一种
	//application.Run(iris.Addr(":8080"), iris.WithoutServerError(iris.ErrServerClosed)) //第二种

}
```

