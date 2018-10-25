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
