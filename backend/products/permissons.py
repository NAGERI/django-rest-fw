from rest_framework import permissions

# THis is a custom permission class.
class IsStaffEditorPermission(permissions.DjangoModelPermissions):
  perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
  def has_permission(self, request, view):
    if not request.user.is_staff: # This can check a payment layer
      return False # Means this user is not AdminUser
    return super().has_permission(request, view);
    """
    user = request.user
    print(user.get_all_permissions())
    if user.is_staff:
      if user.has_perm("products.add_product"): # ""
        return True
      return True
    #default should return False
    return False
    """
