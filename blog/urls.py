from django.urls import path

from blog import views

urlpatterns = [

    path('view/<int:blog_num>',views.show_blog, name='show_blog'),
    path('teachers',views.view_all_teachers, name='view_all_teachers'),
    path('teachers/generator',views.teacher_list_generator, name='teacher_list_generator'),
]
