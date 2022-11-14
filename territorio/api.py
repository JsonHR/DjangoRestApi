from .models import Territorio
from rest_framework import viewsets,permissions
from .serializers import TerritorioSerializer

class TerritorioViewSet(viewsets.ModelViewSet):
    queryset = Territorio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TerritorioSerializer