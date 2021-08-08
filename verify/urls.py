from django.urls import path

from verify import views

urlpatterns = [
    path('send_sms/', views.send_sms),
]
