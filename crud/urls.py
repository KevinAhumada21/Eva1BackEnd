from django.urls import path, include

urlpatterns = [
    path('contactos/', include('inventario.urls')),
]
