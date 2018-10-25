# myblog
切换数据库sqlite至mysql（所需库mysql-server, mysqlclient #连接python）
mysql基本语法
venv用法,分python2和python3环境

day 1:
博客应用的数据框架：文章分类，文章标签，文章主体（标题，正文，创建时间，摘要）

关系：文章主题与分类的关系，文章一对一，分类一对多，ForeignKey()
      文章主体与标签的关系，文章多对多，分类多对多，ManyToManyField()
day 2:
httpresponse 在 django.http

模板技巧 {% load static files % } 用来加载文本标签使定位到正确路径的static
{% static 'blog/css/bootstrap.min.css' %}

语句用{% endfor %} 结束

admin.py 用于注册数据库中的成员用于编辑

reverse函数位于 django.urls库 用于解析url并返回一个地址，第一参数为解析对象url，第二个参数为所需参数，（我们设定的 name='detail' 在这里派上了用场。看到这个 reverse 函数，它的第一个参数的值是 'blog:detail'，意思是 blog 应用下的 name=detail 的函数，由于我们在上面通过 app_name = 'blog' 告诉了 Django 这个 URL 模块是属于 blog 应用的，因此 Django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数，于是 reverse 函数会去解析这个视图函数对应的 URL，我们这里 detail 对应的规则就是 post/(?P<pk>[0-9]+)/这个正则表达式，而正则表达式部分会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。）
