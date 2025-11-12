# 📦 Inventory Management System

A comprehensive command-line inventory management system built with Python that helps you manage product inventory, track stock levels, and generate detailed reports.


![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

## ✨ Features

### Core Functionality
- **📋 View All Products** - Display complete inventory in a formatted table
- **➕ Add New Product** - Add products with automatic ID generation
- **🔍 Search Product** - Search by product name
- **✏️ Update Product** - Modify product details (name, price, quantity)
- **🗑️ Delete Product** - Remove products with confirmation
- **📊 Generate Report** - Comprehensive inventory analytics and insights

### Smart Features
- **Duplicate Detection** - Prevents adding duplicate products
- **Low Stock Alerts** - Warns when inventory falls below 5 units
- **Automatic CSV Management** - Creates and maintains inventory.csv automatically
- **Export Reports** - Save detailed reports as text files
- **Unique Product IDs** - UUID-based identification system

### Report Analytics
- Total Products Count
- Total Inventory Value
- Most/Least Expensive Products
- Highest/Lowest Stock Levels
- Low Stock Warnings

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Required Libraries

```bash
pip install colorama tabulate
```

## 📁 Project Structure

```
Inventory Manager(CSV)/
│
├── main.py                    # Main application (no colors)
├── main(color).py             # Colorful version with colorama
├── inventory.csv              # Auto-generated inventory database
├── transactions.log           # Transaction history (future feature)
└── README.md                  # This file
```

## 💻 Usage

### Running the Application

**Standard Version:**
```bash
python main.py
```

**Colorful Version:**
```bash
python main(color).py
```

### Menu Options

```
╔════════════════════════════════════════════╗
║    INVENTORY MANAGEMENT SYSTEM             ║
╚════════════════════════════════════════════╝

  1.  View all products
  2.  Add new product
  3.  Search product
  4.  Update product
  5.  Delete product
  6.  Generate report
  7.  Exit
```

## 📖 Detailed Features

### 1. View All Products
Displays all products in a formatted table with:
- Product ID
- Product Name
- Price
- Quantity

```
+----------+-------------+-------+----------+
| ID       | Name        | Price | Quantity |
+----------+-------------+-------+----------+
| a1b2c3d4 | Laptop      | 999   | 10       |
| e5f6g7h8 | Mouse       | 25    | 50       |
+----------+-------------+-------+----------+
```

### 2. Add New Product
- Automatically generates unique 8-character ID
- Checks for duplicate product names
- If duplicate exists, offers to:
  - Update product features (name, price, quantity)
  - Only update quantity (add stock)

### 3. Search Product
- Case-insensitive name search
- Displays complete product details
- Shows "Product not found" message if not exists

### 4. Update Product
- Search by Product ID
- Update name, price, or quantity
- Press Enter to keep existing values
- Saves changes to CSV immediately

### 5. Delete Product
- Search by Product ID or Name
- Shows product details before deletion
- Requires confirmation (y/n)
- Prevents accidental deletions

### 6. Generate Report
Provides comprehensive analytics:

```
==================================================
                  INVENTORY REPORT
==================================================

📊 Total Products: 25
💰 Total Inventory Value: $15,450.00
📦 Total Quantity: 500 units

💎 Most Expensive Product: Gaming Laptop ($1,299)
💵 Least Expensive Product: USB Cable ($5)

📈 Highest Stock: Mouse (150 units)
📉 Lowest Stock: Webcam (3 units)

⚠️  LOW STOCK ALERT (2 products):
   - Webcam: 3 units remaining
   - Keyboard: 4 units remaining


==================================================
```

**Export Option:** Save report as `.txt` file with unique filename

## 🎨 Color Version Features

The `main(color).py` version includes:
- 🟢 **Green** - Success messages
- 🔴 **Red** - Errors and warnings
- 🔵 **Cyan** - Information and headers
- 🟡 **Yellow** - Current values and alerts
- 🟣 **Magenta** - Special highlights

## 📊 CSV File Structure

The `inventory.csv` file stores data in the following format:

```csv
prod_id,prod_name,prod_price,prod_quan
a1b2c3d4,Laptop,999,10
e5f6g7h8,Mouse,25,50
```

**Fields:**
- `prod_id` - Unique 8-character UUID
- `prod_name` - Product name (string)
- `prod_price` - Price per unit (numeric)
- `prod_quan` - Quantity in stock (integer)

## 🔒 Data Safety Features

1. **File Creation** - Automatically creates CSV if missing
2. **Empty File Handling** - Recreates headers if file is empty
3. **Confirmation Prompts** - Asks before deleting products
4. **Duplicate Prevention** - Warns before adding existing products
5. **Input Validation** - Checks for empty inventory before operations

## 🛠️ Technical Details

### Libraries Used

- **csv** - CSV file reading/writing
- **os** - File path and existence checking
- **uuid** - Unique ID generation
- **tabulate** - Formatted table display
- **colorama** - Terminal colors (color version only)

### Key Functions

| Function | Description |
|----------|-------------|
| `initialize_csv()` | Creates/validates CSV file |
| `generate_prod_id()` | Generates unique 8-char UUID |
| `load_prod()` | Loads products from CSV to list |
| `save_prod()` | Saves product list to CSV |
| `add_prod()` | Adds new product with duplicate check |
| `view_prod()` | Displays all products in table |
| `search_prod()` | Searches product by name |
| `update_prod()` | Updates product by ID |
| `delete_prod()` | Deletes product with confirmation |
| `generate_report()` | Creates detailed analytics |
| `export_report()` | Saves report to file |

## 🚧 Future Enhancements

### Planned Features
- 🛒 **Buy Orders** - Restock inventory
- 💰 **Sell Orders** - Process sales with stock validation
- 📜 **Transaction History** - Track all buy/sell operations
- 📈 **Sales Analytics** - Revenue and profit tracking
- 🔐 **User Authentication** - Multi-user support
- 💾 **Database Support** - SQLite/MySQL integration
- 🌐 **Web Interface** - Flask/Django web app
- 📱 **Mobile App** - Cross-platform mobile version

## 🐛 Known Issues

1. No input validation for numeric fields (price, quantity)
2. Case-sensitive product name comparison in delete function
3. No backup mechanism for CSV file
4. Limited to single CSV file (no multi-store support)

## 📝 Example Usage

### Adding a Product
```
Enter your product name: Laptop
Enter the price: 999
Please enter the quantity as well: 10

✓ Laptop is added with the Id: a1b2c3d4 in the inventory
```

### Searching a Product
```
Please Enter Product Name: laptop

----- Product Found -----
ID: a1b2c3d4
Name: Laptop
Price: $999
Quantity: 10
```

### Generating Report
```
Do you want to export this report to a file? (y/n): y

✓ Report exported to: inventory_report_x7y9z2a4.txt
```

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a learning project for Python CSV operations and inventory management systems.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

For questions or issues, please create an issue in the project repository.

---

**Version:** 1.0.0  
**Last Updated:** November 2025  
**Python Version:** 3.10+

---

### Quick Start Commands

```bash
# Clone or download the project
cd "Inventory Manager(CSV)"

# Install dependencies
pip install colorama tabulate

# Run standard version
python main.py

# Run colorful version
python main(color).py
```

---

**Happy Inventory Managing! 📦✨**