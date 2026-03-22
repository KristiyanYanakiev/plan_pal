from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.FriendListView.as_view(), name='list'),
]