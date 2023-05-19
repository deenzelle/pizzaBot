#Pizza bot program

#3/5/23 p3 things
#Bugs - Phone number input allows letters
#name input allows numbers

#known bugs
# 18/5/23 - final printout is not printing customer details correctly

#imports randomness
import random
#imports ability to import random numbers from the random name list
from random import randint

import sys

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

# validates input to check if they are an integer      
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Enter a number between {low} and {high}")               
        except ValueError:
            print("That is not a valid number")
            print(f"Enter a number between {low} and {high}")            
            
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
    print("*** Welcome to Dream Pizzas                                              ***")
    print("*** My name is",name, "                                                  ***")
    print("*** I will be here to help you order your delicious Dream Pizza          ***")
    print("****************************************************************************")

#Create menu for pickup or delivery
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("Is your order being picked up at our store, or would you like it to be delivered?")
    print("For pickup enter 1")
    print("For delivery enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print("You have selected to have your pizza picked up!")
        pickup_info()
        del_pick = "pickup"
    else:
        print("You have selected to have your pizza delivered!")
        order_list.append("Delivery Charge")
        order_cost.append(5)
        delivery_info()
        del_pick = "delivery"
    return del_pick


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
    LOW = 1
    HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("How many pizzas do you want to order?")
    num_pizzas = val_int(LOW, HIGH, question)

    # Choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0:
            print("Please choose your pizzas by entering the number on the menu: ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH}: ")
            pizza_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            num_pizzas = num_pizzas-1
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))

#Print order out - including if order is delivery or pick up and the names and price of each pizza - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details:")
    if del_pick == "pickup":
        print("Your order is for Pickup")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery ($5.00 delivery charge applies)")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details:")
    count=0
    for item in order_list:
        print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count + 1

    print()
    print("Order Cost Details:")
    print(f"The total cost of the order is: ${total_cost:.2f}")


#Create cancel order function
def confirm_cancel():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("Please confirm your order")
    print("To confirm your order, enter 1")
    print("To cancel your order, enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("Your order has been confirmed!")
        print("Your pizza will be with you shortly")
        new_exit()

    elif confirm == 2:
        print("Your order has been cancelled")
        print("You can restart your order or exit the BOT")
        new_exit()

       

#Create option for new order or to exit
def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("Do you want to start another order or exit the bot?")
    print("To start another order, enter 1")
    print("To exit the BOT, enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("New Order")
        order_list.clear()
        order_cost = [].clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost = [].clear()
        customer_details.clear()
        sys.exit()

#Main function
def main():
    '''
    Purpose: To run all functions
    Parameter: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_pizza()
    print_order(del_pick)
    confirm_cancel()


main()