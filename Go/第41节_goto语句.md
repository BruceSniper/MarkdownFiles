# 一、goto语句

goto：可以无条件地转移到过程中指定的行。

语法结构：

```go
goto label;
..
..
label: statement;
```



![goto1](http://7xtcwd.com1.z0.glb.clouddn.com/goto1.jpg)

```go
package main

import "fmt"

func main() {
   /* 定义局部变量 */
   var a int = 10

   /* 循环 */
   LOOP: for a < 20 {
      if a == 15 {
         /* 跳过迭代 */
         a = a + 1
         goto LOOP
      }
      fmt.Printf("a的值为 : %d\n", a)
      a++     
   }  
}
```



统一错误处理
多处错误处理存在代码重复时是非常棘手的，例如：

```go
		err := firstCheckError()
    if err != nil {
        goto onExit
    }
    err = secondCheckError()
    if err != nil {
        goto onExit
    }
    fmt.Println("done")
    return
onExit:
    fmt.Println(err)
    exitProcess()



```






千锋Go语言的学习群：784190273
