from datetime import date
from django.shortcuts import render
from rest_framework import response
from rest_framework.serializers import Serializer
from core.models import mecanico
from .serializers import MecanicoSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def mecanicos(request):
    """listar todos los mecanicos"""
    if request.method == 'GET':
        mecanicos = mecanico.objects.all()
        serializer = MecanicoSerializer(mecanicos, many=True)
        return Response(serializer.data)
        """Agregar mecanicos"""
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MecanicoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])        
def mecanic(request, pk):
    """Traer elemento de la bdd"""
    try:
        mecanic = mecanico.objects.get(phone=pk)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        """Mostrar un solo mecanico"""
        serializer = MecanicoSerializer(mecanico)
        return Response(serializer.data)

    if request.method == 'PUT':
        """Edita un solo mecanico"""
        data = JSONParser().parse(request)
        serializer = MecanicoSerializer(mecanico, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mecanico.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)