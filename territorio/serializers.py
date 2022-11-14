from rest_framework import serializers
from .models import Territorio

class TerritorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territorio
        fields = ('id','idTerritorio','nombre','created_at')
        read_only_fields =('created_at', )