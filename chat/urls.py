from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('search', views.SearchChatView.as_view(), name='search_result'),
    path('<slug:slug>/', views.chat_detail, name='detail'),
    path('', views.index, name='home'),

]