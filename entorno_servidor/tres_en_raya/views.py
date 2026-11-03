from django.shortcuts import render

def verificar_ganador(tablero):
    # Todas las combinaciones
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    # Comprobamos si hay simbolos iguales
    for a, b, c in lineas_ganadoras:
        if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a] 
            #comprobamos si hay empate
    if '-' not in tablero:
        return 'Empate'
    #la partida continua
    return None


def tres_en_raya(request):
    if request.method == 'POST':
        tablero = list(request.POST.get("tablero"))
        posicion = int(request.POST.get("posicion"))
        turno = request.POST.get("turno")
        
        terminado = False
        
        if tablero[posicion] == '-':
            tablero[posicion] = turno
            

            resultado = verificar_ganador(tablero)
            
            if resultado:
                terminado = True
                if resultado == 'Empate':
                    mensaje = '¡Es un empate!'
                else:
                    mensaje = '¡Ha ganado ' + resultado + '!'
            else:
                # Si nadie ha ganado todavía, pasamos el turno
                turno = 'O' if turno == 'X' else 'X'
                mensaje = 'Turno de ' + turno

        else:
            # Si pulsó una casilla ocupada, mantenemos el mensaje del turno actual
            mensaje = 'Turno ' + turno

    else:
        # Estado inicial
        tablero = ['-','-','-','-','-','-','-','-','-']
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False
                
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }
    
    return render(request, 'tres_en_raya.html', contexto)