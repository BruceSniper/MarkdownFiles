## 第三部分：JavaScript

### 一. JavaScript简介

#### 1. JavaScript概述

JavaScript是基于对象和事件的脚本语言。

特点：

* 安全性（不允许直接访问硬盘），他可以做的是信息的动态交互。
* 跨平台性。（只要是可以解释执行JS的浏览器都可以执行，和平台无关）

#### 2. JavaScript和Java的不同之

* JS是Netscape公司的产品，Java是SUN（现在是Oracle）公司的产品。
* JS是基于对象，Java是面向对象。
* JS只需要解释执行，Java需要先编译成字节码文件，再执行。
* JS是弱类型，Java是强类型。

#### 3. JavaScript和HTML结合的方式

想要将其他代码融入html中，都需要以标签的形式

* 代码放在<script>...</script>标签中
* 使用script标签的src属性引入一个js文件，方便后期更新，及维护。例如：`<script  type="javascript"  src="test.js"></script>`

### 二. JavaScript语法

####  1. 变量

 通过关键字var来定义，弱类型即是不用指定具体类型。
 例如：var  x  =  12； x  =  "hello"；
注：JS中特殊的常量undefined，当变量没有初始化就被使用，该变量的值就是undefined（未定义）。

#### 2. 语句

* 判断结构（if语句）
注：在JS中0就是false，非0就是true（通常用1表示）

* 选择结构（switch语句）
注：没有具体类型限制

* 循环结构（while语句，do...while语句，for语句）

#### 3. 函数

* 一般函数

格式：

```javascript
function  函数名（形式参数...）

    {

        执行语句；

        renturn  返回值；

    }
```

函数是多条语句的封装体，只有被调用才会被执行。

注意：调用有参数的函数，但没有给其赋值，函数一样可以运行；或者调用没有参数的函数，给其传值，也一样运行。简单地说，只要写了函数后面的小括号，函数就可以运行。

其实，在函数中有一个参数数组对象（arguments），该对象将传递的参数都封装在一个数组中。例如：

```javascript
function  demo（）{

    alert（arguments.length）；

 }

demo（123，"hello"，true）；//调用函数，弹出对话框的结果为3。
```

通过for循环遍历该数组，如：

```javascript
for（var  x=0；x<arguments.length；x++）{

    alert（arguments[x]）；

}
```

函数在调用时的其他写法：

```javascript
var  show  =  demo（）//show变量接收demo（）函数的返回值
var  show  =  demo  //这种写法是可以的，意为show和demo是一个函数，那么该函数也通过show（）的方式运行
```

* 动态函数

通过JS的内置对象function实现，例如：

```javascript
var  demo  =  new  function（"x，y"；"alert（x+y）"；）；
demo（4,6）；
```

和一般函数不同的是，动态函数、参数及函数体都可以通过参数传递，动态指定。

* 匿名函数

格式：`function（）{...}`，例如：

```javascript
var  demo  =  function（）{...}

demo（）；
```

通常在定义事件属性的行为时，较为常用。

匿名函数就是一种简写格式。

#### 4. 数组

方便操作多元素的容器，可以对其中的元素编号。

特点：可以存任意元素，长度是可变的。

格式：

```javascript
var arr = new Array（）；

arr[0] = "hello"；

arr[1] = 123；

var arr = ["hello"，123，true，"abc"]；

for(var x=0；x<arr.length；x++){

    alert(arr[x])；
}
```

#### 5. 对象

JS除了已经提供的内置对象外，也可以自定义对象。

例如：

```javascript
function  Person(){}

var  p  =  new  Person()；

p.name  =  "zhangsan"

p.age  =  13；

p.function(){

    alert("run")；

}

或：

funtion  Person(){

    this.name  =  name；
    this.age  =  age；

}
var  p  =  new  Person("zhangsan"，13)；
```

**with语句**

 格式：

    with（对象）{}

应用：

    当调用一个对象中多个成员时，为了简化调用，避免"对象. "这种形式的重复书写，可以写成：

```javascript
var p = new Person(“zhangsan”,20);

with(p)

{

    alert(name+”,”+age);

}
```

with语句定义了某个对象的作用域，在该域中可以直接调用该对象的成员。

**for...in语句**

用于遍历对象属性。

例：

```javascript
var p = new Person(“zhangsan”,20);

for(x in p){

    alert(x);//结果是两个对话框，一个是name，一个是age。

    alert(x+”:”+p[x]);//可以得到属性与属性的值。p[x]:p对象就是个数组，要通 过指定的元素名获取元素的值。

}
```

### 三. window对象

#### 1. avigator对象

* appName属性：浏览器的名称
* AppVersion属性：浏览器的版本号

#### 2. location对象

* href属性：获取或者设置地址

#### 3. screen对象

* height与availHeight属性：获取屏幕的高度，是否去除任务栏
* width与availWidth属性：获取屏幕的宽度，是否去除任务栏

#### 4. event对象

* keyCode属性：获取键盘按键
* returnValue属性：获取或者设置某个属性的返回值
* srcElement属性：获取某个事件的源对象

#### 5. window方法

* confirm：弹出一个确认对话框，返回值的值为true或false
* focus：使某个元素获得焦点，并执行onfocus时间制定的代码
* moveBy与moveTo：移动
* open：打开窗口，可以制定标题、打开方式、窗口属性（标题栏、滚动条、可变大小等）
* prompt：显示一个提示框，有一条消息和一个输入框
* setTimeout与clearTimeout：间隔多长时间之后执行
* setInterval与clearInterval：每间隔多长时间执行