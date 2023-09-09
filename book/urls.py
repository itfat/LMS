from django.urls import path

from book import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<pk>/', views.BookDetail.as_view()),
    path('book/assign/<pk>/', views.BookAssign.as_view(), name="assign_book"),
]
   