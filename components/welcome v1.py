import random
#imports ability to import random numbers from the random name list
from random import randint

#list of random names
names = ["Bread", "Moana", "Mark", "Phoebe", "Sally", "Michael", "Chaewon", "Haewon", "Hanni", "Joaquin"]

num = randint(0,9)

name = (names[num])

print("*** Welcome to BinkyBong Pizzas ***")
print("*** My name is",name, "***")
print("*** I will be here to help you order your delicious BinkyBong Pizza")

