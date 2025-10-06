from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm

def lista_contactos(request):
    query = request.GET.get('q')
    if query:
        contactos = Contacto.objects.filter(nombre__icontains=query) | Contacto.objects.filter(correo__icontains=query)
    else:
        contactos = Contacto.objects.all()
    return render(request, 'inventario/lista_contactos.html', {'contactos': contactos, 'query': query})

def nuevo_contacto(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_contactos')
    return render(request, 'inventario/nuevo_contacto.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return redirect('lista_contactos')
    return render(request, 'inventario/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'inventario/eliminar_contacto.html', {'contacto': contacto})

def detalle_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    return render(request, 'inventario/detalle_contacto.html', {'contacto': contacto})
