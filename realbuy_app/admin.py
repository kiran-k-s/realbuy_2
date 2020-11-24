from django.contrib import admin
from .models import Property
from .forms import TypeAdminForm,FloorAdminForm


class TypeAdmin(admin.ModelAdmin):
    form = TypeAdminForm
    
class FloorAdmin(admin.ModelAdmin):
    form = FloorAdminForm
    
admin.site.register(Property, TypeAdmin, FloorAdmin)