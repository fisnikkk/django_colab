from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_profiles/', views.UserProfileListView.as_view(), name='user_profile_list'),
    path('user_profiles/create/', views.UserProfileCreateView.as_view(), name='user_profile_create'),
    path('user_profiles/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user_profiles/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='user_profile_delete'),
    path('', views.my_model_list, name='my_model_list'),
    path('my_model/<int:pk>/', views.MyModelDetailView.as_view(), name='my_model_detail'),
    path('my_model/create/', views.MyModelCreateView.as_view(), name='my_model_create'),
    path('my_model/<int:pk>/update/', views.MyModelUpdateView.as_view(), name='my_model_update'),
    path('my_model/<int:pk>/delete/', views.MyModelDeleteView.as_view(), name='my_model_delete'),
]
