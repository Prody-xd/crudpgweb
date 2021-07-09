from django.http import response
from django.shortcuts import render
from .models import mecanicos
from .serializers import mecanicosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_api import serializers


class mecanicosApiView (APIView):
  """Api View de Prueba"""
  serializer_class = serializers.mecanicosSerializers
  def get(self, request, format=None):
    """Retornar lista de caracteristicas del APIView"""
    an_apiview = [
      'Diego Santana',
      '975416016',
      'diegosantana@gmail.com',
      'medicion de kilometraje',
      '3 años de experiencia'
    ],[
      'Joel Salinas',
      '45320879',
      'joelsalinas@gmail.com',
      'Mantencion de Motor',
      '2 años de experiencia'
    ]
    return Response({'message': 'hello', 'an_apiview': an_apiview})

  def post(self, request):
     serializer = self.serializer_class(data=request.data)

     if serializer.is_valid():
       nombre = serializer.validated_data.get('nombre')
       message = f'hello {nombre}'
       return Response({'message':message})
     else:
       return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
       )


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

  def put(self, request, pk=None):
    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):

    return Response({'method': 'PATCH'})
  def delete(self, request, pk=None):
    
    return Response({'method': 'DELETE'})
