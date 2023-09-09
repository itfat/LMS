from rest_framework import permissions

class IsAdminOrManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request
        print("======================user=1============")
        print(user)
        print("======================user=============")
        return user.role in ["ADMIN", "MANAGER"]

class IsAdminOrManagerOrUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request
        print("======================user=2============")
        print(user)
        print("======================user=============")
        return user.role in ["ADMIN", "MANAGER", "NORMAL"]

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        
        user = request
        print("======================user=3============")
        print(user)
        print("======================user=============")
        return user.role == "ADMIN"
