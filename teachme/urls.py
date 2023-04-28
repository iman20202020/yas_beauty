from django.urls import path

from teachme import views

app_name = 'teachme'
urlpatterns = [
    path('teacher/list/', views.teacher_list, name="teacher_list"),
    # path('<slug:teacher_slug>', views.teacher_detail, name="teacher_detail"),


    path('<slug>', views.TeacherDetailView.as_view(), name="teacher_detail"),


    path('teacher/request/send/<int:teacher_id>', views.teacher_request_send, name="teacher_request_send"),
# search pages
    path('nail-implants/', views.nail_implants, name="nail_implants"),
    path('eyebrow_microblading_training/', views.eyebrow_microblading_training, name="eyebrow_microblading_training"),
    path('eyebrow_lift_training/', views.eyebrow_lift_training, name="eyebrow_lift_training"),
    path('eyebrow_permanent_makeup_training/', views.eyebrow_permanent_makeup_training, name="eyebrow_permanent_makeup_training"),
    path('haircut-training/', views.haircut_training, name="haircut_training"),
    path('hair-coloring-training/', views.hair_coloring_training, name="hair_coloring_training"),
    path('face-balancing-training/', views.face_balancing_training, name="face_balancing_training"),
    path('extension-training-for-eylashes/', views.extension_training_for_eylashes, name="extension_training_for_eylashes"),
    path('face-cleaning-training/', views.face_cleaning_training, name="face_cleaning_training"),
    path('hair-dress-training/', views.hair_dress_training, name="hair_dress_training"),
    path('like/', views.like_view, name='like'),
    path('comment/<int:teacher_id>/', views.comment, name='comment'),
]
