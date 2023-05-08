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

#list of pizzas
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie',
               'Vegan', 'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

#list of pizza prices (in order)
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# list to store ordered pizzas
order_list = []
# list to store ordered pizzas prices
order_cost = []

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

#Create menu for pickup
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
                    pickup_info()
                    break

                elif delivery == 2:
                    print("You have selected to have your pizza delivered!")
                    delivery_info()
                    break
            else:
                print("The number must be 1 or 2")

        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Pickup information - name and number
def pickup_info():
    # instructions for asking name
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question )
    # print (customer_details['name'])

    # instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question )
    # print (customer_details['phone'])
    print(customer_details)


# Delivery information - Name, Phone number, Address
def delivery_info():
    # instructions for asking for user's name
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    # instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])

    # instructions for asking for user's house number
    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question )
    print (customer_details['house'])

    # instructions for asking for user's street name
    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question )
    print (customer_details['street'])

    # instructions for asking for user's suburb
    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question )
    print (customer_details['suburb'])

#Create pizza menu
def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count]))


#Create function so that user can choose number of pizzas required
#Create pizza ordering function
def order_pizza():
    # ask for the total amount of pizzas for order
    num_pizzas = 0

    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order?: "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5 pizzas")
        except ValueError:
            print("That is not a valid number")
            print("Please choose a number between 1 and 5")

    print(num_pizzas)

    # Choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please choose your pizzas by entering the number on the menu: "))
                    if pizza_ordered >= 1 and pizza_ordered <= 12:
                        break
                    else:
                        print("Your pizza order must be between 1 and 12 pizzas")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")

            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            num_pizzas = num_pizzas-1
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))

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
    menu()
    order_pizza()


main()
