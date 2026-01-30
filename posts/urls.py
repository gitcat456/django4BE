from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('create/', views.create_post, name='create-post'),
    path('delete/', views.delete_post),
]

# The `urlpatterns` list routes URLs to views
# example 1: function views 
        # 2: class based views
        # 3: include another URLConf
        