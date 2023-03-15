from django.urls import re_path
from django.contrib.auth.decorators import login_required
from apps.meseros import views
from apps.meseros.views import *

app_name = 'meseros'
urlpatterns = [
    re_path(r'^$', login_required(views.index_meseros), name='index_meseros'),
    re_path(r'^peru$', login_required(views.index_meseros_peru), name='index_meseros_peru'),
    re_path(r'^update$', login_required(views.update_meseros), name='update_meseros'),
    re_path(r'^cargar$', login_required(views.carga_meseros), name='carga_meseros'),
    re_path(r'^editar/(?P<meseros_id>\d+)$', login_required(views.carga_meseros), name='editar_meseros'),
    re_path(r'^borrar/(?P<meseros_id>\d+)$', login_required(views.borrar_meseros), name='borrar_meseros'),
    re_path(r'^serialized$', MeserosViewSet.as_view(), name='serialized_meseros'),
    re_path(r'^serialized/(?P<meseros_id>\d+)$', MeserosViewSet.as_view(), name='serialized_meseros_id'),
]