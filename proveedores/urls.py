# proveedores/surls.py
"""URLs de la app proveedoress — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'proveedoress'


def bienvenida_proveedoress(request):
    """Vista temporal de bienvenida para la app proveedoress."""
    return HttpResponse(
        "<h2>📦 Módulo proveedoress</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_proveedoress, name='inicio'),
]
