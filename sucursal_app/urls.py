from django.urls import path
from sucursal_app import views
urlpatterns = [
    path("inicio_Sucursal",views.inicio_Sucursal, name="inicio_Sucursal"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>",views.seleccionarSucursal,name="seleccionarSucursal"),
    path("editarSucursal/",views.editarSucursal,name="editarSucursal"),
    path("borrarSucursal/<id_sucursal>",views.borrarSucursal,name="borrarSucursal")
]
