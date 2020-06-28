## Iris框架设置操作

#### @author:Davie
#### 版权所有：北京千锋互联科技有限公司  

## 路由组的使用  
在实际开发中，我们通常都是按照模块进行开发，同一模块的不同接口url往往是最后的一级url不同，具有相同的前缀url。因此，我们期望在后台开发中，可以按照模块来进行处理我们的请求，对于这种需求，iris框架也是支持的。

```
usersRouter := app.Party("/admin", userMiddleware)
```

如上述代码所示，iris框架中使用app.Party方法来对请求进行分组处理，第二个参数是处理路由组的中间件方法，通常情况下我们会在中间件中写context.Next()方法。


### 应用程序内代码配置

在iris框架开发中，初始化应用程序时已经使用了默认的配置值。作为开发者，我们可以不需要其他额外的配置就启动我们的应用程序。  

如果开发者想要自己根据自己的需求进行配置，iris框架也是支持的，本节课我们来学习一下iris框架所支持的配置方式。  

现在主流的配置文件格式有：xml、yaml、 cnf、toml、json等等格式。xml现在使用的已经不多，cnf格式的配置文件适合数据库的配置文件，在本节内容中，我们将带大家学习多种配置文件的使用方法。
 


在iris程序的全局app实例中，支持通过多种方式进行代码配置，途径是多样的：  

* 1、使用app.Configure(iris.WithConfiguration(iris.Configuration{DisableStartuplog:false}))来对整体应用进行配置项配置  

* 2、通过app.Run方法的第二个参数来进行相关的自定义配置项的配置，第二个参数的类型同1一致。  

以上两种方式，无论哪种方式，都是对app服务应用进行Configuration配置，提供应用配置的Configuration结构体定义所支持的配置项分别为：

* DisableInterruptHandler：如果设置为true，当人为中断程序执行时，则不会自动正常将服务器关闭。如果设置为true，需要自己自定义处理。默认为false。  
* DisablePathCorrection： 该配置项表示更正并将请求的路径重定向到已注册的路径。比如：如果请求/home/ 但找不到此Route的处理程序，然后路由器检查/home处理程序是否存在，如果是，（permant）将客户端重定向到正确的路径/home。默认为false。 
* EnablePathEscape：该配置选项用于配置是否支持路径转义。适用于请求url中包含转义字符时进行配置。默认为false。  
* FireMethodNotAllowed： 默认为false。 
* DisableBodyConsumptionOnUnmarshal：该设置选项用于配置读取请求数据的方法是否使用，如果设置为true，则表示禁用context.UnmarshalBody，context. ReadJSON以及context.ReadXML。默认为false。
* DisableAutoFireStatusCode：该配置变量为控制是否处理错误自动执行，如果为true，则不会进行错误自动执行。该配置项默认为false。
* TimeFormat：时间格式。默认格式为："Mon, 02 Jan 2006 15:04:05 GMT"  
* Charset：字体格式选项。默认字体为："UTF-8"

### 通过TOML配置文件进行配置  
**什么是toml?**  
toml是Tom’s Obvious, Minimal Language的缩写， toml是一种配置文件。TOML是前GitHub CEO， Tom Preston-Werner，于2013年创建的语言，其目标是成为一个小规模的易于使用的语义化配置文件格式。TOML被设计为可以无二义性的转换为一个哈希表(Hash table)。  

具体的项目配置使用中，我们需要创建config.tml类型的配置文件，并在程序中明确使用toml文件进行读取配置内容。如下图所所示：  

```
app.Configure(iris.WithConfiguration(iris.TOML("./configs/iris.tml")))
```

### 通过YAML配置文件  
YAML 是专门用来写配置文件的语言，写法简洁、功能强大，比JSON格式还要方便。Yaml实质上是一种通用的数据串行化格式。Yaml的主要语法格式有以下几项：  

* 大小写敏感。
* 使用缩进表示层级关系。
* 缩进时不允许使用Tab键，只允许使用空格。
* 缩进的空格数目不受限制，相同层级的配置元素	左侧对齐即可。  

在本节内容中，我们可以通过yaml配置文件来对应用进行简单选项的的配置：  

```
app.Configure(iris.WithConfiguration(iris.))
```

### 通过读取自定义配置文件
这里我们给大家演示如何使用json格式的配置文件来进行应用的配置，然后从应用程序中进行读取。  

首先创建json格式的配置文件，并编写配置项，如下图：  

```
{
  "appname": "IrisDemo",
  "port": 8000
}
```

在应用程序内，编程实现对配置文件的读取和解析，如下图：  

```
file, _ := os.Open("/Users/hongweiyu/go/src/irisDemo/5-路由组及Iris配置/config.json")
defer file.Close()

decoder := json.NewDecoder(file)
conf := Coniguration{}
err := decoder.Decode(&conf)
if err != nil {
	fmt.Println("Error:", err)
}
fmt.Println(conf.Port)
```

本节课我们带大家学习了在iris框架中如何使用路由组和对应用进行相关的配置的内容，本节课学习的内容我们在实战项目中都能能够用到。