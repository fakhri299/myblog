from rest_framework import permissions

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
        