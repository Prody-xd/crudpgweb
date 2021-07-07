from django.db.models import fields
from rest_framework import serializers
from core.models import mecanicos

class mecanicosSerializers(serializers,serializers.ModelSerializer):
    class Meta:
        model = mecanicos
        fields['nombre','telefono','email','especialidad','tiempo_exp']