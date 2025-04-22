from rest_framework import serializers
from .models import GetData

class Usersserializer (serializers.ModelSerializer):
  class Meta:

    model = GetData
    fields = '__all__'