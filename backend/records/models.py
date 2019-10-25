from django.db import models


# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=100)


class MachineRecord(models.Model):
    machine = models.ForeignKey(Machine, related_name='records')
    status = models.BooleanField()
    stop_timestamp = models.DateTimeField()
    # duration of the stop in seconds
    duration = models.IntegerField() 
    operator_timestamp = models.DateTimeField()


class Cause(models.Model):
    name = models.CharField(max_length=100)


class CauseRecord(models.Model):
    cause = models.ForeignKey(Cause, related_name='records')
    extras = models.CharField(max_length=200)
    machine_record = models.ForeignKey(MachineRecord, related_name='causes')


class Variable(models.Model):
    unit = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
