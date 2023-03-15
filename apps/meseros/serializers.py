from apps.meseros.models import Meseros
from rest_framework import serializers

class MeserosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meseros
        fields = '__all__'