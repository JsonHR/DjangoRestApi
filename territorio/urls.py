from rest_framework import routers
from .api import TerritorioViewSet

router = routers.DefaultRouter()

router.register('api/territorio',TerritorioViewSet,'territorio')

urlpatterns = router.urls