from rest_framework.permissions import BasePermission


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Viewer').exists()
    
class IsPoster(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Poster').exists()
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()