from django.urls import path

from clerk import views

urlpatterns = [
    path('',views.index_clerk, name='index_clerk')
]