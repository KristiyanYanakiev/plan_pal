from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'comments'

urlpatterns = [
    path('create/<int:pk>/', CommentCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', CommentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='delete'),
]