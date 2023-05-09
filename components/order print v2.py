#component numero seven
# list to store ordered pizzas
order_list = ['Margherita', 'Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
# list to store ordered pizzas prices
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Flat Bush'}

#print("\n",cust_details['name'], "\n",cust_details['phone'], "\n",cust_details['house'], "\n",cust_details['street'], "\n",cust_details['suburb'],)

print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House Number: {} \nCustomer Street Name: {} \nCustomer Suburb: {}".format(cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb'],))

count=0
for item in order_list:
    print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count + 1