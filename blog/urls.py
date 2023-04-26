from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<slug:name>', views.named_blog_view, name='named_blog_view')
]
