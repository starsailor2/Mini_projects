from colorama import Fore, Back, Style, init
import tabulate # for interactive table display
import os
import csv # for reading and writing csv file
import uuid # for uniqueID assign to each product

# Automatically resets colors after each print (no need to manually reset)
init(autoreset=True)

USER_FILE = os.path.join(os.path.dirname(__file__), 'inventory.csv')

def initialize_csv(USER_FILE=USER_FILE):
    if not os.path.exists(USER_FILE) or os.stat(USER_FILE).st_size == 0: # if the filename doesnot exist
        with open(USER_FILE, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["prod_id","prod_name", "prod_price", "prod_quan"])
        print(f"{Fore.GREEN} New CSV file created name: {USER_FILE}")
    else:
        print(f"{Fore.CYAN} CSV file {USER_FILE} already exist")

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
            print(f"\n{Fore.RED} Product {prod_name} already exists in inventory!")
            print(f"{Fore.YELLOW}   ID: {prod['prod_id']} | Price: Rs.{prod['prod_price']} | Quantity: {prod['prod_quan']}")
            
            choice = input(f"\n{Fore.CYAN}if you want to update the product features(name, price) instead? press np and if update only quantity press q: ").lower()
            if choice == 'np':
                print(f"\n{Fore.CYAN}Updating product: {prod['prod_name']}")
                prod["prod_name"] = input("Enter new name (or press Enter to keep): ") or prod["prod_name"]
                prod["prod_price"] = input("Enter new price (or press Enter to keep): ") or prod["prod_price"]
                prod["prod_quan"] = input("Enter new quantity (or press Enter to keep): ") or prod["prod_quan"]
                save_prod(products)
                print(f"{Fore.GREEN} Product updated successfully!")
            
            elif choice == "q":
                additional_qty = input("Enter quantity to add: ")
                prod["prod_quan"] = str(int(prod["prod_quan"]) + int(additional_qty))
                save_prod(products)
                print(f"{Fore.GREEN} Updated quantity for '{prod_name}' to {prod['prod_quan']}")

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

    print(f"{Fore.GREEN} {prod_name} is added with the Id: {prod_id} in the inventory")

# show ALL products in the inventory
def view_prod():
    products = load_prod()

    if not products:
        print(f"{Fore.YELLOW}  No products in the inventory")
        return
    
    headers = ["ID", "Name", "Price", "Quantity"]
    rows = []

    for p in products:
        rows.append([p["prod_id"], p["prod_name"], p["prod_price"], p["prod_quan"]])
    
    print(f"{Fore.CYAN}{tabulate.tabulate(rows, headers=headers, tablefmt='grid')}")
        
# search a product with name and get details
def search_prod():
    products = load_prod()

    name = input("Please Enter Product Name: ")

    for prod in products:
        if prod["prod_name"].lower() == name.lower():
            print(f"\n{Fore.GREEN} ----- Product Found -----")
            print(f"{Fore.CYAN}ID: {prod['prod_id']}")
            print(f"{Fore.CYAN}Name: {prod['prod_name']}")
            print(f"{Fore.CYAN}Price: Rs.{prod['prod_price']}")
            print(f"{Fore.CYAN}Quantity: {prod['prod_quan']}")
            break

    else:
        print(f"{Fore.RED} Product '{name}' not found in inventory")

# update the features for the product for a selected ID (name/price/quantity)
def update_prod():
    products = load_prod()
    
    if not products:
        print(f"{Fore.YELLOW}  No products in inventory")
        return
    
    prod_input = input("Enter Product ID/Name to update: ")
    
    for prod in products:
        if prod["prod_id"] == prod_input or prod["prod_name"].lower() == prod_input.lower():
            print(f"\n{Fore.YELLOW}Current details: {prod['prod_name']} - Rs.{prod['prod_price']} - Qty: {prod['prod_quan']}")
            
            prod["prod_name"] = input("Enter new name (or press Enter to keep): ") or prod["prod_name"]
            prod["prod_price"] = input("Enter new price (or press Enter to keep): ") or prod["prod_price"]
            prod["prod_quan"] = input("Enter new quantity (or press Enter to keep): ") or prod["prod_quan"]
            
            save_prod(products)  # Save updated list back to CSV
            print(f"{Fore.GREEN} Product updated successfully!")
            return
    
    print(f"{Fore.RED} Product ID '{prod_input}' not found")

