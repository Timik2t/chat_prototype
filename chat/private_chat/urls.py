from django.urls import path
from private_chat.views import MessagesListView, ChatView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('messages/<int:pk>/', MessagesListView.as_view(), name='messages'),
]
