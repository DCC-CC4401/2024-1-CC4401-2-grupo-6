#user: wcadmin
#mail: wcadmin@uchile.cl
#pass: wcadmin

from django.contrib import admin
from .models import User, Tarea, Bathroom
from django.utils.translation import gettext_lazy as _

admin.site.register(User)
admin.site.register(Tarea)

class BathroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'building', 'floor', 'latitude', 'longitude', 'publicar']
    list_filter = ['publicar']
    actions = ['publicar_baños']

    def publicar_baños(self, request, queryset):
        queryset.update(publicar=True)
        self.message_user(request, _('Los baños seleccionados han sido publicados.'))
    publicar_baños.short_description = _('Marcar seleccionados como publicados')

admin.site.register(Bathroom, BathroomAdmin)

