from django.urls import path, include

from book import views

urlpatterns = [
    path('books/', views.get_all, name="book_list"),
    path('book/<id_arg>', views.get, name="get_book"),
    path('book/<id_arg>', views.delete, name="delete_book"),
    path('book/', views.post, name="add_book"),
    path('book/<id_arg>', views.update, name="update_book")

]
   