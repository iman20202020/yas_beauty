from django.urls import path

from blog import views

urlpatterns = [

    path('view/<int:blog_num>',views.show_blog, name='show_blog'),
]
