### Permissions and Groups Setup (Documentation)

Defined custom model permissions for the Book model:

- can_view
- can_create
- can_edit
- can_delete

Groups created in the admin panel:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views are protected using `@permission_required` decorators.

To test:
- Create users in Django admin.
- Assign them to appropriate groups.
- Log in and verify access to `book` views is correctly restricted.

Permissions are enforced using:
@permission_required('relationship_app.can_edit', raise_exception=True)
