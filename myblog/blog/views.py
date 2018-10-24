from django.shortcuts import render
from django.views.generic.detail import DetailView,ListView
# Create your views here.

class BlogListView(ListView):
	model = Blog 
	context_object_name = 'blogs'
	template_name = 'index.html'
