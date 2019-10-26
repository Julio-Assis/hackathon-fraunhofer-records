from django.db import models


# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=100)


class MachineRecord(models.Model):
    machine = models.ForeignKey(
        Machine,
        related_name='records',
        on_delete=models.CASCADE
    )
    status = models.BooleanField()
    stop_timestamp = models.DateTimeField()
    # duration of the stop in seconds
    duration = models.IntegerField()
    operator_timestamp = models.DateTimeField(auto_now_add=True)


class Cause(models.Model):
    name = models.CharField(max_length=100)


class CauseRecord(models.Model):
    cause = models.ForeignKey(
        Cause,
        related_name='records',
        on_delete=models.CASCADE
    )
    extras = models.CharField(max_length=200)
    machine_record = models.ForeignKey(
        MachineRecord,
        related_name='causes',
        on_delete=models.CASCADE
    )


class Variable(models.Model):
    unit = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class VariableRecord(models.Model):
    variable = models.ForeignKey(
        Variable,
        on_delete=models.CASCADE,
        related_name='records'
    )

    machine_record = models.ForeignKey(
        MachineRecord,
        on_delete=models.CASCADE,
        related_name='variable_records'
    )

    value = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
