from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Blog

# Create your views here.

#def all_blogs(request):
#    return render(request,'blog/all_blogs.html')

# Create your views here.

def all_blogs (request):
    #order by date and limit to 5
    blogs = Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
