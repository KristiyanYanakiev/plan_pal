from django.urls import path
from votes import views

app_name = 'votes'

urlpatterns = [
    path('<int:proposal_id>/', views.vote_on_proposal, name="vote"),
]