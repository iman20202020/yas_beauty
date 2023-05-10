from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog_view'),

    path('<slug:slug>', views.named_blog_view, name='named_blog_view'),


    path('blog2/', views.view_blog2, name='view_blog2'),
    path('blog3/', views.IndexView.as_view(), name='view_blog3'),
]
