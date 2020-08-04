# Golang精编100题3：判断题

1.【初级】数组是一个值类型（）

参考答案：T

2.【初级】使用map不需要引入任何库（）

参考答案：T

3.【中级】内置函数delete可以删除数组切片内的元素（）

参考答案：F

4.【初级】指针是基础类型（）

参考答案：F

5.【初级】 interface{}是可以指向任意对象的Any类型（）

参考答案：T

6.【中级】下面关于文件操作的代码可能触发异常（）
```go
file, err := os.Open("test.go")
defer file.Close()
if err != nil {
 fmt.Println("open file failed:",err)
 return
}
...
```

参考答案：T

13.【初级】 Golang不支持自动垃圾回收（）

参考答案：F

14.【初级】 Golang支持反射，反射最常见的使用场景是做对象的序列化（）

参考答案：T

15.【初级】 Golang可以复用C/C++的模块，这个功能叫Cgo（）

参考答案：F

16.【初级】下面代码中两个斜点之间的代码，比如json:“x”，作用是X字段在从结构体实例编码到JSON数据格式的时候，使用x作为名字，这可以看作是一种重命名的方式（）

```go
type Position struct {
    X int `json:"x"`
    Y int `json:"y"`
    Z int `json:"z"`
}
```

参考答案：T

21.【初级】通过成员变量或函数首字母的大小写来决定其作用域（）

参考答案：T

22.【初级】对于常量定义zero(const zero = 0.0)，zero是浮点型常量（）

参考答案：T

23.【初级】对变量x的取反操作是~x（）

参考答案：F

24.【初级】下面的程序的运行结果是xello（）

```go
func main() {
    str := "hello"
    str[0] = 'x'
    fmt.Println(str)
}
```

参考答案：F

29.【初级】 golang支持goto语句（）

参考答案：T

30.【初级】下面代码中的指针p为野指针，因为返回的栈内存在函数结束时会被释放（）

```go
type TimesMatcher struct {
    base int
    }
    func NewTimesMatcher(base int) *TimesMatcher{
    return &TimesMatcher{base:base}
    }
    func main() {
    p := NewTimesMatcher(3)
    ...
}
```
参考答案：F

40.【初级】匿名函数可以直接赋值给一个变量或者直接执行（）

参考答案：T

41.【初级】如果调用方调用了一个具有多返回值的方法，但是却不想关心其中的某个返回值，可以简单地用一个下划线“_”来跳过这个返回值，该下划线对应的变量叫匿名变量（）

参考答案：T

42.【初级】在函数的多返回值中，如果有error或bool类型，则一般放在最后一个（）

参考答案：T

43.【初级】错误是业务过程的一部分，而异常不是（）

参考答案：T

44.【初级】函数执行时，如果由于panic导致了异常，则延迟函数不会执行（）

参考答案：F

45.【中级】当程序运行时，如果遇到引用空指针、下标越界或显式调用panic函数等情况，则先触发panic函数的执行，然后调用延迟函数。调用者继续传递panic，因此该过程一直在调用栈中重复发生：函数停止执行，调用延迟执行函数。如果一路在延迟函数中没有recover函数的调用，则会到达该携程的起点，该携程结束，然后终止其他所有携程，其他携程的终止过程也是重复发生：函数停止执行，调用延迟执行函数（）

参考答案：F

46.【初级】同级文件的包名不允许有多个（）

参考答案：T

47.【中级】可以给任意类型添加相应的方法（）

参考答案：F

48.【初级】 golang虽然没有显式的提供继承语法，但是通过匿名组合实现了继承（）

参考答案：T

49.【初级】使用for range迭代map时每次迭代的顺序可能不一样，因为map的迭代是随机的（）

参考答案：T

50.【初级】 switch后面可以不跟表达式（）

参考答案：T

51.【中级】结构体在序列化时非导出变量（以小写字母开头的变量名）不会被encode，因此在decode时这些非导出变量的值为其类型的零值（）

参考答案：T

52.【初级】 golang中没有构造函数的概念，对象的创建通常交由一个全局的创建函数来完成，以NewXXX来命名（）

参考答案：T

53.【中级】当函数deferDemo返回失败时，并不能destroy已create成功的资源（）

```go
func deferDemo() error {
    err := createResource1()
    if err != nil {
       return ERR_CREATE_RESOURCE1_FAILED
    }
    
    defer func() {
       if err != nil {
           destroyResource1()
       }
    }()
     
    err = createResource2()
    if err != nil {
       return ERR_CREATE_RESOURCE2_FAILED
    }
    
    defer func() {
       if err != nil {
           destroyResource2()
       }
    }()
     
    err = createResource3()
    if err != nil {
       return ERR_CREATE_RESOURCE3_FAILED
    }
    return nil
}
```

参考答案：F

80.【中级】 channel本身必然是同时支持读写的，所以不存在单向channel（）

参考答案：F

81.【初级】 import后面的最后一个元素是包名（）

参考答案：F