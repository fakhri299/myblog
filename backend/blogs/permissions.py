from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

class OwnProfilorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if  request.user == obj.author:
                return True
            else:
                return False

class OwnCommentorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if  request.user == obj.author:
                return True
            else:
                return False
        


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or   is_admin