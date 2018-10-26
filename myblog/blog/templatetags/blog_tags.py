from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag  #注册为模板标签
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num] #导入前五的数据

@register.simple_tag
def archives():
	return Post.objects.dates('created_time','month',order='DESC')#创建时间，精确到月份并降序排序

@register.simple_tag
def get_categories():
	return Category.objects.all()




