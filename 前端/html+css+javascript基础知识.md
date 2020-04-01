# HTML+CSS+JavaScript基础知识

## 第一部分：HTML

### 一. 简介HTML

1. HTML（Hyper Text Mark-up Language超文本标记语言）的缩写（标记：就是用来描述网页内容的一些特定符号）。HTML不是编程语言，而是一种描述性的标记语言，用于描述网页内容的显示方式，比如文字的颜色、大小，这些都是利用html标记来实现的。
2. HTML文档的创建方式：

* 手工直接编写（例如记事本）
* 通过图形化的HTML开发软件Dreamweaver
* 由web服务器上的动态网页程序生成

### 二. HTML的语法

HTML最基本的语法就是`<标记符>内容</标记符>`，标记符通常都是承兑使用的，有一个开始标记和一个结束标记。结束标记只是在开始标记的前面加上一个斜杠/当浏览器打开html文件后，就会理解里面的标记符，然后把标记符对应的功能表达出来。

HTML标记的类型：单标记与双标记

#### 1. 单标记

* <标记名称>：单一型，无属性值。如 `<br/>`
* <标记名称 属性="属性值">：单一型，有属性值。如 `<hr  width="80%" />`

#### 2. 双标记

* `<标记名称>...</标记名称>`：没有属性值。如`<title>...</title>`
* `<标记名称  属性="属性值">...</标记名称>`：有属性值。如`<body  bgcolor="red">...</body>`

#### 3. 总结

* 标记与属性、属性之间以空格分隔
* 属性不区分先后顺序，且属性不是必须的
* 虽然在HTML中标记不区分大小写，但在XHTML中所有的标记都必须小写，所以建议所有标记都采用小写

### 三. HTML文档结构

所有的网页文件，通常由四对标记来构成文档的骨架，它们是：
```html
        <html>：标识网页文件的开始和结束，所有的html元素都要放在这对标记中

                      <head>：标识网页文件的头部信息，如标题、搜索关键字等

                                      <title>标题</title>：标识文件的标题

                      </head>

                      <body>：标识文件的主体部分

                                    正文

                       </body>

         </html>
```

#### （一）meta标记用于定义文件信息

meta标记用于定义文件信息，对网页文件进行说明，放置于`<head></head>`之间

* 设置关键字：`<meta name="keywords" content="value"/>`，多个关键字内容之间可以用逗号分隔。
* 设置描述：`<meta name="description" content="value"/>`
* 设置作者：`<meta name="author" content="value"/>`
* 设置字符集：`<meta http-equiv="content-type" content="text/html;charset=gb2312"/>`
* 设置页面定时跳转：`<meta http-equiv="Refresh" content="2;http://www.itcast.com"/>`

#### （二）网页主体标记body

1. 注释：<!--注释内容-->

2. body属性：

```html
<body  bgcolor="背景颜色" background="背景图片" text="文本颜色" link="链接文本颜色" vlink="访问过的链接文本颜色" alink="激活的链接文本颜色" leftmargin="zuobianjie" rightmargin="右边界" topmargin="上边界"  bottommargin="下边界">
```

#### （三）字体修饰

1. `<font>`标记：

`<font  color="文本颜色"  size="字号"  face=""></font>`

