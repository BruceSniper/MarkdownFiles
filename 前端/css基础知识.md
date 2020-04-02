## 第二部分：CSS

### 一. Web标准简介

#### 1. 什么是web标准？

web标准不是某一个标准，而是由W3C和其他标准化组织指定的一系列的标准集合，包含我们熟悉的HTML、XHTML、JavaScript、CSS等。

#### 2. web标准的目的？

在于创建一个统一的用于web表现层的技术标准，以便于通过不同浏览器或终端设备向最终户展示信息内容。

#### 3、采用web标准的好处？

* 提高页面浏览速度：使用css方法，比传统的设计方法至少节约50%以上的文件尺寸。
* 缩短改版时间，将表现（样式/外观）与内容（信息/数据）相分离：只需要简单的修改几个css文件就可以重新设计一个有成千上万页面的站点。
* 降低网站流量的费用：带宽要求降低（代码更简洁），成本降低。
* 更容易被搜索引擎搜索到：提高网站在百度或谷歌上的排名。
* 内容能被更广泛的设备访问：包括屏幕阅读、手持设备、搜索机器人、打印机、电冰箱等等。

#### 4. web标准的构成？

**web标准由三部分组成：**

* 结构（structure）
* 表现（presentation）
* 行为（behavior）

#### 5. 理解表现和结构的分离

基本的概念：内容、结构、表现和行为

* 内容：就是制作者放到页面内真正想让访问者浏览的信息。
* 结构：使内容更加具有逻辑性和易用性（类似于一级二级标题、正文、列表等称为结构）
* 表现：用于修饰内容外观的样式
* 行为：对内容的交互及操作效果，如通过JavaScript判断表单提交等

