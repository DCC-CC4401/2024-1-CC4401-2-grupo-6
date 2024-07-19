#user: wcadmin
#mail: wcadmin@uchile.cl
#pass: wcadmin

from django.contrib import admin
from django.utils.html import format_html
from .models import Cleaning, User, Tarea, Bathroom, Comment
from django.utils.translation import gettext_lazy as _

admin.site.register(User)
admin.site.register(Tarea)

class BathroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'building', 'floor', 'latitude', 'longitude', 'publicar', 'image_tag']
    list_filter = ['publicar']
    actions = ['publicar_baños']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def publicar_baños(self, request, queryset):
        queryset.update(publicar=True)
        self.message_user(request, _('Los baños seleccionados han sido publicados.'))
    publicar_baños.short_description = _('Marcar seleccionados como publicados')

    # Ajustar el tamaño del campo de descripción
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget.attrs['style'] = 'width: 80%; height: 200px;'
        return formfield

admin.site.register(Bathroom, BathroomAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'bathroom', 'user', 'created_at']
    list_filter = ['bathroom', 'created_at']
    search_fields = ['bathroom__name', 'user__username', 'content']
    actions = ['borrar_comentarios_seleccionados']

    def borrar_comentarios_seleccionados(self, request, queryset):
        queryset.delete()
        self.message_user(request, _('Los comentarios seleccionados han sido eliminados.'))
    borrar_comentarios_seleccionados.short_description = _('Eliminar comentarios seleccionados')

admin.site.register(Comment, CommentAdmin)

class CleaningAdmin(admin.ModelAdmin):
    list_display=['id','bathroom', 'user', 'points']

admin.site.register(Cleaning, CleaningAdmin)
