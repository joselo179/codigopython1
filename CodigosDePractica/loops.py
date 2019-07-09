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



