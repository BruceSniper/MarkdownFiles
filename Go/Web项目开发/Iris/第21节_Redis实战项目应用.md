## Redis实战项目应用

**@author：Davie**
**版权所有：千锋互联科技有限公司**

上节内容讲解了如何安装Redis，如何使用Redis以及Redis的操作。本节内容，继续来学习在真实的项目案例中，Redis的使用方法和操作步骤。

### 项目Redis配置
在实战项目中使用Redis功能，首先需要进行Redis配置。本实战项目中，关与Redis的配置项包含：**连接类型**、**地址**、**端口**、**公共前缀**。以上配置项被定义包含在Iris框架的redis包中的**Config**结构体中，**Config**定义如下：

```
type Config struct {
	// Network "tcp"
	Network string
	// Addr "127.0.0.1:6379"
	Addr string
	// Password string .If no password then no 'AUTH'. Default ""
	Password string
	// If Database is empty "" then no 'SELECT'. Default ""
	Database string
	// MaxIdle 0 no limit
	MaxIdle int
	// MaxActive 0 no limit
	MaxActive int
	// IdleTimeout  time.Duration(5) * time.Minute
	IdleTimeout time.Duration
	// Prefix "myprefix-for-this-website". Default ""
	Prefix string
}
```

* **Network：** 连接类型。TCP

* **Addr：** 即将连接的Redis服务主机IP。本实战项目的Redis服务部署在本机，因此主机ip为127.0.0.1。Redis服务默认端口为6379。因此，Addr在本实例项目中的配置值为127.0.0.1:6379。

* **Password：** 登陆Redis的密码。默认配置为空。

* **Prefix：**为要保存的所有的内容设置公共的前缀。默认设置为空。

* **IdleTimeout：**设置Redis中的生效时长。这里我们设置time.Duration(24) * time.Hour。在实际的开发过程中，开发者可以根据自己的需求设定Redis的生效时长。

Redis在配置文件中的配置情况如下：

```
{
  "app_name": "CmsProject",
  "port": "8080",
  "static_path": "/manage/static",
  "database": {
    "drive": "mysql",
    "port": "3306",
    "user": "root",
    "pwd": "271400",
    "database": "qfCms"
  },
  "redis": {
    "network": "tcp",
    "addr": "127.0.0.1",
    "port": "6379",
    "prefix": ""
  },
  "mode": "dev"
}
```

### Redis连接对象实例化
我们通过读取配置文件完成配置内容的读取，利用Redis配置信息实例化Redis对象，Redis实例化如下：
```

var once sync.Once

/**
 * 返回Redis实例
 */
func NewRedis() *redis.Database {

	var database *redis.Database

	once.Do(func() {
		//项目配置
		cmsConfig := config.InitConfig()
		rd := cmsConfig.Redis
		database = redis.New(service.Config{
			Network:     rd.NetWork,
			Addr:        rd.Addr + ":" + rd.Port,
			IdleTimeout: time.Duration(24) * time.Hour,
			Prefix:      rd.Prefix,
		})
	})
	
	return database
}

```
Redis的实例化使用到了单例方式实现。



### 将Session存储方式设置为Redis
```
redis := datasource.NewRedis()
//设置session的同步位置为redis
sessManager.UseDatabase(redis)
```
### 实战项目中Redis的操作与实现
* Redis缓存管理员统计功能
    
    ```
    adminStatis := sc.Session.Get(ADMINMODULE + date)
		if adminStatis != nil {
			adminStatis = adminStatis.(int64)
			return mvc.Response{
				Object: map[string]interface{}{
					"status": utils.RECODE_OK,
					"count":  adminStatis,
				},
			}
		} else {
			result = sc.Service.GetAdminDailyCount(date)
			sc.Session.Set(ADMINMODULE, result)
		}
    ```
    
* Redis缓存订单统计功能
    
    ```
    orderStatis := sc.Session.Get(ORDERMODULE + date)

		if orderStatis != nil {
			orderStatis = orderStatis.(int64)
			return mvc.Response{
				Object: map[string]interface{}{
					"status": utils.RECODE_OK,
					"count":  orderStatis,
				},
			}
		} else {
			result = sc.Service.GetOrderDailyCount(date)
			sc.Session.Set(ORDERMODULE+date, result)
		}

    ```
    
* Redis缓存用户统计功能
    ```
    userResult := sc.Session.Get(USERMODULE + date)
		if userResult != nil {
			result = userResult.(int64)
			return mvc.Response{
				Object: map[string]interface{}{
					"status": utils.RECODE_OK,
					"count":  userResult,
				},
			}
		} else {
			iris.New().Logger().Error(date) //时间
			result = sc.Service.GetUserDailyCount(date)
			//设置缓存
			sc.Session.Set(USERMODULE+date, result)
		}
    ```

###  查看Redis存储效果
* 开启Redis服务
  在Mac下，启动redis服务使用如下命令：**redis**
![Mac下启动Redis服务](http://7xtcwd.com1.z0.glb.clouddn.com/启动Redis服务.png)
* 开启Redis-cli客户端
在MacOS系统下，启动redis-cli工具的命令：**redis-cli**
![启动Redis-cli客户端](http://7xtcwd.com1.z0.glb.clouddn.com/Redis-cli客户端.png)
如上我们可以通过**keys**命令来查看我们存储的所有的内容
* get key读取具体信息
在查询所对应的key的redis存储内容值。



