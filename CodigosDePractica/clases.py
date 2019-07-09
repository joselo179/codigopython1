#una clase es como un plano para crear objetos, un objeto tiene propiedades y metodos (funciones) asociadas a el, casi todo en python es un objeto(clase)

#create a class
class Usuario:
    #Constructor funcion que corre, cuando haces una instanciacion
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def saludos(self, num1=1):
        print(num1)
        return('Me llamo {0} y tengo {1}'.format(self.nombre,self.edad))

    def tengo_cumple(self):
        self.edad+=1

#init un objeto para el usuario
Joselo = Usuario('Joselo Vazquez','vazquez_lopez88@hotmail.com',30)
print(type(Joselo))
print(Joselo.nombre)
print(Joselo.saludos())
#extender la clase usuario
class Cliente(Usuario):

   def __init__(self, nombre, email, edad):
       self.nombre = nombre
       self.email = email
       self.edad = edad
       self.saldo = 0

   def establecer_saldo(self,saldo):
       self.saldo = saldo

   def saludos(self):
       return('Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre,self.edad,self.saldo))

#init un objeto del tipo usuario
Joselo = Usuario('Joselo Vazquez','vazquez_lopez88@hotmail,com',30)
print(type(Joselo))
print(Joselo.nombre)
print(Joselo.saludos())

#init un objeto del tipo cliente
Julieta = Cliente('Julieta Mtz','drpapeleria@hotmail.com',38)
print(type(Julieta))
print(Julieta.nombre)
Julieta.establecer_saldo(5e8)
print(Julieta.saludos())


