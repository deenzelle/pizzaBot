#component numero tres

#Bug - accepts blank input, allows letters to be inputted as phone *numbers*

print("Please enter the pickup information ")

# Customer name
valid = False
while not valid:
    name = input("Please enter your name ")
    if name != "":
        print(name)
        break

    else:
        print("Sorry this cannot be blank, please enter your name")

# Customer phone number
valid = False
while not valid:
    phone = input("Please enter your phone number ")
    if phone != "":
        print(phone)
        break
    else:
        print("Sorry this cannot be blank, please enter your phone number")
