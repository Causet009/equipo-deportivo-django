from django.urls import path
from . import views

app_name = 'equipo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('jugador/<int:id>/', views.detalle, name='detalle'),
]