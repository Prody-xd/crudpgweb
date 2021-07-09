from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import mecanicos

class mecanicosSerializers(serializers.ModelSerializer):
    
    nombre = serializers.CharField(max_length=250)
    class Meta:
        model = mecanicos
        fields = ['nombre','telefono','email','especialidad','tiempo_exp']