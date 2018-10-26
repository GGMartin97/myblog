from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm
# Create your views here.


def post_comment(request,post_pk):
	#获取评论文章，后面用来关联
	post = get_object_or_404(Post,pk=post_pk)


	#POST请求才是提交表单
	form = CommentForm(request.POST)

	#检查表单是否符合要求
	if form.is_valid():
		comment = form.save(commit=False)
		
		comment.post = post

		comment.save()

		return redirect(post)

	else:
		comment_list = post.comment_set.all()
		conntext = {'post':post,
					'form':form,
					'comment_list':comment_list

		}
		return render(request,'blog/detail.html',conntext=conntext)
	return redirect(post)

