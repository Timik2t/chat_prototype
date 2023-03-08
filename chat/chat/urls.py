from django.contrib import admin
from django.urls import path, include
from private_chat import views

urlpatterns = [
    path('chat/', include('private_chat.urls')),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('admin/', admin.site.urls),
]
