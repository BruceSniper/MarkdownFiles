# 创建Django项目

## 1. 使用Pycharm创建django项目
> Location: E:\EyeGlassesKnowledgeGraphSystem
> 
> New environment using Virtualenv

**一定一定要勾选“Inherit global site-pankages”**，否则会报错：“Django is not importable in this environment”

## 2. 创建后端
进入项目根目录，创建一个 App 作为项目后端

```python
cd pc_admin
pipenv run python manage.py startapp backend　　　# backend就是app名称
```

创建成功后目录如下:

```
.
├── backend
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── EyeGlassesKnowledgeGraphSystem
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 3. 创建前端

* 使用cnpm 下载vue-cli

```
cnmp install -g @cue/cli
```

* 使用vue-cli在根目录创建一个名称叫【frontend】的Vue.js项目作为项目前端

```
vue-init webpack frontend
```

创建成功后目录如下

```
.
├── backend
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── frontend
│   ├── README.md
│   ├── build
│   │   └── ....
│   ├── config
│   │   ├── dev.env.js
│   │   ├── index.js
│   │   ├── prod.env.js
│   │   └── test.env.js
│   ├── index.html
│   ├── package.json
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   └── logo.png
│   │   ├── components
│   │   │   └── HelloWorld.vue
│   │   └── main.js
│   ├── static
│   └── test
│       └── ...
├── manage.py
└── EyeGlassesKnowledgeGraphSystem
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

* 使用 webpack 打包vue项目

```
cd frontend
npm install
npm run build
```

此时直接运行npm run dev也可以直接查看前端 vue界面

构建完成会生成一个文件夹，名字叫dist，里面有一个 index.html 和一个 文件夹static。

## 4. 前后端结合设置

使用Django的通用视图 TemplateView修改静态指向路径（就是让Django访问目录指向我们刚才打包的dist/index.html）

找到项目根目录 EyeGlassesKnowledgeGraphSystem/urls.py文件作出如下修改：

```python
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView  # 注意加上这句

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
]
```

配置Django项目的模板搜索路径和静态文件搜索路径 找到根目录下 EyeGlassesKnowledgeGraphSystem/settings.py文件并打开，找到TEMPLATES配置项，修改如下:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS':['frontend/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Add for vue.js
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/static"),
]
```

项目即可运行

## 5. ECharts设置

1. 进入frontend文件夹安装echarts

```
cd frontend
cnpm install echarts
```

2. 安装pyecharts

```
# 项目根目录
pipenv install pyecharts
```

## 6. 安装Django rest framework

`pipenv install djangorestframework markdown django-filter`

将`'rest_framework'`加入到settings.py的`INSTALLED_APPS`里

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'rest_framework',
]
```