## MVC包使用

#### @author：Davie
#### 版权所有：北京千锋互联科技有限公司 

在Iris框架中，封装了mvc包作为对mvc架构的支持，方便开发者遵循mvc的开发原则进行开发。

iris框架支持请求数据、模型、持久数据分层处理，并支持各层级模块代码绑定执行。

MVC即：model、view、controller三个部分，分别代表数据层、视图层、控制层。控制器层负责完成页面逻辑、实体层负责完成数据准备与数据操作、视图层负责展现UI效果。
 
在iris框架中，用一张图表示前端请求、服务端处理请求、服务端返回数据到前端的请求过程图，描述如下：

![Iris框架mvc请求过程](/Users/hongweiyu/Desktop/web_mvc_diagram.png)

##### mvc.Application
iris框架中的mvc包中提供了Application结构体定义。开发者可以通过注册自定义的controller来使用对应提供的API，其中包含路由组router.Party,以此用来注册layout、middleware以及相应的handlers等。

##### iris.mvc特性
iris框架封装的mvc包，支持所有的http方法。比如，如果想要提供GET，那么控制器应该有一个名为Get（）的函数，开发者可以定义多个方法函数在同一个Controller中提供。这里的Get、Post方法是指的直接和八种请求类型同名的方法，mvc模块会自动执行到Get()、Post()等八种对应的方法。如下所示：

```
//自定义的控制器
type CustomController struct{}
//注册自定义控制器处理请求
mvc.New(app).Handle(new(CustomController))
//自动处理基础的Http请求
//Url： http://localhost:8000
//Type：GET请求
func (cc *CustomController) Get() mvc.Result{
    //todo
    return mvc.Response{
        ContentType:"text/html",
    }
}
/**
 * Url：http://localhost:8000
 * Type：POST
 **/
func (cc *CustomController) Post() mvc.Result{
    //todo
    return mvc.Response{}
}
```
##### 根据请求类型和请求URL自动匹配处理方法
在iris框架中的mvc设计包中，设定了自定义的控制器以后，支持根据请求类型和对应的URL自动匹配对应的处理方法。具体案例如下：

```
/**
 * url：http://localhost:8000/info
 * type：GET请求
 **/
func (cc *CustomController) GetInfo() mvc.Result{
    //todo
}

/**
 * url：http://localhost:8000/login
 * type：POST
 **/
func (cc *CustomController) PostLogin() mvc.Result{
    //todo
}
```
如上案例，当我们发起请求时，iris框架就能够自动匹配对应的控制器的处理方法。除了上述get和post两个方法之外，http请求的八种类型中的其他请求类型，也支持自动匹配。

##### BeforeActivation方法
在通过Configure和Handle进行了自定义Controller绑定以后，就可以使用自己自定义的Controller来进行自定义处理处理请求方法。开发者可以在BeforeActivation方法中来处理请求定义。如下所示，我们给出案例说明：

```
func （m *CustomController） BeforeActivation(a mvc.BeforeActivation){
    a.Handle("GET","/users/info","QueryInfo")
}
//对应处理请求的方法
func (m *CustomController) QueryInfo() mvc.Result{
    //todo
}
```

##### 使用mvc.Configure配置路由组和控制器
除了使用mvc.new(app)来构建mvc.Application结构体对象和Handle方法来配置处理请求的控制器外，iris框架还支持使用mvc.Configure来配置路由组和控制器的设置。具体使用方法如下：

```
mvc.Configure(app.Party("/user"), func(mvc *mvc.Application) {
		mvc.Handle(new(UserController))
})
```

本节课中我们学习了mvc包中控制器极其处理方法的基本用法，在实战项目中，我们会在本节课学习内容的基础上，继续深入学习更详细的操作。