![](https://img-blog.csdn.net/20150729132038220)

### 二. CSS简介

#### （一）概念

1. CSS是Cascading  Style  Sheets（层叠样式表）的简称。

2. 更多的人把它称作样式表，顾名思义，它是一种设计网页样式的工具。借助CSS的强大功能，网页将在你丰富的想象力下千变万化。实际上CSS代码都是由一些最基本的语句组成的。

3. CSS可以作为HTML、XHTML、XML的样式控制语言。

#### （二）CSS语法结构

##### 1. 选择符{  属性：值 }

例如：`body{ font-size : 12px; }`

参数说明：

* 选择符（Selector）：指明这组样式所要针对的对象。可以是一个XHTML标签，如body、h1等；也可以是定义了特定的ID或class的标签，如`#main`选择符表示选择`<div  id="main">`，即一个被指定了main为id的对象。
* 属性（Property）：选择符的样式属性，如颜色、大小、定位、浮动方式等。
* 值（Value）：指属性的值。

>注：同时可以为一个选择符定义多个属性，每个属性之间用分号分隔。

##### 2. CSS长度单位

![](https://img-blog.csdn.net/20150729134626231)

##### 3. CSS颜色单位

![](https://img-blog.csdn.net/20150729134552202)

##### 4. CSS控制字体

![](https://img-blog.csdn.net/20150729134752296)

#### （三）CSS在网页中的应用方式

1. 内联式样式表：直接写在现有的标记中，如：

`<p  style="color:red">...</p>`

2. 嵌入式样式表：使用`<style></style>`标签嵌入到HTML文件的头部`<head>`标记内，如：

`<style  type="text/css">...</style>`

3. 外部链接式：将样式表写在一个独立的css文件中，然后再页面head区`<head>`标记内用`<link>`标签调用它，如：

`<link  href="main.css"  rel="stylesheet"  type="text/css">`

4. 导入式样式表：导入式样式表和链接式样式表的功能基本相同，只是语法和动作方式略有不同，同样也将导入式样代码写在`<head>`标记内，如：

```html
<style  type="text/css">

    @import  url(basic.css);

</style>
```

#### （四）CSS选择符类型

1. 类型选择符：就是HTML文档中的元素，如：

`p{属性：值}`

2. 类选择符：可以自定义样式，应用于一个或多个网页元素，类在网页中可以出现多次用于定义重复的样式，类以.开头，后面的名称自己定义，类定以后还需要在网页中加入class=类名称，加以调用。如：

```html
.warning{属性：值}

<p class="warning">...</p>
```

3. ID选择符：与类基本相似，只是以英文#开头，因为ID具有唯一性，所以在网页中只能出现一次，用于定义只出现一次的样式。如：

```html
#main{属性：值}

<p ID="main">...</p>
```

#### （五）CSS样式的特点

1. 继承：

网页中子元素将继承父元素的样子，例如：要控制段落p中的文字大小，可以直接给body标记家样式。

2. 层叠（覆盖）：

* 网页中子元素定义了与父元素相同的样式，则子元素的样式将覆盖掉父元素中的样式
* 定义后面的样式会覆盖前面的样式

#### （六）CSS样式的优先权

1. 四种方式的优先权：内联式【行内样式】-->嵌入式【内部式】-->连接式【外部式】-->@import【导入式】

2. CSS优先权：就近原则

总结：范围越小，优先权越高；

离要修饰目标越近的样式，优先权越高。

3. 选择符的优先权：ID>class>类选择符

#### （七）CSS控制文本

![](https://img-blog.csdn.net/20150804200457931)

#### （八）CSS控制链接

![](https://img-blog.csdn.net/20150804200628154)

### 三. CSS高级

#### （一）CSS选择符的详细使用

1. 类型选择符：

* 就是html文档中的元素`[作用于html标记]`。如：`p{属性：值}`

2. 类选择符：

* 可以自己定义样式，应用于一个或多个网页元素，类在网页中可以出现多次，用于定义重复的样式。类以英文.开头，后面的名字自己定义，类定以后还需要在网页中加入"class=类名称"，加以调用。如：  `.waring{属性：值}  <p  class="waring">...</p>`

3. ID选择符：

* 与类基本相似，只是以英文#开头，因为ID具有唯一性，所以在网页中只能出现一次，用于定义只出现一次的样式。如：  `#main{属性：值}   <p  ID=main></p>`

4. 通配选择符：

* 用于定义所有元素。如：*{属性：值}

5. 包含选择符：

* 所有被e1包含的e2。如：table  td{属性：值}
* 同时给某个元素应用多个类和ID。如：<p  class="a1  a2"   id="a6">...</p>

6. 选择符分组：

* 将同样的样式定义用于多个选择符，选择符之间用逗号隔开。如：body，div，p{属性：值}

7. 标签指定式选择符：

如果既想使用id或class，也想使用标签选择符，那么，

* `h1#content{}`：表示针对所有id为content的h1标签；
* `h1.content{}`：表示针对所有class为content的h1标签；

8. 组合选择符：

将以上选择符组合使用，那么，

* `h1  .content{}`：表示在h1下所有class为content的标签；
* `h1  .content，#content  h1{}`

#### （二）CSS常用属性

##### 1. CSS控制边框属性：

|功能|语法|
|-|-|
|设置边框粗细|border-top-width：12px|
|设置边框样式	|border-bottom-style：slide（实线）、dashed（虚线）|
|设置边框颜色	|border-right-color：#000000|
|设置某一边框的属性|	border-边框位置：线宽  线型  颜色|
|设置四条边的属性	|border：线宽  线型  颜色|

##### 2. CSS控制背景：

|功能|	语法|
|-|-|
|背景|	background：颜色  图片 平铺方式  固定方式  位置|
|背景颜色|	background-color：#ccc|
|背景图片|	background-image：url|
|背景图片的重复方式|	background-repeat：【repeat，no-repeat，repeat-x，repeat-y】|
|背景图片的依附方式	|background-attachment：【scroll，fixed】|
|背景图片的位置	|background-position：top【left、center、right】  center【left、center、right】  bottom【left、center、right】，x坐标y坐标（左上角是0，0，单位是像素px）|

##### 3. CSS控制列表：

|功能	|语法|
|-|-|
|列表属性|	list-style：list-stylet-ype  list-style-position  list-style-image|
|列表项目类型	|list-style-type：none，disc，circle，square，decimal，lower-roman，upper-roman，lower-alpha，upper-alpha|
|列表项目位置	|list-style-position：inside，outside|
|列表项目图片|	list-style-image：url，none|

##### 4. CSS控制元素的尺寸：

|功能|	语法|
|-|-|
|设置元素的宽度|	width：100px|
|设置元素的高度	|height：100px|
|设置元素最小宽和高	|min-width：50px，min-height：50px|
|设置元素最大宽和高|	max-width：50px，max-height：50px|
|设置元素的外边距	|margin：上  右  下  左|
|设置元素的内边距	|padding：上  右  下  左|

### 四. CSS+DIV布局

#### （一）网页元素分类

##### 1. div是什么？

div是一个容器，能放置内容，例如：`<div>内容</div>`。

说明：XHTML中每一个标签对象几乎都可以成为一个容器，例如：<h1>标题</h1>。

div是xhtml中指定的，专门用于布局设计的容器对象。CSS布局中，div是这种布局的核心对象，做一个简单的布局只需要两样东西div与css，因此也有人称CSS布局为div+css布局。

#### （二）盒子模型

##### 1. 盒子模型：W3C组织建议把所有网页中的对象都放到一个盒子中。

* 设计师可以通过创建定义来控制这个盒子的属性，这些对象包括段落、列表、标题、图片及层`<div>`。
##### 2、盒子模型主要定义这四个区域：内容（content）、填充（padding）、边框（border）、边界（margin）。

##### 3、整个盒子模型在页面中所占的宽度：左边界+左边框+左填充+内容+右填充+右边框+右边界。

示意图如下：

![](https://img-blog.csdn.net/20150811133133571)

3D示意图如下：

![](https://img-blog.csdn.net/20150811133302534)

#### （三）CSS布局

##### 1. 元素的分类：不同的元素在文档类型定义DTD（Document  Type  Difinition）内有默认的分类，可以通过css修改分类的定义。

1. 块级元素：`{display：block}`

* 每个块级元素都从一个新行开始，而且其后的元素也需要另起一行开始，如：div[层]、标题、段落、表格、body等；
* 块级元素只能作为其他块级元素的子元素，而且需要一定的条件；

2. 内联元素：`{display：inline}`

* 内联元素不需要在新行显示，而且也不强迫后面的元素换行，如：a、em、span等；
* 内敛元素可以作为任何元素的子元素；

3. 隐藏元素：`{display：none}`

* 当某个元素被设置为display：none时，浏览器会完全忽略这个元素，此元素将不会被显示；

##### 2. 浮动与清除浮动

1. 浮动（float）

浮动（float）是CSS实现布局的一种方式，包括div在内的任何元素都可以浮动的方式展示。

值：

* none：不浮动
* left：对象向左浮动，而右侧的内容流向对象的右侧
* right：对象向右浮动，而左侧的对象内容流向对象的左侧

2. 浮动的清理（clear）

清理时浮动的又一个有用的工具，实现拒绝浮动对象对后面对象的影响。

技巧：

* 当浮动了许多元素之后，突然需要另起一行时，可以制作一个空白的div标签，为其设置clear：both清楚左右的浮动

3. 溢出（overflow）

设置当前对象的内容超出其指定高度和宽度时，如何管理内容。

* visible：默认值，不剪切内容，也不添加滚动条；
* auto：在必须时，对象内容才会被剪切，或显示滚动条；
* hidden：不显示超过尺寸的内容；
* scroll：总是显示滚动条；

4. 定位（position）

设置对象的定位方式。

* static：静态定位，页面中没一个对象的默认值；
* absolute：绝对定位，将对象从文档流中分离出来，通过设置left、right、top、bottom四个方向，相对于父级元素进行绝对定位；
* relative：相对定位，对象不从文档流中分离出来，通过设置left、right、top、bottom四个方向，相对于自身位置进行相对定位；

##### 3. CSS布局方式

* 默认文档流方式：以默认的html元素的结构顺序显示；
* 浮动布局方式：通过html元素的float属性显示；
* 定位布局方式：通过设置html元素的position属性显示；

```html
#box{

          width:300px;

          height:300px;

          position:relative;

}

#first{

          width:300px;

          height:300px;

          position:absolute;
          top:10px;

          right:20px;

}

#second{

          width:300px;

          height:300px;

          position:absolute;
          top:100px;

          left:200px;

}
<div  id="box">

          <div  id="first">...</div>

          <div  id="second">...</div>

</div>
```

##### 4. 清除浮动的方式

1. 额外标签法：w3c推荐，在浮动元素的最后添加一个空标签

```html
.clear{

          clear:both;

}

<div  id="box">

          <div  id="first">...</div>

          <div  id="second">...</div>

          <div  class="clear">...</div>

</div>
```

2. overflow方法：

```html
#box{

          width:300px;

          height:300px;

          overflow:hidden;

}

<div  id="box">

          <div  id="first">...</div>

          <div  id="second">...</div>

</div>
```

3. 利用伪对象after方法（网上最流行的清除浮动代码）

```html
.clearFix：after{

          clear:both;

          display:block;

          visibility:hidden;

          height:0;

          line-height:0;

          content:"";

}

.clearFix{zoom:1}
```