from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index_accounts, name='index_accounts'),
    path('base/', views.base_view, name='base_view'),
    path('user/verify', views.user_verify, name='user_verify'),
    path('user/create', views.user_create, name='user_create'),
    path('teacher/edit/', views.teacher_edit, name='teacher_edit'),
    path('student/edit/', views.student_edit, name='student_edit'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('logout/',views.logout_view, name='logout_view'),
    path('accounts/login/',views.login_view, name='login_view'),
    path('search/', views.search_view, name='search_view'),
    path('contact-us/',views.contact_us, name='contact_us' ),
    path('pass-reset/',views.pass_reset, name='pass_reset' ),
    path('pass-reset-conf/',views.pass_reset_confirmed, name='pass_reset_confirmed' ),
    path('site/laws/',views.site_laws, name='site_laws' ),


]

