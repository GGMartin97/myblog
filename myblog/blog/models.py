from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#分类
class Category(models.Model):
	name = models.CharField(max_length=100)
	#在shell环境下返回分类名字
	
	def __str__(self):
		return self.name

#标签
class Tag(models.Model):
	name=models.CharField(max_length=100)
	#在shell环境下返回标签名字
	def __str__(self):
		return self.name

#文章
class Post(models.Model):
	#文章的标题
	title=models.CharField(max_length=70)
	#文章的正文
	body=models.TextField()
	#文章的创建时间和修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	#文章摘要，当CharField有参数blank=True即可空白避免报错
	excerpt = models.CharField(max_length=200,blank=True)
	#每篇文章可以对应很多标签，而一个标签也可以对应很多文章，所以ManyToManyField()参数加上blank=True,
	#可以选择没有标签
	tags=models.ManyToManyField(Tag,blank=True)
	#一篇文章只有一个分类，而一个分类对应多篇文章，所以用ForeignKey()
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	#文章作者，django自带用户模型，同样一对多关系
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	#
	#在shell环境下返回标题
	def __str__(self):
		return self.title

