from django.conf.urls import re_path
from .views import status

urlpatterns = [
    re_path(r'^$', status, name='status'),
]
