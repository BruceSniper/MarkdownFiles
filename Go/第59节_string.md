# 一、字符串(string)

> @author：韩茹
> 版权所有：北京千锋互联科技有限公司

## 1.1 什么是string

Go中的字符串是一个字节的切片。可以通过将其内容封装在“”中来创建字符串。Go中的字符串是Unicode兼容的，并且是UTF-8编码的。

示例代码：

```go
package main

import (  
    "fmt"
)

func main() {  
    name := "Hello World"
    fmt.Println(name)
}
```



## 1.2  string的使用

### 1.2.1 访问字符串中的单个字节

```go
package main

import (  
    "fmt"
)

func main() {  
    name := "Hello World"
    for i:= 0; i < len(s); i++ {
        fmt.Printf("%d ", s[i])
    }
    fmt.Printf("\n")
    for i:= 0; i < len(s); i++ {
        fmt.Printf("%c ",s[i])
    }
}
```

运行结果：

72 101 108 108 111 32 87 111 114 108 100 
H e l l o   W o r l d 





千锋Go语言的学习群：784190273








