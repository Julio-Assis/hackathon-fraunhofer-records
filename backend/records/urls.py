from django.urls import path
from django.conf.urls import include, url
from records.views import (
    index,
    MachineRecordViewSet,
    MachineViewSet,
    CauseViewSet,
)
from rest_framework_nested import routers


machines_router = routers.SimpleRouter()
machines_router.register(
    '',
    MachineRecordViewSet,
    base_name='machines'
)

list_machines_router = routers.SimpleRouter()
list_machines_router.register(
    '',
    MachineViewSet,
    base_name='list-machines'
)

causes_router = routers.SimpleRouter()
causes_router.register(
    '',
    CauseViewSet,
    base_name='causes'
)

app_name = 'records'
urlpatterns = [
    path(r'', index, name='index'),
    url(r'list-machines/', include((list_machines_router.urls, None))),
    url(r'machines/', include((machines_router.urls, None))),
    url(r'causes/', include((causes_router.urls, None))),
]
