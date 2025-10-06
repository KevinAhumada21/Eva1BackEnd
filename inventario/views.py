from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm

def nuevo_contacto(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_contactos')
    return render(request, 'inventario/nuevo_contacto.html', {'form': form})
