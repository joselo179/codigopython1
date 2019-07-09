

#Create a list, 1st way to do it
numbers = [1,2,3,4,5]
fruits = ["Apple", "Oranges","Grapes","Pears"]

#Create a list, use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, fruits)

#Get a value of a list
print(fruits[1])

#Get length

print(len(fruits))

#Append to the list

fruits.append("Mangos")

#Removed to the list

fruits.remove("Grapes")
print(fruits)

#Insert to position
fruits.insert(2,"Strawberries")
print(fruits)

#Remove from a position, with pop
fruits.pop(2)
print(fruits)

#Reverse the list
fruits.reverse()
print(fruits)

#sort alphabetically
fruits.sort()
print(fruits)

