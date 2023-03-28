from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('<str:name>', views.blog_view, name='blog_view'),

]
