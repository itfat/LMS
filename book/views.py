from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from book.models import Book
from book.serializers import BookSerializer
from library.permissions import IsAdminOrManagerOrReadOnly, IsAdminOrManagerOrUser


class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrManagerOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookAssign(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrManagerOrUser]  # Allow assignment for all users

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.status == "AVAILABLE":
            user = request.user
            instance.user = user
            instance.status = "ON_HOLD"
            instance.save()

            return Response({"message": "Book assigned successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Book is not available for assignment"}, status=status.HTTP_400_BAD_REQUEST)
