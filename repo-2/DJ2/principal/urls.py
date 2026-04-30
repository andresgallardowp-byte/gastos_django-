from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('registrar/', views.registrar_gasto, name='registrar_gasto'),
    path('editar/<int:id>/', views.editar_gasto, name='editar_gasto'),
    path('eliminar/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),
]