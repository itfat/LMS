from django.urls import include, path

from book import views

urlpatterns = [
    path('books/', views.book_list),
    path('book/<pk>/', views.book_detail),
]
   