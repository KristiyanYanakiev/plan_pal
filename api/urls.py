from django.urls import path
from .views import ProposalListCreateAPI, ProposalDetailAPI, VoteAPI

urlpatterns = [
    path('proposals/', ProposalListCreateAPI.as_view(), name='api-proposals'),
    path('proposals/<int:pk>/', ProposalDetailAPI.as_view(), name='api-proposal-detail'),
    path('proposals/<int:pk>/vote/', VoteAPI.as_view(), name='api-vote'),
]