from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
    path('bookshelf/', include('bookshelf.urls')),
]
