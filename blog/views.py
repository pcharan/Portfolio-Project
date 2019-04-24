from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
	blog = Blog.objects
	return render(request, 'bloghome.html', {'blogs':blog})

def detail(request, blog_id):
	detailblog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'detail.html', {'blog':detailblog})
	