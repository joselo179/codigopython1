x = 10
y = 5

if x > y:
   print('{0} es mas grande que {1}'.format (x,y))
   print(str(x) + 'es mas grande que '+ str(y))
else:
   print('{0} es mas grande que {1}'.format(y,x))
   print(str(y) + 'es mas grande que '+ str(x))

if x > y:
   print('{0} es mas grande que {1}'.format(x,y))
elif x==y:
   print('{0} y {1} son iguales'.format (x,y))
else:
   print('{0} es mas grabde que {1}'.format(y,x))

#if anidados 
if x > 2:
  if x <= 10:
     print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

#and
if x > 2 and x <= 10:
   print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

#or
if x > 2 or x <= 10:
   print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

if not (x==y):
   print('{0} no es igual a {1}'.format(x,y))


numbers = [1,2,3,4,5]
z=5


  
