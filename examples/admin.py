from django.contrib import admin

from .models import dep, ter, equipment, type_eq, bild, status, history

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'note' )

admin.site.register(type_eq)
admin.site.register(dep)
admin.site.register(ter)
admin.site.register(bild)
admin.site.register(status)
admin.site.register(history)

#admin.site.register(equipment)
admin.site.register(equipment, EquipmentAdmin)
