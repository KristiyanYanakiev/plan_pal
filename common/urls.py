from django.urls import path

from common import views

urlpatterns = [
    path('', views.home_page, name='home')
]