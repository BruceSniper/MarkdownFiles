# 创建 Django 博客的数据库模型

### 编写博客模型代码
以上是自然语言描述的表格，数据库也和编程语言一样，有它自己的一套规定的语法来生成上述的表结构，这样我们才能把数据存进去。一般来说这时候我们应该先去学习数据库创建表格的语法，再回来写我们的 django 博客代码了。但是 django 告诉我们不用这么麻烦，它已经帮我们做了一些事情。django 把那一套数据库的语法转换成了 Python 的语法形式，我们只要写 Python 代码就可以了，django 会把 Python 代码翻译成对应的数据库操作语言。用更加专业一点的说法，就是 django 为我们提供了一套 ORM（Object Relational Mapping）系统。

例如我们的分类数据库表，django 只要求我们这样写：

```python
blog/models.py
 
from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=100)
```

`Category` 就是一个标准的 Python 类，它继承了 `models.Model` 类，类名为 `Category` 。`Category` 类有一个属性 `name`，它是 `models.CharField` 的一个实例。

这样，django 就可以把这个类翻译成数据库的操作语言，在数据库里创建一个名为 category 的表格，这个表格的一个列名为 name。还有一个列 id，虽然没有显示定义，但 django 会为我们自动创建。可以看出从 Python 代码翻译成数据库语言时其规则就是一个 Python 类对应一个数据库表格，类名即表名，类的属性对应着表格的列，属性名即列名。

我们需要 3 个表格：文章（Post）、分类（Category）以及标签（Tag），下面就来分别编写它们对应的 Python 类。模型的代码通常写在相关应用的 models.py 文件里。已经在代码中做了详细的注释，说明每一句代码的含义。但如果你在移动端下阅读不便的话，也可以跳到代码后面看正文的里的讲解。

