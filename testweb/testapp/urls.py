from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
