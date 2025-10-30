
menu = {
    'pizza': 400,
    'burger': 89,
    'salad': 49,
    'coffee': 350,
    'pasta': 250,
    'sandwich': 199,
    'soda': 30,
    'dessert': 150,
    'noodles': 180
}

print("Welcome to my PYTHON Restaurant")
print("This is our Menu")

for key, value in menu.items():
    print(f"{key}: {value}")

order_total_cost = 0

order = []

while True:
    item = input("Enter the name of item you want to order = ")
    quant = int(input("Enter the quantity of item = "))

    if item in menu:
        order.append((item, quant))
        order_total_cost += menu[item] * quant
        print(f"Your item {item} has been added to order")

    another_order = input("Do you want to order more items? (yes/no) = ")
    if another_order == 'no':
        print("Your order summary is as follows:")
        print("-----------------------------------")
        print(order)
        print("-----------------------------------")
        print("Itemized Bill:")
        for ordered_item, quantity in order:
            item_cost = menu[ordered_item] * quantity
            print(f"{ordered_item} x {quantity} = {item_cost}")
        
        print(f"Total cost of your order is: {order_total_cost}")
    
        print("How do you want to pay? (cash/card) = ")
        payment_method = input()
        if payment_method == 'cash':
            print("You have chosen to pay by cash.")
        elif payment_method == 'card':
            print("You have chosen to pay by card.")
        else:
            print("Invalid payment method selected.")

        print("Payment successful!")
        print("Your order is successfully placed.")
        print("Thank you for visiting PYTHON Restaurant. Have a great day!")

        break