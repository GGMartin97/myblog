from django.urls import path
from . import views
app_name='blog'#消除模板找不到空间名

urlpatterns = [
	path('',views.index,name='index'),
	path('post/<int:post_id>',views.detail, name='detail'),
	path('archives/<int:year>/<int:month>',views.archives,name='archives'),
	path('category/<int:pk>',views.category,name='category'),
	path('maintenance',views.maintenance,name='maintenance'),
	path('about',views.about,name='about'),
	path('contact',views.contact,name='contact'),
	path('bloglist',views.bloglist,name='bloglist'),
	]