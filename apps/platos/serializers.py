from apps.platos.models import Platos
from rest_framework import serializers

class PlatosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platos
        fields = '__all__'