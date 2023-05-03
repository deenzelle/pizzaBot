#Pizza bot program

#3/5/23 p3 things
#Bugs - Phone number input allows letters
#name input allows numbers

#imports randomness
import random
#imports ability to import random numbers from the random name list
from random import randint

#list of random names
names = ["Bread", "Moana", "Mark", "Phoebe", "Sally", "Michael", "Chaewon", "Haewon", "Hanni", "Joaquin"]

# validates input to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")
            
# Creates the customer detail dictionary to have memory of user input
customer_details = {}

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
    print("*** Welcome to Dream Pizzas                                          ***")
    print("*** My name is",name, "                                                  ***")
    print("*** I will be here to help you order your delicious Dream Pizza      ***")
    print("****************************************************************************")

#Create menu for pickup or delivery
def order_type():
    print("Is your order being picked up at our store, or would you like it to be delivered?")
    print("For pickup enter 1")
    print("For delivery enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number: "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("You have selected to have your pizza picked up!")
                    pickup()
                    break

                elif delivery == 2:
                    print("You have selected to have your pizza delivered!")
                    break
            else:
                print("The number must be 1 or 2")

        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Grabbing the user's name and phone number for pickup information
# instructions for asking name
def pickup():
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question )
    # print (customer_details['name'])

    # instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question )
    # print (customer_details['phone'])
    print(customer_details)

#Create function so that user can choose number of pizzas required

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
    order_type()


main()
