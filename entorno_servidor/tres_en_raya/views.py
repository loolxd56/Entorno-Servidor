from django.shortcuts import render

def verificar_ganador(tablero):
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for a, b, c in lineas_ganadoras:
        if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a] 
            
    if '-' not in tablero:
        return 'Empate'
    return None


def tres_en_raya(request):
    # Contador de visitas (Tarea 1)
    request.session['visitas'] = request.session.get('visitas', 0) + 1

    # 1. Inicializar o reiniciar la sesión usando '-' para coincidir con verificar_ganador
    if 'tablero' not in request.session or 'reiniciar' in request.POST:
        request.session['tablero'] = ['-'] * 9 
        request.session['turno'] = 'X'
        request.session['terminado'] = False
        request.session['mensaje'] = 'Turno de X'

    if request.method == 'POST' and 'posicion' in request.POST:
        casilla = int(request.POST.get('posicion'))
        tablero = request.session['tablero']
        turno = request.session['turno']
        terminado = request.session['terminado']

        # Si la casilla tiene '-' y el juego no ha terminado
        if tablero[casilla] == '-' and not terminado:
            tablero[casilla] = turno
            
            resultado = verificar_ganador(tablero) 
            if resultado == 'Empate':
                request.session['mensaje'] = '¡Empate!'
                request.session['terminado'] = True
            elif resultado:
                request.session['mensaje'] = '¡Ha ganado ' + resultado + ' !'
                request.session['terminado'] = True
            else:
                nuevo_turno = 'O' if turno == 'X' else 'X'
                request.session['turno'] = nuevo_turno
                request.session['mensaje'] = 'Turno de' + nuevo_turno

            # Guardar cambios en la sesión
            request.session.modified = True 

    # 2. Enviar las variables exactas que espera tu HTML
    context = {
        'tablero': request.session['tablero'],
        'turno': request.session['turno'],
        'terminado': request.session['terminado'],
        'mensaje': request.session['mensaje'],
    }
    
    return render(request, 'tres_en_raya/tres_en_raya.html', context)