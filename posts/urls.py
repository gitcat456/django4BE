from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('create/', views.create_post, name='create-post'),
    path('delete/', views.delete_post),
]