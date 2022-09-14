from rest_framework.serializers import ModelSerializer
from memoriesapp.models import Memories

class memoriesserializer(ModelSerializer):
    class Meta:
        model = Memories
        fields = "__all__"