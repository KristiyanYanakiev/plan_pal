

from django.urls import path, include

from friends import views

app_name = 'friends'
urlpatterns = [
    path('', views.friends_list, name='list'),
    path('create/', views.create_friend, name='create'),
    path('<int:pk>/', include([
        path('', views.friend_details, name='details'),
        path('edit/', views.edit_friend, name='edit'),
        path('delete/', views.delete_friend, name='delete')

    ]))

]