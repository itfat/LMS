from rest_framework import serializers
from book.models import Book
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    # book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
