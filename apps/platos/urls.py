from django.urls import re_path
from django.contrib.auth.decorators import login_required
from apps.platos import views
from apps.platos.views import *

app_name = 'apps.platos'
urlpatterns = [
    re_path(r'^$', login_required(views.index_platos), name='index_platos'),
    re_path(r'^serialized$', login_required(PlatostViewSet.as_view()), name='serialized_platos'),
]