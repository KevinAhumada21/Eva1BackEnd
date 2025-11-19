from django.contrib import admin
from .models import Contacto
import csv
from django.http import HttpResponse

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'correo')  
    list_filter = ('nombre',)
    list_per_page = 20

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
    
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="contactos.csv"'
        writer = csv.writer(response)
        writer.writerow(['Nombre', 'Teléfono', 'Correo', 'Dirección'])

        for contacto in queryset:
            writer.writerow([contacto.nombre, contacto.telefono, contacto.correo, contacto.direccion])

        return response

    export_as_csv.short_description = "Exportar seleccionados a CSV"

admin.site.register(Contacto, ContactoAdmin)