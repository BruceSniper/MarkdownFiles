# Golang精编100题2：填空题

1.【初级】声明一个整型变量i__________

参考答案：var i int

2.【初级】声明一个含有10个元素的整型数组a__________

参考答案：var a [10]int

3.【初级】声明一个整型数组切片s__________

参考答案：var s []int

4.【初级】声明一个整型指针变量p__________

参考答案：var p *int

5.【初级】声明一个key为字符串型value为整型的map变量m__________

参考答案：var m map[string]int

6.【初级】声明一个入参和返回值均为整型的函数变量f__________

参考答案：var f func(a int) int

7.【初级】声明一个只用于读取int数据的单向channel变量ch__________

参考答案：var ch <-chan int

8.【初级】假设源文件的命名为slice.go，则测试文件的命名为__________

参考答案：slice_test.go

9.【初级】 go test要求测试函数的前缀必须命名为__________

参考答案：Test

10.【中级】下面的程序的运行结果是__________

```go
for i := 0; i < 5; i++ {
    defer fmt.Printf("%d ", i)
}
```

参考答案：4 3 2 1 0

13.【中级】下面的程序的运行结果是__________

```go
func main() {
    x := 1
    {
       x := 2
       fmt.Print(x)
    }
    fmt.Println(x)
}
```

参考答案：21

21.【中级】下面的程序的运行结果是__________

```go
func main() {
    strs := []string{"one","two", "three"} 
    for _, s := range strs {
       go func() {
           time.Sleep(1 * time.Second)
           fmt.Printf("%s ", s)
       }()
    }
    time.Sleep(3 * time.Second)
}
```
参考答案：three three three

32.【中级】下面的程序的运行结果是__________

```go
func main() {  
    x := []string{"a", "b", "c"}
    for v := range x {
       fmt.Print(v)
    }
}
```

参考答案：012

38.【中级】下面的程序的运行结果是__________

```go
func main() {  
    x := []string{"a", "b","c"}
    for _, v := range x {
       fmt.Print(v)
    }
}
```

参考答案：abc

44.【初级】下面的程序的运行结果是__________

```go
func main() {  
    i := 1
    j := 2
    i, j = j, i
    fmt.Printf("%d%d\n", i, j)
}
```

参考答案：21

50.【初级】下面的程序的运行结果是__________

```go
func incr(p *int) int {
    *p++  
    return *p
}

func main() {  
    v := 1
    incr(&v)
    fmt.Println(v)
}
```
参考答案：2

59.【初级】启动一个goroutine的关键字是__________

参考答案：go

60.【中级】下面的程序的运行结果是__________

```go
type Slice []int

func NewSlice() Slice {
    return make(Slice, 0)
}

func (s* Slice) Add(elem int) *Slice {
    *s = append(*s, elem)
    fmt.Print(elem)
    return s
}

func main() {  
    s := NewSlice()
    defer s.Add(1).Add(2)
    s.Add(3)
}
```

参考答案：132