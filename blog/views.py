from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def showblog(request):
    blogs = Blog.objects.all()
    return render(request,'blog/blog.html',{'blogs':blogs})

def post_details(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request,'blog/post_details.html', {'blog':post})

