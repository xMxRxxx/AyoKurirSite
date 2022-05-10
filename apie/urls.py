
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', listTodoItem.as_view()),
    path('detailItem/<int:pk>/', detailTodoItem.as_view()),
    path('userprofil/<str:Username>/<str:Password>', listTodoDetailUser.as_view()),
    # path('message/', listTodoMessage.as_view()),
    path('getImageProduct/<int:product_id>/', getImageProduct),
    path('getUser/<str:Email>/<str:Password>', getUser),

    path('getDetailMessages/<int:sender>/<int:receiver>/', getDetailMessages),
    path('getListMessages/<int:sender>/<int:receiver>/', getListMessages),

    
]
