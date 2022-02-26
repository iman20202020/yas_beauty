from django.urls import path

from teachme import views

app_name = 'teachme'
urlpatterns = [
    path('teacher/list/', views.teacher_list, name="teacher_list"),
    path('teacher/detail/<int:teacher_id>/', views.teacher_detail, name="teacher_detail"),

    path('teacher/request/send/<int:teacher_id>', views.teacher_requst_send, name="teacher_request_send"),
    path('request/user/verify/<int:teacher_id>', views.request_user_verify, name="request_user_verify"),
]
