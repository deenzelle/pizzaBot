#Pizza bot program
import random
#imports ability to import random numbers from the random name list
from random import randint

#list of random names
names = ["Bread", "Moana", "Mark", "Phoebe", "Sally", "Michael", "Chaewon", "Haewon", "Hanni", "Joaquin"]

#Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameter: None
    Returns: None
    '''

    num = randint(0,9)
    name = (names[num])
    print("****************************************************************************")
    print("*** Welcome to BinkyBong Pizzas                                          ***")
    print("*** My name is",name, "                                                  ***")
    print("*** I will be here to help you order your delicious BinkyBong Pizza      ***")
    print("****************************************************************************")

#Create menu for pickup or delivery
def pickup():
    print("Is your order being picked up at our store, or would you like it to be delivered?")
    print("For pickup enter 1")
    print("For delivery enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    break

                elif delivery == 2:
                    print("Delivery")
                    break
            else:
                print("The number must be 1 or 2")

        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")

#Create pickup function

#Create function so that user can coose number of pizzas required

#Create pizza menu

#Create pizza ordering function

#Create print function to display pizzas ordered, cost and delivery options if required

#Create cancel order function

#Create option for new order or to exit

#Main function
def main():
    '''
    Purpose: To run all functions
    Parameter: None
    Returns: None
    '''
    welcome()
    pickup()


main()
