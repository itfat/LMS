from rest_framework import serializers
from book.models import Book
from user.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    class Meta:
        model = MyUser
        # fields = ['id', 'username', 'email', 'role']
        fields = '__all__'
