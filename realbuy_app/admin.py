from django.contrib import admin
from .models import Property,ContactUs,Profile
from .forms import TypeAdminForm,FloorAdminForm


class TypeAdmin(admin.ModelAdmin):
    form = TypeAdminForm
    
class FloorAdmin(admin.ModelAdmin):
    form = FloorAdminForm
    
class PropertyExtendAdmin(TypeAdmin, FloorAdmin):
    pass
    
admin.site.register(Property, PropertyExtendAdmin)
admin.site.register(ContactUs)
admin.site.register(Profile)

