from rest_framework.permissions import BasePermission

def IsInGroupsPerm(groups):
    class DynamicGroupPermissions(BasePermission):
        def has_permission(self, request, view):
            # Add inside has_permission for debugging
            print(f"User: {request.user}, Groups: {[g.name for g in request.user.groups.all()]}, Superuser: {request.user.is_superuser}")
            
            return (
                request.user
                and request.user.is_authenticated
                and (
                    request.user.is_superuser or
                    request.user.groups.filter(name__in=groups).exists()
                )
            )
    return DynamicGroupPermissions