```python
blog/models.py
 
from django.db import models
from django.contrib.auth.models import User
 
 
class Category(models.Model):
    """
    django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)
 
 
class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)
 
 
class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
 
    # 文章标题
    title = models.CharField(max_length=70)
 
    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()
 
    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
 
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
 
    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一
    # 对多的关联关系。且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    # 数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此     # 使用 models.CASCADE 参数，意为级联删除。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 
    # ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
 
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 
    # django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 
    # Category 类似。
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

### 博客模型代码代码详解

首先是 `Category` 和 `Tag` 类，它们均继承自 `models.Model` 类，这是 django 规定的。`Category` 和 `Tag` 类均有一个`name` 属性，用来存储它们的名称。由于分类名和标签名一般都是用字符串表示，因此我们使用了 `CharField` 来指定 `name` 的数据类型，同时 `max_length` 参数则指定 `name` 允许的最大长度，超过该长度的字符串将不允许存入数据库。除了 `CharField` ，django 还为我们提供了更多内置的数据类型，比如时间类型 `DateTimeField`、整数类型 `IntegerField` 等等。

>提示：
>
>在本教程中我们会教你这些类型的使用方法，但以后你开发自己的项目时，你就需要通过阅读 django 官方文档 关于字段类型的介绍 来了解有哪些数据类型可以使用以及如何使用它们。

`Post` 类也一样，必须继承自 `models.Model` 类。文章的数据库表稍微复杂一点，主要是列更多，我们指定了这些列：

* `title`。这是文章的标题，数据类型是 `CharField`，允许的最大长度 `max_length = 70`。

* `body`。文章正文，我们使用了 `TextField`。比较短的字符串存储可以使用 `CharField`，但对于文章的正文来说可能会是一大段文本，因此使用 `TextField` 来存储大段文本。

* `created_time`、`modified_time`。这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的列用 `DateTimeField` 数据类型。

* `excerpt`。文章摘要，可以没有文章摘要，但默认情况下 `CharField` 要求我们必须存入数据，否则就会报错。指定 `CharField` 的 `blank=True` 参数值后就可以允许空值了。

* `category` 和 `tags`。这是分类与标签，分类与标签的模型我们已经定义在上面。我们把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 `ForeignKey`，即一对多的关联关系。且自 django 2.0 以后，`ForeignKey` 必须传入一个 `on_delete` 参数用来指定当关联的数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此使用 `models.CASCADE` 参数，意为级联删除。

而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 `ManyToManyField`，表明这是多对多的关联关系。同时我们规定文章可以没有标签，因此为标签 `tags` 指定了 `blank=True`。

* `author`。文章作者，这里 `User` 是从 `django.contrib.auth.models` 导入的。`django.contrib.auth` 是 django 内置的应用，专门用于处理网站用户的注册、登录等流程。其中 `User` 是 django 为我们已经写好的用户模型，和我们自己编写的 `Category` 等类是一样的。这里我们通过 `ForeignKey` 把文章和 `User`关联了起来，因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 `Category` 类似。

### 理解多对一和多对多两种关联关系
我们分别使用了两种关联数据库表的形式：`ForeignKey`和 `ManyToManyField`。

##### ForeignKey

`ForeignKey` 表明一种一对多的关联关系。比如这里我们的文章和分类的关系，一篇文章只能对应一个分类，而一个分类下可以有多篇文章。反应到数据库表格中，它们的实际存储情况是这样的：

| 文章 ID | 标题 | 正文 | 分类 ID |
|---|---|---|---|
| 1 | title 1 |body 1 | 1 |
| 2 | title 2 |body 2 | 1 |
| 3 | title 3 |body 3 | 1 |
| 4 | title 4 |body 4 | 2 |

| 分类 ID |	分类名 |
|---|---|
| 1 | Django |	
| 2 | Python |

可以看到文章和分类实际上是通过文章数据库表中**分类 ID**这一列关联的。当要查询文章属于哪一个分类时，只需要查看其对应的分类 ID 是多少，然后根据这个分类 ID 就可以从分类数据库表中找到该分类的数据。例如这里文章 1、2、3 对应的分类 ID 均为 1，而分类 ID 为 1 的分类名为 django，所以文章 1、2、3 属于分类 django。同理文章 4 属于分类 Python。

反之，要查询某个分类下有哪些文章，只需要查看对应该分类 ID 的文章有哪些即可。例如这里 django 的分类 ID 为 1，而对应分类 ID 为 1 的文章有文章 1、2、3，所以分类 django 下有 3 篇文章。

希望这个例子能帮助你加深对多对一关系，以及它们在数据库中是如何被关联的理解，更多的例子请看文末给出的 django 官方参考资料。

##### ManyToManyField

`ManyToManyField` 表明一种多对多的关联关系，比如这里的文章和标签，一篇文章可以有多个标签，而一个标签下也可以有多篇文章。反应到数据库表格中，它们的实际存储情况是这样的：

| 文章 ID | 标题 | 正文 |
|---|---|---|
| 1 | title 1 |body 1 |
| 2 | title 2 |body 2 |
| 3 | title 3 |body 3 |
| 4 | title 4 |body 4 |

| 分类 ID |	分类名 |
|---|---|
| 1 | Django学习 |	
| 2 | Python学习 |

| 文章 ID |	标签 ID |
|---|---|
| 1 | 1 |	
| 1 | 2 |
| 2 | 1 |
| 3 | 2 |

多对多的关系无法再像一对多的关系中的例子一样在文章数据库表加一列 **分类 ID** 来关联了，因此需要额外建一张表来记录文章和标签之间的关联。例如**文章 ID** 为 1 的文章，既对应着 **标签 ID** 为 1 的标签，也对应着 **标签 ID** 为 2 的标签，即文章 1 既属于标签 1：django 学习，也属于标签 2：Python 学习。

反之，**标签 ID** 为 1 的标签，既对应着 **文章 ID** 为 1 的文章，也对应着 **文章 ID** 为 2 的文章，即标签 1：django 学习下有两篇文章。