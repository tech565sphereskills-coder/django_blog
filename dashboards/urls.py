from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Category crud operations
    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),

    # blog post crud operations
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/edit/<int:id>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:id>/', views.delete_post, name='delete_post'),

]