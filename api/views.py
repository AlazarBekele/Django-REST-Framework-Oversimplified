from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import Usersserializer

# Create your views here.
@api_view (['GET'])
def get_data (request):
  return Response (Usersserializer({'name' : 'Alazar', 'age' : 17}).data)