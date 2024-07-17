from django.urls import path
from . import views
from .views import ProductoDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.exit, name='exit'),
    path('productos/', views.productos, name='productos'),
    path('insumos/', views.insumos, name='insumos'),
    path('manualidades/', views.manualidades, name='manualidades'),
    path('textiles/', views.textiles, name='textiles'),
    path('agregarProducto/', views.agregar_producto, name='agregarProducto'),
    path('eliminar/<int:producto_id>/', ProductoDeleteView.as_view(), name='eliminarProducto'),
    path('editar/<int:producto_id>/', views.editarProducto, name='editarProducto'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('horario/', views.horario, name='horario'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('mensajes/eliminar/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('mensajes/<int:mensaje_id>/', views.mensaje_detalle, name='mensaje_detalle'),
    path('direccion/', views.direccion, name='direccion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)