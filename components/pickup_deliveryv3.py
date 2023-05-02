# menu so that user can choose either pickup or delivery

# Bugs
# Need to make it so that it only accepts '1' or '2'

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
