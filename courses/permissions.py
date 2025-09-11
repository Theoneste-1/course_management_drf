from rest_framework import permissions

class IsInstructorsOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name='Instructors').exists()
class  IsOwnEnrollment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.student == request.user
        return obj.student == request.user
    