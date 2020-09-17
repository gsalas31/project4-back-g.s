from django.urls import path, include
from rest_framework import routers
from apps.api.views import CategoryViewSet, CategoryProducts, CategoryTutorials

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
urlpatterns = [
    path('', include(router.urls))

]