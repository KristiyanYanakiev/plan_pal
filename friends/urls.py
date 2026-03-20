from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.FriendListView.as_view(), name='list'),
    path('create/', views.FriendCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.FriendUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.FriendDeleteView.as_view(), name='delete'),

    path('groups/', views.FriendGroupListView.as_view(), name='group-list'),
    path('groups/create/', views.FriendGroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/edit/', views.FriendGroupUpdateView.as_view(), name='group-edit'),
    path('groups/<int:pk>/delete/', views.FriendGroupDeleteView.as_view(), name='group-delete'),
]
