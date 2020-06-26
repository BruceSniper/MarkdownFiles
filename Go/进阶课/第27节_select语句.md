# select语句

> @author：韩茹
>
> 版权所有：北京千锋互联科技有限公司

select 是 Go 中的一个控制结构。select 语句类似于 switch 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。

## 一、语法结构

select语句的语法结构和switch语句很相似，也有case语句和default语句：

```go
select {
    case communication clause  :
       statement(s);      
    case communication clause  :
       statement(s); 
    /* 你可以定义任意数量的 case */
    default : /* 可选 */
       statement(s);
}
```

说明：

- 每个case都必须是一个通信

- 所有channel表达式都会被求值

- 所有被发送的表达式都会被求值

- 如果有多个case都可以运行，select会随机公平地选出一个执行。其他不会执行。 

- 否则：

  如果有default子句，则执行该语句。

  如果没有default字句，select将阻塞，直到某个通信可以运行；Go不会重新对channel或值进行求值。



## 二、示例代码

示例代码：

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	/*
	分支语句：if，switch，select
	select 语句类似于 switch 语句，
		但是select会随机执行一个可运行的case。
		如果没有case可运行，它将阻塞，直到有case可运行。
	 */

	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		time.Sleep(2 * time.Second)
		ch2 <- 200
	}()
	go func() {
		time.Sleep(2 * time.Second)
		ch1 <- 100
	}()

	select {
	case num1 := <-ch1:
		fmt.Println("ch1中取数据。。", num1)
	case num2, ok := <-ch2:
		if ok {
			fmt.Println("ch2中取数据。。", num2)
		}else{
			fmt.Println("ch2通道已经关闭。。")
		}


	}
}

```

运行结果：可能执行第一个case，打印100，也可能执行第二个case，打印200。(多运行几次，结果就不同了)



![WX20190816-104608](/Users/ruby/Documents/千锋教育/视频/Go语言进阶视频/第29节_select语句/img/WX20190816-104608.png)



select语句结合time包的和chan相关函数，示例代码：

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	//go func() {
	//	ch1 <- 100
	//}()

	select {
	case <-ch1:
		fmt.Println("case1可以执行。。")
	case <-ch2:
		fmt.Println("case2可以执行。。")
	case <-time.After(3 * time.Second):
		fmt.Println("case3执行。。timeout。。")

	//default:
	//	fmt.Println("执行了default。。")
	}
}

```



运行结果：

![WX20190816-104450](img/WX20190816-104450.png)













千锋Go语言的学习群：784190273

github知识库：

https://github.com/rubyhan1314

Golang网址：

https://www.qfgolang.com/



作者B站：

https://space.bilibili.com/353694001

对应视频地址：

https://www.bilibili.com/video/av56018934

https://www.bilibili.com/video/av47467197

源代码：

https://github.com/rubyhan1314/go_goroutine



