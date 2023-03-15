from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from apps.meseros.models import Meseros
from apps.meseros.forms import MeserosForm
from apps.meseros.serializers import MeserosSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def index_meseros(request):
    meseros = Meseros.objects.filter(procedencia='Perú').filter(edad__lt=30)
    d = {'meseros': meseros}
    return render(request, 'meseros/index_meseros.html', d)

def index_meseros_peru(request):
    meseros = Meseros.objects.filter(procedencia='Perú')
    d = {'meseros': meseros}
    return render(request, 'meseros/index_meseros.html', d)

def update_meseros(request):
    meseros = Meseros.objects.filter(procedencia='Perú').filter(edad__lt=30).update(edad=5)
    d = {'meseros': meseros}
    return render(request, 'meseros/index_meseros.html', d)

def carga_meseros(request, meseros_id=None):
    form = MeserosForm()
    if request.method == 'POST':
        if meseros_id is None:
            form = MeserosForm(request.POST)
        else:
            form = MeserosForm(request.POST, instance=get_object_or_404(Meseros, pk=meseros_id))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('meseros:index_meseros'))
    elif meseros_id is not None:
        try:
            p = get_object_or_404(Meseros, id=meseros_id)
            form = MeserosForm(instance=p)
        except:
            form = MeserosForm()
    if meseros_id is not None:
        return render(request, 'meseros/carga_meseros.html', {'formulario': form, 'meseros_id': meseros_id}) 
    return render(request, 'meseros/carga_meseros.html', {'formulario': form})

def borrar_meseros(request, meseros_id):
    query = Meseros.objects.get(id=meseros_id)
    query.delete()
    return HttpResponse("Mesero borrado.")

class MeserosViewSet(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, format=None, meseros_id=None):
        if meseros_id is None:
            meseros = Meseros.objects.all()
        else:
            meseros = Meseros.objects.filter(id=meseros_id)
        serializer = MeserosSerializer(meseros, many=True)
        return Response(serializer.data)

    def put(self, request, meseros_id=None, format=None):
        meseros = Meseros.objects.get(id=meseros_id)
        serializer = MeserosSerializer(meseros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, meseros_id=None, format=None):
        meseros = Meseros.objects.filter(username=meseros_id)
        if meseros:
            meseros.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
