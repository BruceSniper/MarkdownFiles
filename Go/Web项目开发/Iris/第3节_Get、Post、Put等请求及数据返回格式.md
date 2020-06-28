## Get、Post、Put等请求及数据返回格式
#### @author：Davie
#### 版权所有：北京千锋互联科技有限公司

### 数据请求方式的分类
所有的项目中使用的请求都遵循HTTP协议标准，HTTP协议经过了1.0和1.1两个版本的发展。 
  
* HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法。
* HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。

因此，我们可以说，HTTP协议一共定义了八种方法用来对Request-URI网络资源的不同操作方式，这些操作具体为：GET、POST、PUT、DELETE、HEAD、OPTIONS、TRACE、CONNECT等八种操作方式。  
	

### Iris框架的请求处理方式  

* 1、Iris框架中服务实例app中包含多个方法，用来支持对上述HTTP多种请求类型的直接处理，直接定义为get方法、post方法、put方法等，app中包含的自动处理路由请求的方法与http请求类型的分类一致。

* 2、除了上述1中自动处理各类别的请求外，框架还支持使用通用的Handle方法来自定义编写自己的请求处理类型及对应的方法。  

两种路由请求的处理方式示例如下：  

```
app := iris.New()

//url: http://localhost:8000/getRequest
//type：GET请求
app.Get("/getRequest", func(context context.Context) {
		path := context.Path()
		app.Logger().Info(path)
})

//url: http://localhost:/user/info
//type：POST请求
app.Handle("POST", "/user/info", func(context context.Context) {
		context.WriteString(" User Info is Post Request , Deal is in handle func ")
})

//启动端口监听服务
app.Run(iris.Addr(":8000"))

```

#### GET请求
向特定的网络资源数据发起请求。GET请求可以携带请求数据，携带的请求数据会以？分割URL和传输数据，参数之间以&相连，比如http://localhost:3000?name=davie&pwd=123。  
如下是一个http的get类型的请求：  

```
http://localhost:8000/userpath
```

服务端的路由处理方式如下：  

```
//url：http://localhost:8000/userpath
//type：GET请求、用GET方法处理
app.Get("/userpath", func(context context.Context) {

		//获取Path
		path := context.Path()
		//日志输出
		app.Logger().Info(path)
		//写入返回数据：string类型
		context.WriteString("请求路径：" + path)
})
```

上述为使用已经封装的默认的app.Get方式来处理请求，使用Handle方法来进行处理，如下所示：  

```
//url：http://localhost:8000/hello
//type：GET请求、Handle方法第一个参数为GET，表明是GET请求方式
app.Handle("GET", "/hello", func(context context.Context) {
		context.HTML("<h1> Hello world. </h1>")
})
```

#### POST请求
POST请求在进行请求时会将请求数据放在请求body中进行请求，请求数据大小没有限制。在开发过程中，我们使用postman工具来进行POST请求的调试。  
POST请求的示例如下所示：  

```
http://localhost:8000/postLogin
```

服务端的路由处理方式如下：  

```
//type：POST请求
//携带数据：name、pwd命名的请求数据
app.Post("/postLogin", func(context context.Context) {
		//获取请求path
		path := context.Path()
		//日志
		app.Logger().Info(path)
		//获取请求数据字段
		name := context.PostValue("name")
		pwd, err := context.PostValueInt("pwd")
		if err != nil {
			panic(err.Error())
		}
		app.Logger().Info(name, "  ", pwd)
		//返回
		context.HTML(name)
})
```

上述为使用默认路由请求方法Post方法来进行处理，同时，还可以使用Handle方法来进行处理，如下图： 

```
//url：http://localhost:8000/user/info
//type：POST请求，Handle方法第一个参数为POST，表明是Post请求
app.Handle("POST", "/user/info", func(context context.Context) {
		context.WriteString(" User Info is Post Request , Deal is in handle func ")
})
```

#### PUT、DELETE、OPTIONS、HEAD等其他类型请求  
除了上述GET、POST最为常见的两种请求方式以外，还有PUT、DELETE、OPTIONS、HEAD等其他类型请求，对于其他类型的请求，如同GET和POST请求一样，都是可以通过两种方式来进行处理：  

* 1、iris框架提供的自动识别请求类型的处理请求方法，如put方法、head方法、options方法、delete方法等

* 2、使用通用的Handle方法对路由请求进行处理，开发者自己选择具体的请求类型以、对应url和要进行处理的func。  

如下是put和delete的请求处理：   
**PUT请求** 

```
//type：PUT类型请求
app.Put("/putinfo", func(context context.Context) {
		path := context.Path()
		app.Logger().Info("请求url：", path)
})
```
**DELETE请求**

```
//type：DELETE类型请求  
app.Delete("/deleteuser", func(context context.Context) {
		path := context.Path()
		app.Logger().Info("Delete请求url：", path)
})
```

### 请求处理的数据格式返回  
在本节课程中，我们已经学习了如何对不同类型的请求进行处理以及如何获取请求所携带的数据，当后台接收到请求后，将会对请求进行处理，处理完毕后将数据返回给请求的客户端。接下来，我们看一看如何将数据进行返回，以及都有哪些形式。  

在进行请求处理时，处理方法func有一个参数context。Context是用于处理请求的上下文环境变量，用于处理http请求及相关数据返回。iris框架支持多种数据格式的返回，此处我们学习掌握返回string、json、xml以及html格式的数据。

#### 返回string类型数据   

```
context.WriteString("hello world")
``` 
 
#### 返回json格式的数据  
```
context.JSON(iris.Map{"message": "hello word", "requestCode": 200})
```

#### 返回xml格式的数据  
```
context.XML(Person{Name: "Davie", Age: 18})
```

#### 返回html格式数据  
```
context.HTML("<h1> Davie, 12 </h1>")
```

通过本节课的内容，我们学习了iris框架中的不同类型的数据请求以及返回不同的数据格式。

