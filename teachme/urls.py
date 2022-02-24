from django.urls import path

from teachme import views

app_name = 'teachme'
urlpatterns = [
    path('teacher/list/<str:category_id>/<str:syllabus_id>', views.teacher_list, name="teacher_list"),
    path('teacher/detail/<int:teacher_id>/<str:teacher_cat>', views.teacher_detail, name="teacher_detail"),
    path('teacher/request/<int:teacher_id>', views.teacher_request, name="teacher_request"),
]
