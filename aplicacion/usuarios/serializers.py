from rest_framework import serializers
from .models import persona


class MipersonaSerializer(serializers.ModelSerializer):
    #esta clase especifica el modelo de django
    class Meta:
        model = persona
        fields = '__all__'