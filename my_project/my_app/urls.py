from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_model_list, name='my_model_list'),
    path('my_model/<int:pk>/', views.MyModelDetailView.as_view(), name='my_model_detail'),
    path('my_model/create/', views.MyModelCreateView.as_view(), name='my_model_create'),
    path('my_model/<int:pk>/update/', views.MyModelUpdateView.as_view(), name='my_model_update'),
    path('my_model/<int:pk>/delete/', views.MyModelDeleteView.as_view(), name='my_model_delete'),
]
