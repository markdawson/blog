from django.shortcuts import render, get_object_or404
from .models import Post

def post_list(request):
	post = Post.published.all()
	return render(request,
		'blog/post/list.html',
		{'posts': post})