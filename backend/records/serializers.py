from rest_framework import serializers
from records.models import (
    Machine,
    MachineRecord,
    Variable,
    VariableRecord,
    Cause
)


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('name',)


class VariableRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariableRecord
        fields = '__all__'


class MachineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineRecord
        fields = ('id', 'machine', 'status', 'stop_timestamp',
                  'duration', 'operator_timestamp',
                  'variable_records',)

    expandable_fields = {
        'variable_records': (VariableRecordSerializer, {
            'source': 'variable_records',
            'fields': [
                'variable',
                'value'
            ],
            'many': True
        }),
    }
