import colorama
import tabulate # for interactive table display
import os
import csv # for reading and writing csv file
import uuid # for uniqueID assign to each product

USER_FILE =  os.path.join(os.path.dirname(__file__), 'inventory.csv')

def initialize_csv(USER_FILE=USER_FILE):
    if not os.path.exists(USER_FILE) or os.stat(USER_FILE).st_size == 0: # if the filename doesnot exist
        with open(USER_FILE, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["prod_id","prod_name", "prod_price", "prod_quan"])
        print(f"New CSV file created name: {USER_FILE}")
    else:
        print(f"CSV file {USER_FILE} already exist")

def generate_prod_id():
    prod_id = str(uuid.uuid4())[:8]
    return prod_id

# load the products from CSV file to the list of dictioanaries
def load_prod():
    products = []

    if not os.path.exists(USER_FILE):
        return products
    
    with open(USER_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)

    return products

def save_prod(products):
        with open(USER_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["prod_id", "prod_name", "prod_price", "prod_quan"])
            writer.writeheader()  # Write the header row
            writer.writerows(products)  # Write all products at once

# add new product / update if the product already there 
def add_prod():

    prod_name = input("Enter your product name : ")

    # check if product already exists or not
    products = load_prod()
    for prod in products:
        if prod["prod_name"].lower() == prod_name.lower():
            print(f"\n Product {prod_name} already exists in inventory!")
            print(f"   ID: {prod['prod_id']} | Price: Rs.{prod['prod_price']} | Quantity: {prod['prod_quan']}")
            
            choice = input("\nif you want to update the product features(name, price) instead? press np and if update only quantity press q: ").lower()
            if choice == 'np':
                print(f"\nUpdating product: {prod['prod_name']}")
                prod["prod_name"] = input("Enter new name (or press Enter to keep): ") or prod["prod_name"]
                prod["prod_price"] = input("Enter new price (or press Enter to keep): ") or prod["prod_price"]
                prod["prod_quan"] = input("Enter new quantity (or press Enter to keep): ") or prod["prod_quan"]
                save_prod(products)
                print("✓ Product updated successfully!")
            
            elif choice == "q":
                additional_qty = input("Enter quantity to add: ")
                prod["prod_quan"] = str(int(prod["prod_quan"]) + int(additional_qty))
                save_prod(products)
                print(f" Updated quantity for '{prod_name}' to {prod['prod_quan']}")

            return
                
    # if not exist then
    # Enter the details of the product
    prod_id = generate_prod_id()
    prod_price = input("Enter the price: ")
    prod_quan = input("Please enter the quantity as well: ")

    # create a dictionary form
    new_product = {
        "prod_id": prod_id,
        "prod_name": prod_name,
        "prod_price": prod_price,
        "prod_quan": prod_quan
    }
    # Append directly to CSV file
    with open(USER_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["prod_id", "prod_name", "prod_price", "prod_quan"])
        writer.writerow(new_product)

    print(f"{prod_name} is added with the Id: {prod_id} in the inventory")

# show ALL products in the inventory
def view_prod():
    products = load_prod()

    if not products:
        print("No products in the inventory")
        return
    
    headers = ["ID", "Name", "Price", "Quantity"]
    rows = []

    for p in products:
        rows.append([p["prod_id"], p["prod_name"], p["prod_price"], p["prod_quan"]])
    
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        
# search a product with name and get details
def search_prod():
    products = load_prod()

    name = input("Please Enter Product Name: ")

    for prod in products:
        if prod["prod_name"].lower() == name.lower():
            print("\n ----- Product Found -----")
            print(f"ID: {prod['prod_id']}")
            print(f"Name: {prod['prod_name']}")
            print(f"Price: {prod['prod_price']}")
            print(f"Quantity: {prod['prod_quan']}")
            break

    else:
        print(f"Product '{name} not found in inventory")

# update the features for the product for a selected ID (name/price/quantity)
def update_prod():
    products = load_prod()
    
    if not products:
        print("No products in inventory")
        return
    
    prod_input = input("Enter Product ID/Name to update: ")
    
    for prod in products:
        if prod["prod_id"] == prod_input or prod["prod_name"].lower() == prod_input.lower():
            print(f"\nCurrent details: {prod['prod_name']} - Rs.{prod['prod_price']} - Qty: {prod['prod_quan']}")
            
            prod["prod_name"] = input("Enter new name (or press Enter to keep): ") or prod["prod_name"]
            prod["prod_price"] = input("Enter new price (or press Enter to keep): ") or prod["prod_price"]
            prod["prod_quan"] = input("Enter new quantity (or press Enter to keep): ") or prod["prod_quan"]
            
            save_prod(products)  # Save updated list back to CSV
            print("Product updated successfully!")
            return
    
    print(f"Product ID '{prod_input}' not found")

