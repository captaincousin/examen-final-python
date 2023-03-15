from django.shortcuts import render
from apps.platos.models import Platos
from apps.platos.serializers import PlatosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

def index_platos(request):
    platos = Platos.objects.filter(procedencia='Perú').filter(precio__gte=40)
    d = {'platos': platos}
    return render(request, 'platos/index_platos.html', d)

class PlatostViewSet(APIView):

    def get(self, format=None):
        platos = Platos.objects.filter(precio__gte=50)
        serializer = PlatosSerializer(platos, many=True)
        return Response(serializer.data)