def delete_prod():
    products = load_prod()

    # if the inventory is empty
    if not products:
        print(f"{Fore.YELLOW}  No products in the inventory")
        return
    
    # its sensitive so we are asking for ID not Name
    prod_input = input("Enter the Product ID/Name to delete: ")
    
    for i, prod in enumerate(products):
        if prod["prod_id"] == prod_input or prod["prod_name"].lower() == prod_input.lower():
            print(f"\n{Fore.YELLOW}--- Details of the Product which to be deleted ---")
            print(f"{Fore.CYAN}ID: {prod['prod_id']}")
            print(f"{Fore.CYAN}Name: {prod['prod_name']}")
            print(f"{Fore.CYAN}Price: Rs.{prod['prod_price']}")
            print(f"{Fore.CYAN}Quantity: {prod['prod_quan']}")

            # ask for confirmation
            confirm = input(f"\n{Fore.RED}Are you really sure you want to delete this product? (if yes then press y otherwise n): ")

            if confirm == "y":
                products.pop(i) # remove product from the list
                save_prod(products)
                print(f"{Fore.GREEN} Product name {prod['prod_name']} deleted successfully")
            
            else:
                print(f"{Fore.YELLOW} Deletion Cancelled")

            return

    # the inventory is not empty and
    # incase the prod_id is not belong to any product

    print(f"{Fore.RED} Product {prod_input} not found")

def generate_report():
    products = load_prod()
    
    if not products:
        print(f"\n{Fore.YELLOW}  No products in inventory to generate report")
        return
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}" + "="*50)
    print(f"{Fore.CYAN}{Style.BRIGHT}         INVENTORY REPORT")
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "="*50)
    
    # Basic Statistics
    total_products = len(products)
    total_value = 0
    total_quantity = 0
    
    for prod in products:
        price = float(prod["prod_price"])
        quantity = int(prod["prod_quan"])
        total_value += price * quantity
        total_quantity += quantity
    
    print(f"\n{Fore.GREEN} Total Products: {total_products}")
    print(f"{Fore.GREEN} Total Inventory Value: Rs.{total_value:.2f}")
    print(f"{Fore.GREEN} Total Quantity: {total_quantity} units")
    
    # Most Expensive Product
    most_expensive = max(products, key=lambda p: float(p["prod_price"]))
    print(f"\n{Fore.MAGENTA} Most Expensive Product: {most_expensive['prod_name']} (Rs.{most_expensive['prod_price']})")
    
    # Least Expensive Product
    least_expensive = min(products, key=lambda p: float(p["prod_price"]))
    print(f"{Fore.MAGENTA} Least Expensive Product: {least_expensive['prod_name']} (Rs.{least_expensive['prod_price']})")
    
    # Highest Stock
    highest_stock = max(products, key=lambda p: int(p["prod_quan"]))
    print(f"\n{Fore.BLUE} Highest Stock: {highest_stock['prod_name']} ({highest_stock['prod_quan']} units)")
    
    # Lowest Stock
    lowest_stock = min(products, key=lambda p: int(p["prod_quan"]))
    print(f"{Fore.BLUE} Lowest Stock: {lowest_stock['prod_name']} ({lowest_stock['prod_quan']} units)")
    
    # Low Stock Alert (quantity < 5)
    low_stock_products = [p for p in products if int(p["prod_quan"]) < 5]
    
    if low_stock_products:
        print(f"\n{Fore.RED}  LOW STOCK ALERT ({len(low_stock_products)} products):")
        for prod in low_stock_products:
            print(f"{Fore.RED}   - {prod['prod_name']}: {prod['prod_quan']} units remaining")
    else:
        print(f"\n{Fore.GREEN} No low stock items")
    
    print(f"\n{Fore.CYAN}" + "="*50)
    
    # Option to export report
    export = input(f"\n{Fore.CYAN}Do you want to export this report to a file? (y/n): ").lower()
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
    
    print(f"\n{Fore.GREEN}✓ Report exported to: {filename}")


def menu():

    initialize_csv()

    while True:

        print(f'''{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════╗
║    INVENTORY MANAGEMENT SYSTEM       ║
╚══════════════════════════════════════╝
{Style.RESET_ALL}

{Fore.GREEN}  1.  View all products
{Fore.GREEN}  2.  Add new product
{Fore.GREEN}  3.  Search product
{Fore.GREEN}  4.  Update product
{Fore.GREEN}  5.  Delete product
{Fore.GREEN}  6.  Generate report
{Fore.RED}  7.  Exit
              ''')

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Viewing All Products ---{Style.RESET_ALL}")
                view_prod()
            case "2":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Adding New Product ---{Style.RESET_ALL}")
                add_prod()
            case "3":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Searching Product ---{Style.RESET_ALL}")
                search_prod()
            case "4":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Updating Product ---{Style.RESET_ALL}")
                update_prod()
            case "5":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Deleting Product ---{Style.RESET_ALL}")
                delete_prod()
            case "6":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- Generating Report ---{Style.RESET_ALL}")
                generate_report()
            case "7":
                print(f"\n{Fore.GREEN} Thank you for using Inventory Management System!")
                print(f"{Fore.GREEN}Exiting...!!!")
                break
            case _:
                print(f"{Fore.RED} You entered an invalid number, please try again")

        # Add pause after each operation
        input(f"\n{Fore.YELLOW}Press Enter to continue...")            

if __name__ == "__main__":
    menu()