from django.urls import path

from user import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/<id_arg>/', views.user_detail),
]
