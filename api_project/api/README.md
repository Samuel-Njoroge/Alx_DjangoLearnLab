"""
Authentication:
- Token-based authentication is used.
- Tokens can be obtained via /api/token/ by POSTing username and password.

Permissions:
- All API endpoints require authentication (IsAuthenticated).
- To test, include the token in the Authorization header: 'Authorization: Token <token>'.
"""
