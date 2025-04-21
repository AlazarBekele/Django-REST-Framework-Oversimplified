from rest_framework.response import Response # rendered out JSON data
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData (request):

  person = {'name' : 'Alazar', 'Age' : 17}

  return Response (person)