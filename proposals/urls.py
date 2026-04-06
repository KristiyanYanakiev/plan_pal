from django.urls import path
from .views import (
    ProposalListView,
    ProposalCreateView,
    ProposalUpdateView,
    ProposalDeleteView,
    ProposalDetailView,
    VoteView,
)

app_name = 'proposals'

urlpatterns = [
    path('', ProposalListView.as_view(), name='list'),
    path('create/', ProposalCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', ProposalUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ProposalDeleteView.as_view(), name='delete'),
    path('<int:pk>/', ProposalDetailView.as_view(), name='details'),
    path('<int:pk>/vote/<int:value>/', VoteView.as_view(), name='vote'),
]