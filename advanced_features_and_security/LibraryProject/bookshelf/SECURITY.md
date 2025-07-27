# Django Security Configuration

## Secure Settings
- DEBUG set to False
- CSRF and session cookies secured for HTTPS
- XSS and clickjacking protections enabled

## CSRF Protection
- All form templates use `{% csrf_token %}`

## ORM-Based Data Access
- Django ORM used for all queries to avoid SQL injection
- Inputs validated using Django Forms

## Content Security Policy
- Configured via `django-csp` middleware
- Restricts content sources to trusted domains only

## Testing
- Manually tested for CSRF, XSS, and unauthorized data access
