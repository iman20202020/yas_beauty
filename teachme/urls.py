from django.urls import path

from teachme import views

app_name = 'teachme'
urlpatterns = [
    path('<slug>', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('teacher/request/send/<int:teacher_id>', views.teacher_request_send, name="teacher_request_send"),
    # path('<str:teachers_syllabus>/', views.teachers_list, name="teachers_list"),
    path('comment/<int:teacher_id>/', views.comment, name='comment'),

    path('list/<syllabus>', views.TeacherList.as_view(), name='teachers_list'),
]
