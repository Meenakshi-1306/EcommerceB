from django.urls import path, re_path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy, FrontendAppView

urlpatterns = [
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),  # catch-all for React
]
