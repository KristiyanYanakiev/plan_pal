from django.urls import path
from .views import (
    SendConnectionRequestView,
    AcceptConnectionRequestView,
    UserListView,
    PendingRequestsView
)

app_name = 'connections'

urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
    path('requests/', PendingRequestsView.as_view(), name='requests'),

    path('send/<int:user_id>/', SendConnectionRequestView.as_view(), name='send'),
    path('accept/<int:connection_id>/', AcceptConnectionRequestView.as_view(), name='accept'),
]