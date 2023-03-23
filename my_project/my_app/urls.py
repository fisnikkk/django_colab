from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .models import BlogPost, UserProfile, User

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('user_profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='user_profile_detail'),
    path('register/', views.register, name='register'),
    path('user_profiles/', views.user_profile_list, name='user_profile_list'),
    path('user_profiles/create/', views.UserProfileCreateView.as_view(), name='user_profile_create'),
    path('user_profiles/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user_profiles/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='user_profile_delete'),
    path('blog_post/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_post/create/', views.BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog_post/<int:pk>/update/', views.BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog_post/<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
