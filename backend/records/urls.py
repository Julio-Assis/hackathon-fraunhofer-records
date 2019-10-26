from django.urls import path
from django.conf.urls import include, url
from records.views import (
    index,
    MachineRecordViewSet
)
from rest_framework_nested import routers


machines_router = routers.SimpleRouter()
machines_router.register(
    '',
    MachineRecordViewSet,
    base_name='machines'
)

app_name = 'records'
urlpatterns = [
    path(r'', index, name='index'),
    url(r'machines/', include((machines_router.urls, None))),
]
