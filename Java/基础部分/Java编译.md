# 编译Java文件的过程

### 编写Java源程序
1.在某个目录下新建文本文件，将`.txt`修改成`.java`，完整的文件名字为`HelloWorld.java`
2.用文本编辑器打开
3.在文本文件中键入代码：
```java
public class HelloWorld{
    public static void main(Sting[] args){
        System out println("Hello World!");
    }
}
```

> 文件名必须和类的名字一致，注意大小写


### 编译Java源文件

在DOS命令行中，**进入Java源文件的目录**，使用`javac`命令进行编译

命令：
`javac HelloWorld.java`

编译成功后，会生成一个新的文件`HelloWorld.class`，改文件就是编译后的文件，是Java可运行文件，称为**字节码文件**，有了字节码文件，就可以运行程序了。

### 运行Java程序

在DOS命令行中，**进入Java源文件的目录**，使用`java`命令进行运行。

命令：
`java HelloWorld`

> java HelloWorld **不要写 不要写 不要写.class**

### 编译和运行是两回事

* **编译**：是指将我们编写的Java源文件翻译成JVM认识的class文件，在这个过程中，`javac`编译器会检查我们所写的程序是否有错误，有错误就会提示出来，如果没有错误就会编译成功。
* **运行**：是指将`class文件`交给JVM去运行，此时JVM就会去执行我们编写的程序了。