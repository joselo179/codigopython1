#python tiene fdunciones para crear, leer, actualizar y eliminar archivos

#Abrir un archivo

miArchivo = open('miArchivo.txt','w')

#Obtener info de este archivo

print('Name: ',miArchivo.name)
print('Esta cerrado: ',miArchivo.closed)
print('Modo abierto: ',miArchivo.mode)

#Escribir algo al archivo 

miArchivo.write('Me encanta Pyhthon')
miArchivo.write('y Root')
miArchivo.close()

#Agregar al archivo

miArchivo = open('miArchivo.txt','a')
miArchivo.write('y tambien C++')
miArchivo.close()

#Leer un archivo
miArchivo = open('miArchivo.txt', 'r')
texto = miArchivo.read()
print(texto)
miArchivo.close()


