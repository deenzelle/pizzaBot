#component numero tres
# Customer details dictionary
customer_details = {}

#defines a not blank variable
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cannot be blank")

# Basic instructions for asking name
question = ("Please enter your name: ")
customer_details['name'] = not_blank(question )
print (customer_details['name'])

# Basic instructions for asking for user's phone number
question = ("Please enter your phone number: ")
customer_details['phone'] = not_blank(question )
print (customer_details['phone'])