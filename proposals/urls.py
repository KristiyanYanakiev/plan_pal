from django.urls import path

from . import views
from .views import VoteView

app_name = 'proposals'

urlpatterns = [
    path('', views.ProposalListView.as_view(), name='list'),
    path('create/', views.ProposalCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.ProposalUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProposalDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.ProposalDetailView.as_view(), name='details'),
path('<int:pk>/vote/<int:value>/', VoteView.as_view(), name='vote')
]