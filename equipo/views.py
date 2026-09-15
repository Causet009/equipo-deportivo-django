from django.shortcuts import render
from django.http import Http404


jugadores = [
    {
        'id': 1,
        'nombre': 'Cristiano Ronaldo',
        'posicion': 'Delantero',
        'numero': 7,
        'edad': 41,
        'nacionalidad': 'Portugal',
        'partidos_jugados': 40,
    },
    {
        'id': 2,
        'nombre': 'Lionel Messi',
        'posicion': 'Delantero',
        'numero': 10,
        'edad': 39,
        'nacionalidad': 'Argentina',
        'partidos_jugados': 35,
    },
    {
        'id': 3,
        'nombre': 'Kylian Mbappe',
        'posicion': 'Delantero',
        'numero': 9,
        'edad': 27,
        'nacionalidad': 'Francia',
        'partidos_jugados': 38,
    },
    {
        'id': 4,
        'nombre': 'Kevin De Bruyne',
        'posicion': 'Mediocampista',
        'numero': 17,
        'edad': 35,
        'nacionalidad': 'Belgica',
        'partidos_jugados': 32,
    },
    {
        'id': 5,
        'nombre': 'Virgil van Dijk',
        'posicion': 'Defensa',
        'numero': 4,
        'edad': 35,
        'nacionalidad': 'Paises Bajos',
        'partidos_jugados': 36,
    },
    {
        'id': 6,
        'nombre': 'Thibaut Courtois',
        'posicion': 'Arquero',
        'numero': 1,
        'edad': 34,
        'nacionalidad': 'Belgica',
        'partidos_jugados': 30,
    },
]


def inicio(request):
    contexto = {
        'jugadores': jugadores,
        'total': len(jugadores),
    }

    return render(request, 'equipo/inicio.html', contexto)


def detalle(request, id):
    jugador = None

    for elemento in jugadores:
        if elemento['id'] == id:
            jugador = elemento
            break

    if jugador is None:
        raise Http404('Jugador no encontrado')

    contexto = {
        'jugador': jugador,
    }

    return render(request, 'equipo/detalle.html', contexto)