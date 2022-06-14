from django.urls import path, include
from blogApp.views import BlogCRUD

from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogs', BlogCRUD)


urlpatterns = [    
   # path('blog/', BlogList.as_view()),
   path('', include(router.urls)),
]