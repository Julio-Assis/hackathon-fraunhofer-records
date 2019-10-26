from django.shortcuts import render
from django.http import HttpResponse
from records.models import (
    MachineRecord,
    VariableRecord,
    CauseRecord
)

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


def index(request):
    payload = request.body

    if not is_message_valid(payload):
        return HttpResponse('invalid payload here')

    machine_record = MachineRecord(
        machine=payload.id,
        status=payload.status,
        stop_timestamp=payload.stop_timestamp,
        duration=payload.duration
    )

    machine_record.save()

    for variable in payload.variables:
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

    if not message['machine']:
        return False

    if not message['variables']:
        return False

    if not message['status']:
        return False

    if not message['stop_timestamp']:
        return False

    if not message['duration']:
        return False

    if not message['cause']:
        return False

    return True