def delete_prod():
    products = load_prod()

    # if the inventory is empty
    if not products:
        print("No products in the inventory")
        return
    
    # its sensitive so we are asking for ID not Name
    prod_input = input("Enter the Product ID/Name to delete: ")
    
    for i, prod in enumerate(products):
        if prod["prod_id"] == prod_input or prod["prod_name"] == prod_input:
            print(f"\n--- Details of the Product which to be deleted ---")
            print(f"ID: {prod['prod_id']}")
            print(f"Name: {prod['prod_name']}")
            print(f"Price: Rs.{prod['prod_price']}")
            print(f"Quantity: {prod['prod_quan']}")

            # ask for confirmation
            confirm = input("\nAre you really sure you want to delete this product? (if yes then press y otherwise n): ")

            if confirm == "y":
                products.pop(i) # remove product from the list
                save_prod(products)
                print(f" Product name {prod['prod_name']} deleted successfully")
            
            else:
                print("Deletion Cancelled")

            return

    # the inventory is not empty and
    # incase the prod_id is not belong to any product

    print(f" Product {prod} not found")

def generate_report():
    products = load_prod()
    
    if not products:
        print("\nNo products in inventory to generate report")
        return
    
    print("\n" + "="*50)
    print("         INVENTORY REPORT")
    print("="*50)
    
    # Basic Statistics
    total_products = len(products)
    total_value = 0
    total_quantity = 0
    
    for prod in products:
        price = float(prod["prod_price"])
        quantity = int(prod["prod_quan"])
        total_value += price * quantity
        total_quantity += quantity
    
    print(f"\n Total Products: {total_products}")
    print(f" Total Inventory Value: Rs.{total_value:.2f}")
    print(f" Total Quantity: {total_quantity} units")
    
    # Most Expensive Product
    most_expensive = max(products, key=lambda p: float(p["prod_price"]))
    print(f"\n Most Expensive Product: {most_expensive['prod_name']} (Rs.{most_expensive['prod_price']})")
    
    # Least Expensive Product
    least_expensive = min(products, key=lambda p: float(p["prod_price"]))
    print(f"\n Least Expensive Product: {least_expensive['prod_name']} (Rs.{least_expensive['prod_price']})")
    
    # Highest Stock
    highest_stock = max(products, key=lambda p: int(p["prod_quan"]))
    print(f"\n Highest Stock: {highest_stock['prod_name']} ({highest_stock['prod_quan']} units)")
    
    # Lowest Stock
    lowest_stock = min(products, key=lambda p: int(p["prod_quan"]))
    print(f"\n  Lowest Stock: {lowest_stock['prod_name']} ({lowest_stock['prod_quan']} units)")
    
    # Low Stock Alert (quantity < 5)
    low_stock_products = [p for p in products if int(p["prod_quan"]) < 5]
    
    if low_stock_products:
        print(f"\n LOW STOCK ALERT ({len(low_stock_products)} products):")
        for prod in low_stock_products:
            print(f"   - {prod['prod_name']}: {prod['prod_quan']} units remaining")
    else:
        print("\n No low stock items")
    
    print("\n" + "="*50)
    
    # Option to export report
    export = input("\nDo you want to export this report to a file? (y/n): ").lower()
    if export == 'y':
        export_report(products, total_products, total_value, total_quantity, low_stock_products)


def export_report(products, total_products, total_value, total_quantity, low_stock_products):
    """Export report to a text file"""
    filename = f"inventory_report_{uuid.uuid4().hex[:8]}.txt"
    
    with open(filename, 'w') as file:
        file.write("="*50 + "\n")
        file.write("         INVENTORY REPORT\n")
        file.write("="*50 + "\n\n")
        
        file.write(f"Total Products: {total_products}\n")
        file.write(f"Total Inventory Value: Rs.{total_value:.2f}\n")
        file.write(f"Total Quantity: {total_quantity} units\n")
        
        file.write("="*50 + "\n")
        file.write("ALL PRODUCTS:\n")
        file.write("="*50 + "\n")
        
        for prod in products:
            file.write(f"\nID: {prod['prod_id']}\n")
            file.write(f"Name: {prod['prod_name']}\n")
            file.write(f"Price: Rs.{prod['prod_price']}\n")
            file.write(f"Quantity: {prod['prod_quan']}\n")
            file.write("-" * 30 + "\n")
        
        if low_stock_products:
            file.write("\n" + "="*50 + "\n")
            file.write("LOW STOCK ALERT:\n")
            file.write("="*50 + "\n")
            for prod in low_stock_products:
                file.write(f"- {prod['prod_name']}: {prod['prod_quan']} units\n")
    
    print(f"\n✓ Report exported to: {filename}")


def menu():

    initialize_csv()

    while True:

        print('''
                Welcome to our inventory Management System
              ===============================================
                        1. view all products
                        2. add the product
                        3. search the product
                        4. update the product
                        5. delete the product
                        6. Generate the report
                        7. Exit
              ''')

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n--- Viewing All Products ---")
                view_prod()
            case "2":
                print("\n--- Adding New Product ---")
                add_prod()
            case "3":
                print("\n--- Searching Product ---")
                search_prod()
            case "4":
                print("\n--- Updating Product ---")
                update_prod()
            case "5":
                print("\n--- Deleting Product ---")
                delete_prod()
            case "6":
                print("\n--- Generating Report ---")
                generate_report()
            case "7":
                print("\nThank you for using Inventory Management System!")
                print("Exiting...!!!")
                break
            case _:
                print("You entered an invalid number, please try again")

        # Add pause after each operation
        input("\nPress Enter to continue...")
        print("\n" * 2)  # Clear screen effect               

if __name__ == "__main__":
    menu()