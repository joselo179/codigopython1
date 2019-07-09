#Programa que hace loops

#Simple Loop
people = ['Andres', 'Alejandra', 'Benito', 'Jose','Kevin','Ramiro']

print('****Simple lopp****')
for person in people:
  print('Current Person: {0}'.format(person))

#Break
print('****Break loop****')
for person in people:
    if person == 'Benito':
        break
    print('Current Person: {0}'. format(person))

#Continue
print('****Continue loop****')
for person in people:
    if person == 'Benito':
       continue
    print('Current Person: {0}'.format(person))
    print('Esta orden tiene que estar indentada')

print('****Range loop****')
#range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print('Number:{0}'.format(i))

for i in range(0,len(people)):
    print('Number:{0}'.format(i))
    print('Orden extra para ver la importancia de indentacion')

#while loops: hasta que se cumpla una condicion

count = 0
while count <= 10:
    print('Count: {0}'.format(count))
    count+=1


