from rest_framework.decorators import api_view
from rest_framework.response import Response
from memoriesapp.models import Memories
from .serializers import memoriesserializer

@api_view(['GET'])
def getposts(request):
    obj = Memories.objects.all()
    oj = memoriesserializer(obj, many = True)

    return Response(oj.data)
