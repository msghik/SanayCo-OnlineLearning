from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsInstructor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'instructor'
