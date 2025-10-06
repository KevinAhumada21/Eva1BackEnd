from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('lista_contactos')),
    path('contactos/', include('inventario.urls')),
]
