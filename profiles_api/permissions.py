from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj): 
        """Check user is trying to edit tjeir own profile"""
        if request.method in permissions.SAFE_METHODS: 
            return True

        return obj.id == request.user.id 


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to edit their own status"""

    def has_object_permission(self, request, view, obj): 
        """Check the user is trying to edit tjeir own status"""
        if request.method in permissions.SAFE_METHODS: 
            return True

        return obj.id == request.user.id 

