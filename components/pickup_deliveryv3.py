# menu so that user can choose either pickup or delivery

# Bugs
# Need to make it so that it only accepts '1' or '2'

print("Is your order being picked up at our store, or would you like it to be delivered?")

print("For delivery enter 1")
print("For pickup enter 2")

low = 1
high = 2

while True:
    try:
        delivery = int(input())
        if delivery == "1":
            print("Delivery")
    
        elif delivery == "2":
            print("Pickup")
    
    except ValueError:
        print("That is not a valid number")