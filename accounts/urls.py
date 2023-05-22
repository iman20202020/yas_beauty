from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index_accounts, name='index_accounts'),
    path('user/verify', views.user_verify, name='user_verify'),

    # path('teacher/edit/', views.teacher_edit, name='teacher_edit'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('logout/',views.logout_view, name='logout_view'),
    path('accounts/login/',views.login_view, name='login_view'),
    path('search/', views.search_view, name='search_view'),
    path('contact-us/',views.contact_us, name='contact_us'),
    path('site/laws/',views.site_laws, name='site_laws'),
    path('how/use/',views.how_use, name='how_use'),
    path('how/use2/',views.how_use2, name='how_use2'),
    path('teacher/laws/', views.teacher_laws, name='teacher_laws'),
    path('consult/', views.consult_view, name='consult_view'),





]

