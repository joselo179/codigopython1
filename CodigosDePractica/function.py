#funcion es un bloque de codigo que solo corre cuando se le llama. En python no usamos corchetes, usamos indentacion con tabs o espacios

#crear a function, esta no regresa nada solo imprime

def decirHola(nombre=''):
    print('Hola {0}'.format(nombre))

decirHola('Joselo')
decirHola()

#funcion que me regresa un valor
#funcion suma

def hacerSuma(num1, num2):
    total = num1+num2
    return float(total)

hacerSuma(2,3)
print(hacerSuma(2,3),type(hacerSuma(2,3)))

x = 2
y = 2
total = hacerSuma(x,y)
print(total, type(total),"**lo mismo pero mas cool**")



