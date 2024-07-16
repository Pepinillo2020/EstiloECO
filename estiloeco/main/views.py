from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Producto
from django.contrib import messages
from .forms import ProductoForm, CustomUserCreationForm
from django.views.generic import View
from django.contrib.auth import logout, login

def superuser_required(user):
    return user.is_superuser

def home(request):
    return render(request, 'home.html')

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