![](https://img-blog.csdn.net/20150723203439011)

2. 字符格式:

![](https://img-blog.csdn.net/20150723203613045)

3. 段落控制标记

`<p  align="对齐方式"></p>`

属性名称：align，属性值：left（默认）、center、right

4. 段落标题

`<hx  align="对齐方式"></hx>`

x取值 [1-6] ：hx内的文本对自动加粗显示。

>注：hx针对的对象时段落，font针对的对象时任意文本

5. 换行：`<br/>`换行不换段

6. 水平直线：`<hr/>`

![](https://img-blog.csdn.net/20150723204508453)

#### （四）特殊标记

1. 定义一个块引用：使用文本缩进

格式：`<blockquote>...</blockquote>`

属性名称：cite，属性值：url，说明：被引用的地址

2. 居中标记`<center>内容</center>（被废弃的标签）`

3. 预格式化：`<pre></pre>`

4. 显示已经格式化好的文字，不加此标记的话，HTML浏览器会忽略所有空格和制表符

![](https://img-blog.csdn.net/20150724192955958)

#### （五）列表标记

1. 列表标记的用途：列表标记可以创建一般的无需列表、编号列表，以及定义列表的三种方式。还可以在一种列表中嵌套另一种列表。便于概括显示一系列相关的内容。

* 无序列表：`<ul>...</ul>`
* 有序列表：`<ol>...</ol>`
* 定义列表：`<dl>...<dl>`

2. 无序列表
* 语法：`<ul  type="项目符号类型">    <li  type="项目符号类型">内容1</li>    <li>内容2</li>  </ul>`

![](https://img-blog.csdn.net/20150724194048955)

3. 有序列表

* 语法：`<ol  start="列表起点"  type="项目符号类型">   <li>内容1</li>  <li>内容2</li> </ol>`

![](https://img-blog.csdn.net/20150724194851495)

4. 定义列表

* 语法：

```html
          <dl>----------定义列表
          <dt>标题1</dt>-----------表示一个项目
                    <dd>内容1</dd>------------表示一个项目下的更详细的内容解释
          <dt>标题2</dt>
                    <dd>内容2</dd>
          <dt>标题3</dt>
                    <dd>内容3</dd>
          </dl>
```

#### （六）图片

1. web上支持的图片格式

* GIF（图形交换格式）：GIF格式文件最多只能保存256种颜色。该格式支持透明色，支持动画效果。
* JPEG（联合图像专家组）：改格式不支持透明色及动画，颜色可达1670万种。
* PNG（网格可移植格式）：该格式支持透明色，但不支持动画，颜色从几十种至1670万种。

2. 图片标记：·<img  src="图片的路径"/>·

3. 路径：
* 绝对路径：提供目标文档的完整主机名称、路径信息、及文档全称
* 相对路径：从当前文档开始的路径
* 根相对路径：从站点根目录开始的路径，以/开头

相对路径时，如果当前文档和目标文档位置平行，则直接书写文档全称；如果当前文档和目标文档所在文件夹位置平行，则书写为文件夹名称/目标文档全称；如果当前文档所在位置和目标文档位置平行，则书写为../目标文档全称。

![](https://img-blog.csdn.net/20150724200525954)

### 四. 表格

#### （一）表格结构和属性

1. 因为表格中可以包含任何内容，所以在使用DIV+CSS之前，网页设计师是使用表格对网页内容进行排版与布局的

2. 表格基本结构：

* `<table>...</table>`--------定义表格
* `<tr>...</tr>`----------定义行
* `<td>...</td>`-----------定义列（单元格）
* `<th>...</th>`-----------定义标题栏（文字加粗）

3. 表格的属性`<table>`

![](https://img-blog.csdn.net/20150725130549541)

4. `<table>`标签下的边框设置

![](https://img-blog.csdn.net/20150724201526009)

5. 行的属性`<tr>`

![](https://img-blog.csdn.net/20150725130711858)

6. 列的属性`<td>`

![](https://img-blog.csdn.net/20150725130905228)

#### （二）表格的结构化

##### 1. 结构化格式：

* `<table>`
* `<thead>...</thead>`---------表头区
* `<thead>...</thead>`---------表体区
* `..........`
* `<tfoot>...</tfoot>`----------表尾区
* `</table>`

##### 2. 直列化格式：`<colgroup>...</colgroup>`

![](https://img-blog.csdn.net/20150725131704757)

##### 3. 表格的标题：`<table>   <caption>...</caption>   </table>`

![](https://img-blog.csdn.net/20150725131751600)

### 五. 超链接

一个网站由多个网页组成的，网页之间通过连接实现相互关联。

#### （一）连接的概念

实现当前文档到目标文档的一种跳转。

#### （二）链接语法

` <a  href=连接的目标   title="注释"   target="打开链接窗口的形式">...</a>`

* `_blank`：在新窗口中打开
* `_self`：在自身窗口中打开（默认）
* `_parent`：在上一级窗口中打开
* `_top`：在本窗口中打开

#### （三）链接的类型

##### 1. 内部链接：当前文档和目标文档在同一个站点

`<a  href=目标文档位置及全称>`

##### 2. 外部链接：当前文档和目标文档不在同一个站点

`<a  href=URL>`

##### 3. E-mail链接：允许访问者向指定的地址发邮件

`<a  href=mailto:电子邮件地址>`

##### 4. 局部链接（锚点）：跳转到同一网页或其他文档中的指定位置，

* 创建锚点：`<a  name="锚点名称">...</a>`
* 链接锚点：`<a  href="#锚点名称">...</a>`

##### 5. 空链接：就是没有目标端点的链接

`<a href="#"></a>`

例如：

A. 设为首页：
`<a href="#" onClick="this.style.behavior='url(#default#homepage)';this.sethomepage('http://www.sohu.com')">设为首页</a>`


B. 添加收藏：
`<a href="#" onClick="javascript:window.external.addfavorite('http://www.sohu.com','搜狐')">加入收藏夹</a>`


##### 6. 脚本链接：是一种特殊的链接，当单机设置脚本链接的文本或图像时，可以运行相应的JavaScript语句。

例如：

`<a href=javascript:window.open(“http://www.163.com”)>新浪</a>`

* 关闭窗口：输入javascript:window.close()
* 打开窗口：输入javascript:window.open ('文件名')

### 六. 表单

#### （一）表单的功能

1. 表单的作用是从访问您web站点的用户那里获取信息，访问者可以使用诸如文本框、列表框、单选框及复选框之类的表单元素输入信息，然后单击某个按钮提交这些信息。

2. 客户端和服务器端进行交流的途径。

#### （二）表单标记

##### 1. form标记用于创建一个表单，定义表单的开始和结束，它是一个容器，用于包含其他表单元素，例如文本框、单选框等。表单元素必须写在form标记内才有用。

##### 2. 格式：

`<form  action=URL（处理表单信息的服务器端应用程序） method=处理表单数据的方法（POST/GET）如果不写默认为GET   name=表单名称>...</form>`

##### 3. 表单元素标记：

###### A. 单行文本框：

`<input  name="文本框名称"  type="text"  value="初始值"  size="显示字符数"  maxlength="最多容纳字符数"  readonly="readonly"（设置为只读）  disabled="disabled"（设置为不可操作） />`

###### B. 密码框：

`<input  name="密码框名称"  type="password"  value="初始值"  size="显示字符数" />`

###### C. 多行文本框：

`<textarea  name="文本框名称"  cols="每行的字符数"  rows="显示的行数"></textarea>`

###### D. 单选框：

`<input  name="单选框名称"  type="radio"  value="提交值"  checked="checked"（是否被选中）/>`

###### E. 复选框：

`<input  name="复选框名称" type="checkbox"  value="提交值"  checked="checked" />`

###### F. 标注：

`<label  for="man">男</label>  <input  type="radio"  name="sex"  value="男"  id="man">`

###### G. 列表框：

* 菜单式：

```html
<select  name="列表框名称">

    <option  selected="selected"（哪个为初始值就添加selected语句）  value="提交值">列表1</option>

    <option  value="提交值">列表2</option>

                    ......

</select>

分组：<optgtoup  label="分组名称"></optgroup>
```

* 列表式

```html
<select  name="列表框名称"  size="显示的行数"  multiple（如果允许多选则有该命令，否则没有此命令）>
                    <option  value="提交值"></option>
                    ......
</select>
```

###### H. 按钮：

`<input  type="按钮类型（reset重置表单、submit提交表单、button普通按钮）"  name="按钮名称"  value="按钮显示文本" />`

###### I. 图片按钮：

`<input  name="按钮名称"  type="image"  src="图片路径" />`

###### J. 隐藏域：

`<input  name="名称"  type="hidden"  value="提交值" />`

###### K. 浏览框：

`<input  name="名称"  type="file"  size="显示长度" />`

###### L. 表单外框：

`<fieldset >...</fieldset>`--------定义围绕表单中元素的边框
`<legend>...</legend>`---------legend为fieldset定义标题

### 七. 插入多媒体元素标记

#### 1. Flash动画的插入

![](https://img-blog.csdn.net/20150725201337635)

#### 2. 插入MP3音乐

![](https://img-blog.csdn.net/20150725201617582)

#### 3. 插入背景音乐

`<bgsound  src="音乐文件名及路径"  loop="循环次数" />（如果loop=-1即为无限循环）`

#### 4. 插入视频wmv格式

`<embed  src="tmcq.wmv"></embed>`

#### 5. 网络流媒体文件的插入

```html
<embed src="http://player.youku.com/player.php/sid/XMzA1MDE5MDMy/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash">
</embed>
```

#### 6. 动字幕

`<marquee>滚动的文字</marquee>`

* direction="滚动方向"（left、right、up、down）
* behavior="滚动方式"（scroll、slide、alternet）
* loop="循环次数"（若未指定则循环不止，loop=infinite）
* bgcolor=""  
* onMouseOver="this.stop()"     onMouseOut="this.start()"
* scrollamount=""
* scrolldelay=""

### 八. 框架--实现网页之中嵌套网页

#### 1. 框架的功能：

将浏览器划分为不同的区域，每个区域可以包含不同的网页。以实现多个网页在一个浏览器窗口中显示的效果。

#### 2. 框架的格式：

写框架时，不需要写body语句。

```html
<frameset  rows="行数及行高"  cols="列数及列宽"  framespcing="框架间距"  frameborder="是否显示边框（yes,no/0,1）"  border="边框宽度"  bordercolor="边框颜色">

<frame  src="文件地址及名称"  name="框架名称"  noresize="是否允许改变尺寸（true/false）"  scrolling="滚动条显示（yes/no/auto）">

</frame>

</frameset>
```

#### 3. 内嵌式框架

```html
<iframe  src="被嵌套的网页地址及名称"  width="宽度"  height="高度"  frameborder="是否显示边框（0,1）"  scrolling="滚动条显示（yes/no/auto）">

</iframe>
```

### 九. 从html迈向xhtml

![](https://img-blog.csdn.net/20150727133452741)

#### 1、什么是XHTML？

XHTML是The Extensible  Hyper  Text  Markup  Language的缩写，xhtml的意思是可扩展标识语言。

XHTML是HTML向XML过度的一个桥梁，Xhtml是基于html的，这是更严密、代码更简洁的HTML版本。

#### 2. DOCTYPE

DOCTYPE是document  type（文档类型）的简写，主要用来说明你用的XHTML或HTML是什么版本。浏览器根据DOCTYPE定义的DTD来解释页面代码，并展现出来。所以，建立符合标准的网页，DOCTYPE声明是必不可少的关键组成部分。

#### 3. XHTML1.0提供了三种DTD声明：

* 过度的（Transitional）：要求非常宽松的DTD，它允许你继续使用HTML4.0.1的标记（但是要符合xhtml的语法），完整代码如下：

```html
<!DOCTYPE  html  PUBLIC  "-//W3C//DTD  XHTML1.0 Transitional//EN"  "http://www.w3c.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

* 严格的（Strict）：要求严格的DTD，你不能使用任何表现层的标记和属性，例如`<br>`，完整代码如下：

```html
<!DOCTYPE  html  PUBLIC  "-//W3C//DTD  XHTML1.0 Strict//EN"  "http://www.w3c.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

* 框架的（Frameset）：专门针对框架页面设计使用的DTD，如果你的页面中包含有框架，需要采用这种DTD。完整代码如下：

```html
<!DOCTYPE  html  PUBLIC  "-//W3C//DTD  XHTML1.0 Frameset//EN"  "http://www.w3c.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```

#### 4. XHTML与HTML的区别：

* XHTML标签必须被正确的嵌套；
* XHTML标签必须被关闭；
* 标签名必须用小写字母；
* 属性名必须用小写，必有值，值必加引号；

