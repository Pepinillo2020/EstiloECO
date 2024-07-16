from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Producto, Categoria, Contacto
from django.contrib import messages
from .forms import ProductoForm, CustomUserCreationForm, ContactoForm
from django.views.generic import View
from django.contrib.auth import logout, login

def superuser_required(user):
    return user.is_superuser

def home(request):
    return render(request, 'home.html')

def horario(request):
    return render(request, 'horario.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def exit(request):
    logout(request)
    return redirect(home)

def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            messages.success(request, '¡Recibimos tu mensaje! Gracias por comunicarte.')
            return redirect('contacto')
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'nombre': request.user.get_full_name(),
                'email': request.user.email,
            }
        contacto_form = ContactoForm(initial=initial_data)
    
    return render(request, 'contacto.html', {'form': contacto_form})

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)

@user_passes_test(superuser_required)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('agregarProducto')  
    else:
        form = ProductoForm()
    
    return render(request, 'agregarProducto.html', {'form': form})

@user_passes_test(superuser_required)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    
    return render(request, 'eliminarProducto.html', {'producto': producto})

class ProductoDeleteView(View):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        return render(request, 'eliminarProducto.html', {'producto': producto})

    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return redirect('productos')

@user_passes_test(superuser_required)    
def editarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')  
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})

def insumos(request):
    categoria_insumos = Categoria.objects.get(nombre="insumos")
    productos = Producto.objects.filter(categoria=categoria_insumos)
    
    return render(request, 'insumos.html', {'productos': productos})

def manualidades(request):
    categoria_manualidades = Categoria.objects.get(nombre="manualidades")
    productos = Producto.objects.filter(categoria=categoria_manualidades)
    
    return render(request, 'manualidades.html', {'productos': productos})

def textiles(request):
    categoria_textiles = Categoria.objects.get(nombre="textiles")
    productos = Producto.objects.filter(categoria=categoria_textiles)
    
    return render(request, 'textiles.html', {'productos': productos})