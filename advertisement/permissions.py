from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    # def has_permission(self, request, view):
    #     """ Работает над несколькими объектами (Create, List) """
    #     return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        """ Работа с одним объектом (Update, Delete) """
        return request.user.is_authenticated and obj.author == request.user