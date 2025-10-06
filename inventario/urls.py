from django.urls import path
from .views import lista_contactos, nuevo_contacto, editar_contacto, eliminar_contacto, detalle_contacto

urlpatterns = [
    path('', lista_contactos, name='lista_contactos'),
    path('nuevo/', nuevo_contacto, name='nuevo_contacto'),
    path('editar/<int:id>/', editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>/', eliminar_contacto, name='eliminar_contacto'),
    path('detalle/<int:id>/', detalle_contacto, name='detalle_contacto'),
]
