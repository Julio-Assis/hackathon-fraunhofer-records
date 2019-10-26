from django.contrib import admin
from .models import (
    Machine,
    Variable,
    Cause,
    MachineRecord,
    VariableRecord,
    CauseRecord,
)

# Register your models here.
admin.site.register(Machine)
admin.site.register(Variable)
admin.site.register(Cause)


@admin.register(MachineRecord)
class MachineRecordAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(VariableRecord)
class VariableRecordAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CauseRecord)
class CauseRecordAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
