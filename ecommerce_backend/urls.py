from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # For API endpoints
    path('', include('store.urls')),      # For React frontend routing
]
