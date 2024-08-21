# Permissions and Groups Setup

Custom Permissions
-`can_view`: Allows users to view articles.
-`can_create`: Allows users to create new articles.
-`can_edit`: Allows users to edit existing articles.
-`can_delete`: Allows users to delete articles.

Groups
-**Viewers**: Can view articles.
-**Editors**: Can view, create, and edit articles.
-**Admins**: Can view, create, edit, and delete articles.

Usage in Views
-The `@permission_required` decorator is used to enforce these permissions in views.
-Example: `@permission_required('your_app.can_edit', raise_exception=True)` protects the edit view.
