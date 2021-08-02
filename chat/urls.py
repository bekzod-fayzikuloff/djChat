from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('delete/<int:pk>/<slug:chat_slug>', views.MemberLeaveView.as_view(), name='member_leave'),
    path('<slug:slug>/', views.chat_detail, name='detail'),
    path('', views.index, name='home'),
]