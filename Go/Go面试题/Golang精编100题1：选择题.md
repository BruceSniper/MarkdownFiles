# Golang精编100题1：选择题

1.【初级】下面属于关键字的是（）
A. func
B. def
C. struct
D. class

参考答案：AC

2.【初级】定义一个包内全局字符串变量，下面语法正确的是（）
A. var str string
B. str := “”
C. str = “”
D. var str = “”

参考答案：AD

3.【初级】通过指针变量 p 访问其成员变量 name，下面语法正确的是（）
A. p.name
B. (*p).name
C. (&p).name
D. p->name

参考答案：AB

4.【初级】关于接口和类的说法，下面说法正确的是（）
A. 一个类只需要实现了接口要求的所有函数，我们就说这个类实现了该接口
B. 实现类的时候，只需要关心自己应该提供哪些方法，不用再纠结接口需要拆得多细才合理
C. 类实现接口时，需要导入接口所在的包
D. 接口由使用方按自身需求来定义，使用方无需关心是否有其他模块定义过类似的接口

参考答案：ABD

5.【初级】关于字符串连接，下面语法正确的是（）
A. str := ‘abc’ + ‘123’
B. str := “abc” + “123”
C. str ：= ‘123’ + “abc”
D. fmt.Sprintf(“abc%d”, 123)

参考答案：BD

6.【初级】关于协程，下面说法正确是（）
A. 协程和线程都可以实现程序的并发执行
B. 线程比协程更轻量级
C. 协程不存在死锁问题
D. 通过channel来进行协程间的通信

参考答案：AD

7.【中级】关于init函数，下面说法正确的是（）
A. 一个包中，可以包含多个init函数
B. 程序编译时，先执行导入包的init函数，再执行本包内的init函数
C. main包中，不能有init函数
D. init函数可以被其他函数调用

参考答案：AB

8.【初级】关于循环语句，下面说法正确的有（）
A. 循环语句既支持for关键字，也支持while和do-while
B. 关键字for的基本使用方法与C/C++中没有任何差异
C. for循环支持continue和break来控制循环，但是它提供了一个更高级的break，可以选择中断哪一个循环
D. for循环不支持以逗号为间隔的多个赋值语句，必须使用平行赋值的方式来初始化多个变量

参考答案：CD

9.【中级】对于函数定义：

```go
func add(args ...int) int {
    sum :=0
    for _,arg := range args {
        sum += arg
    }
    returnsum
}
```

下面对add函数调用正确的是（）
A. add(1, 2)
B. add(1, 3, 7)
C. add([]int{1, 2})
D. add([]int{1, 3, 7}…)

参考答案：ABD

16.【初级】关于类型转化，下面语法正确的是（）
A.
```go
type MyInt int
var i int = 1
jMyInt = i
```

B.
```go
type MyInt int
var i int= 1
var jMyInt = (MyInt)i
```

C.
```go
type MyInt int
var i int= 1
var jMyInt = MyInt(i)
```

D.
```go
type MyInt int
var i int= 1
var jMyInt = i.(MyInt)
```
参考答案：C

19.【初级】关于局部变量的初始化，下面正确的使用方式是（）
A. var i int = 10
B. var i = 10
C. i := 10
D. i = 10

参考答案：ABC

20.【初级】关于const常量定义，下面正确的使用方式是（）
A.
```go
const Pi float64 = 3.14159265358979323846
const zero= 0.0
```

B.
```go
const (
    size int64= 1024
    eof = -1
)
```

C.
```go
const (
    ERR_ELEM_EXISTerror = errors.New("element already exists")
    ERR_ELEM_NT_EXISTerror = errors.New("element not exists")
)
```

D.
```go
const u, vfloat32 = 0, 3
const a,b, c = 3, 4, "foo"
```

参考答案：ABD

22.【初级】关于布尔变量b的赋值，下面错误的用法是（）
A. b = true
B. b = 1
C. b = bool(1)
D. b = (1 == 2)

参考答案：BC

23.【中级】下面的程序的运行结果是（）

```go
func main() {  
    if (true) {
       defer fmt.Printf("1")
    } else {
       defer fmt.Printf("2")
    }
    fmt.Printf("3")
}
```

A. 321
B. 32
C. 31
D. 13

参考答案：C

31.【初级】关于switch语句，下面说法正确的有（）
A. 条件表达式必须为常量或者整数
B. 单个case中，可以出现多个结果选项
C. 需要用break来明确退出一个case
D. 只有在case中明确添加fallthrough关键字，才会继续执行紧跟的下一个case

参考答案：BD

32.【中级】 golang中没有隐藏的this指针，这句话的含义是（）
A. 方法施加的对象显式传递，没有被隐藏起来
B. golang沿袭了传统面向对象编程中的诸多概念，比如继承、虚函数和构造函数
C. golang的面向对象表达更直观，对于面向过程只是换了一种语法形式来表达
D. 方法施加的对象不需要非得是指针，也不用非得叫this

参考答案：ACD

33.【中级】 golang中的引用类型包括（）
A. 数组切片
B. map
C. channel
D. interface

参考答案：ABCD