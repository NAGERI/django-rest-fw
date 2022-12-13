from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
  # This mixin can be reused in many ot
  permissions_classes = [permissions.IsAdminUser, IsStaffEditorPermission]