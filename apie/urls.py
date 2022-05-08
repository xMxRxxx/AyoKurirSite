
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', listTodoItem.as_view()),
    path('detailItem/<int:pk>/', detailTodoItem.as_view()),
    path('userprofil/', listTodoUser.as_view()),
    path('message/', listTodoMessage.as_view()),
]
