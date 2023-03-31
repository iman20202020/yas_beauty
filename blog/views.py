from django.shortcuts import render
from django.urls import reverse


def named_blog_view(request, name):
    template_name = f'blog/{name}.html'
    context = {'name': name}
    return render(request, template_name, context)


def blog_view(request):
    return render(request,'blog/blogs.html', {})
