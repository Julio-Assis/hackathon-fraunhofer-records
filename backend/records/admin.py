from django.contrib import admin
from .models import (
    Machine,
    Variable,
    Cause
)


# Register your models here.
admin.site.register(Machine)
admin.site.register(Variable)
admin.site.register(Cause)