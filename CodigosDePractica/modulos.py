#Un modulo es un archivo que contiene funciones para incluir en tu aplicacion
#hay modulos basicos en el nucleo de python, tambien modulos que se pueden
#instalar usando el administrador "pip" y finalmente modulos personalizados

#Importar un modulo de python por default
#forma 1

import datetime
hoy = datetime.date.today()
print(hoy)

#forma 2

from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time.time()
print(estampatemporal)

#Administrador para poder instalar modulos externos


# modulo personalizado
import validador
from validador import validate_email

email = 'pruebaprueba.com'
if validate_email(email):
   print('El correo esta bien escrito')
else:
   print('El correo esta mal escrito')


