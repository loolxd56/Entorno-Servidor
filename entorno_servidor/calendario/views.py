from django.shortcuts import render
from datetime import datetime

def calendario(request, fecha):
    try:
        # strptime intenta convertir el texto usando el formato Día-Mes-Año
        fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")
        
        # extraemos los datos
        mi_dia = fecha_obj.strftime("%d")
        mi_mes = fecha_obj.strftime("%m") 
        mi_ano = fecha_obj.strftime("%Y")
        mensaje = "Una fecha excelente"
        
        return render(request, 'calendario/fecha.html', {
            'dia': mi_dia, 
            'mes': mi_mes, 
            'año': mi_ano, 
            'mensaje': mensaje
        })
        
    except ValueError:
        # Si introduce 'hola' o '12/12/2020', saltará este error
        return render(request, 'calendario/error.html', {'fecha': fecha})