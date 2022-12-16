from django.urls import path

from personas.views import nuevaPersona, detallePersona, editarPersona

urlpatterns = [
    path('nueva_persona', nuevaPersona),
    path('detalle_persona/<int:id>', detallePersona),
    path('editar_persona/<int:id>', editarPersona),
]