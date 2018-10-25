from django.urls import path
from . import views
app_name='blog'#消除模板找不到空间名

urlpatterns = [
	path('',views.index,name='index'),
	path('post/<int:post_id>',views.detail, name='detail'),
	]