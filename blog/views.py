from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from blog.models import Blog
from django.views.generic import DetailView, TemplateView

from seo.mixins.views import (
    ViewSeoMixin,
    ModelInstanceViewSeoMixin,
    UrlSeoMixin
)



class IndexView(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs) :
        data = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(publish=True)
        data['blogs'] = blogs
        return data




def named_blog_view(request, slug):
    template_name = f'blog/{slug}.html'
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog}
    return render(request, template_name, context)


def blog_view(request):
    blogs = Blog.objects.filter(publish=True)
    return render(request, 'blog/index.html', {'blogs': blogs})

def view_blog2(request):
    blog = get_object_or_404(Blog, slug='blog2')
    return render(request, 'blog/blog2.html', {'blog': blog})