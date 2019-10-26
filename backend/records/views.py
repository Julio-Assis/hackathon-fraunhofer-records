from django.shortcuts import render
from django.http import HttpResponse
from records.models import (
    MachineRecord,
    VariableRecord,
    CauseRecord
)
from rest_framework.viewsets import ReadOnlyModelViewSet
from records.serializers import (
    MachineRecordSerializer,
    VariableRecordSerializer
)
from django.views.decorators.csrf import csrf_exempt

'''
message = {
    'machine': 1,
    'variables': [{
        'id': 0,
        'value': 10,
        'timestamp': 123,
    },{
        'id': 1,
        'value': 20,
        'timestamp': 123,
    },{
        'id': 2,
        'value': 30,
        'timestamp': 123,
    },],
    'status': 1,
    'stop_timestamp': 1231241,
    'duration': 1234,
    'cause': {
        'id': 0,
        'extras': ''
    }
}


'''

@csrf_exempt
def index(request):
    if request.method != 'POST':
        return HttpResponse('request should be post')

    payload = request.POST
    if not is_message_valid(payload):
        return HttpResponse('invalid payload here')

    import ipdb; ipdb.set_trace()
    machine_record = MachineRecord(
        machine_id=payload['machine'],
        status=payload['status'],
        stop_timestamp=payload['stop_timestamp'],
        duration=payload['duration']
    )

    machine_record.save()

    for variable in payload['variables']:
        variable_record = VariableRecord(
            variable=variable.id,
            machine_record=machine_record,
            value=variable.value,
            timestamp=variable.timestamp
        )
        variable.save()

    cause_record = CauseRecord(
        cause=payload.cause.id,
        extras=payload.cause.extras,
        machine_record=machine_record
    )

    cause_record.save()
    return HttpResponse('record saved successfully')


class MachineRecordViewSet(ReadOnlyModelViewSet):
    serializer_class = MachineRecordSerializer
    queryset = MachineRecord.objects.all()


class VariableRecordViewSet(ReadOnlyModelViewSet):
    serializer_class = VariableRecordSerializer
    queryset = VariableRecord.objects.all()


'''
message = {
    'machine': 0,
    'variables': [],
    'status': 1,
    'stop_timestamp': 1231241,
    'duration': 1234,
    'cause': {
        'id': 0,
        'extras': ''
    }
}


'''


def is_message_valid(message):

    if not message.get('machine'):
        return False

    if not message.get('variables'):
        return False

    if not message.get('status'):
        return False

    if not message.get('stop_timestamp'):
        return False

    if not message.get('duration'):
        return False

    if not message.get('cause'):
        return False

    return True
