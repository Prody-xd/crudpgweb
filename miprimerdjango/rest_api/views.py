from django.shortcuts import render
from core.models import mecanicos
from .serializers import mecanicosSerializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def mecanicos(request):
  if request.method == 'GET':
    mecanicos = mecanicos.objects.all()
    serializer = mecanicosSerializers(mecanicos, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    data = JSONParser.parser(request)
    serializer = mecanicosSerializers(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)