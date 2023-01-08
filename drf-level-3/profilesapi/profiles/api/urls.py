from django.urls import path, include
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'status', ProfileStatusViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),

]
