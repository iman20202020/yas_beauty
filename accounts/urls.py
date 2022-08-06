from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index_accounts, name='index_accounts'),
    path('base/', views.base_view, name='base_view'),
    path('user/verify', views.user_verify, name='user_verify'),
    path('user/create', views.user_create, name='user_create'),
    path('teacher/edit/', views.teacher_edit, name='teacher_edit'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('logout/',views.logout_view, name='logout_view'),
    path('accounts/login/',views.login_view, name='login_view'),
    path('search/', views.search_view, name='search_view'),
    path('contact-us/',views.contact_us, name='contact_us'),
    path('pass-reset/',views.pass_reset, name='pass_reset'),
    # path('pass-reset-conf/',views.pass_reset_confirmed, name='pass_reset_confirmed'),
    path('site/laws/',views.site_laws, name='site_laws'),
    path('how/use/',views.how_use, name='how_use'),
    path('how/use2/',views.how_use2, name='how_use2'),
    path('teacher/laws/', views.teacher_laws, name='teacher_laws'),

    path('beauty-trainings/', views.beauty_trainings, name='beauty_trainings'),
    path('high-school-trainings/', views.high_school_trainings, name='high_school_trainings'),
    path('mid-school-trainings/', views.mid_school_trainings, name='mid_school_trainings'),
    path('music-trainings/', views.music_trainings, name='music_trainings'),
    path('language-trainings/', views.language_trainings, name='language_trainings'),
]

