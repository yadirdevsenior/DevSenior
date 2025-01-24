import datetime
import re


def Validad_telefono(telefono):
    return bool(re.match(r'^\+?\d{7,15}$', telefono))

def validar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validar_hora(hora):
   return bool(re.match(r'^([01]?\d|2[0-3]):[0-5]\d$', hora))