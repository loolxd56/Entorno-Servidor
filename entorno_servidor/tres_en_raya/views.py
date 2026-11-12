from django.shortcuts import render

def verificar_ganador(tablero):
    # All combinations
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    # We check for identical symbols.
    for a, b, c in lineas_ganadoras:
        if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a] 
            #we check if there is a tie
    if '-' not in tablero:
        return 'Empate'
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
                # If no one has won yet, we pass the turn.
                turno = 'O' if turno == 'X' else 'X'
                mensaje = 'Turno de ' + turno

        else:
            # If an occupied square was selected, we keep the current turn's message.
            mensaje = 'Turno ' + turno

    else:
        # Initial state
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