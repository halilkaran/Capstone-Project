from django.contrib import admin
from django.urls import path, include

# These are for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="BLOG APP API",
      default_version='v0.1',
      description="This is for BlogApp ",
      terms_of_service="#",
      contact=openapi.Contact(email="halilkarancontact@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include('debug_toolbar.urls')),
    
    #myapps
    path('users/', include("users.urls")),
    path('api/', include("blogApp.urls")),
]
