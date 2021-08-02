from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', views.user_profile, name='user_profile'),
    path('messages/<int:pk>/', views.PrivateMessageView.as_view(), name='private_message')
]