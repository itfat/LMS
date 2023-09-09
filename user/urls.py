from django.urls import path

from user import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('user/<pk>/', views.UserDetail.as_view()),
]
