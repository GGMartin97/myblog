from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from comments.forms import CommentForm


# Create your views here.

def index(request):
	post_list=Post.objects.all().order_by('-created_time')
	return render(request,'blog/index.html',{'post_list':post_list})
 	#render通过传入参数构造httpresponse
def bloglist(request):
	post_list=Post.objects.all().order_by('-created_time')
	return render(request,'blog/full-width.html',{'post_list':post_list})

def detail(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	post.body = markdown.markdown(post.body,extensions=[
												'markdown.extensions.extra',
												'markdown.extensions.codehilite',
												'markdown.extensions.toc',
												])
	form = CommentForm()
	comments_list = post.comment_set.all()
	context = {	'post':post,
				'form': form,
				'comments_list':comments_list
	}

	return render(request,'blog/detail.html',context=context)

def archives(request, year, month): #获得日期分类
	post_list = Post.objects.filter(created_time__year=year,
									created_time__month=month,
									).order_by('-created_time')
	return render(request,'blog/index.html',{'post_list':post_list})

def category(request, pk):#获得分类分类
	cate = get_object_or_404(Category,pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'blog/index.html',context={'post_list':post_list})

def maintenance(request):
	return render(request,'blog/maintenance.html')

def about(request):
	return render(request,'blog/about.html')

def contact(request):
	return render(request,'blog/contact.html')