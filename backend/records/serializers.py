from rest_framework import serializers
from records.models import (
    Machine,
    Variable,
    Cause
)


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['name']
