from .views import RegisterAPIs, ProfileAPIs

from django.urls import path, include

urlpatterns = [    
    # path('api-auth/', include('rest_framework.urls'))
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPIs.as_view()),
    path("profile/<int:id>", ProfileAPIs.as_view()),

]