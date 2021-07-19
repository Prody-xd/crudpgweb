from rest_framework import serializers
from core.models import mecanico

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mecanico
        fields = ['name', 'phone', 'email', 'website']