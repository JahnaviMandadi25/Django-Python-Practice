from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about_me, name='about_me'),  # Ensure this path is correct
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
