from django.urls import path, include

from book import views

urlpatterns = [
    path('books/', views.book_list),
    path('book/<id_arg>/', views.book_detail),
]
   