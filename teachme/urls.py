from django.urls import path

from teachme import views

app_name = 'teachme'
urlpatterns = [
    # path('',views.index,name='teachme_index'),
    # path('teacher/list', views.teacher_list, name="teacher_list"),
    path('teacher/detail/<int:teacher_id>', views.teacher_detail, name="teacher_detail"),
    path('teacher/request', views.teacher_request, name="teacher_request"),
    path('message/viewer/<str:message_get>', views.message_viewer, name='message_viewer'),
]
