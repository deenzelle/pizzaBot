#component numero seven
# list to store ordered pizzas
order_list = ['Margherita', 'Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
# list to store ordered pizzas prices
order_cost = [8.50, 8.50, 8.50, 13.50]



cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Botany'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details:")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone Number: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details:")
    count=0
    for item in order_list:
        print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count + 1

    print()
    print("Order Cost Details:")
    print(f"The total cost of the order is: ${total_cost:.2f}")

print_order()