from django.urls import path, include
from proposals import views

app_name = 'proposals'

urlpatterns = [
    path('', views.proposals_list, name='list'),
    path('create/', views.create_proposal, name='create'),
    path('<int:pk>/', include([
        path('', views.proposal_details, name='details'),
        path('edit/', views.edit_proposal, name='edit'),
        path('delete/', views.delete_proposal, name='delete')

    ]))
]