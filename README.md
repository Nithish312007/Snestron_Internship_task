# 🛍️ Online Store Database – Snestron DevOps Internship Project

## 📌 Task Title:
**Design and Query a Relational Database for an Online Store**

This project was created as part of the **Snestron DevOps Internship – July 2025**. The objective was to build a fully functional relational database for a simulated online store using **MySQL**, and to interact with it programmatically using **Python**.

## 🔧 Project Overview

This system simulates a mini e-commerce backend, including:
- 🧍 Customers  
- 📦 Products  
- 🧾 Orders  
- 📄 Ordered Items  
- 💳 Payments  

## 🧰 Technologies Used

| Tool/Technology       | Purpose                          |
|-----------------------|----------------------------------|
| 🐍 Python 3.x         | Automate DB operations           |
| 🐬 MySQL (via XAMPP)  | Database backend                 |
| 📦 mysql-connector-python | Python ↔ MySQL communication |
| 🖥️ Python IDLE        | Script execution environment     |
| 🔍 phpMyAdmin         | GUI for viewing database tables  |


## ✅ Features Implemented

- ✅ 5 Relational tables created with foreign keys
- ✅ Sample data inserted (customers, products, orders, payments)
- ✅ Automated via Python — not manually created
- ✅ SQL queries executed:
  - List all customers and products
  - Show orders with customer name and item count
  - Calculate total amount per order
  - Identify most sold product
- ✅ Outputs displayed in terminal and verified via phpMyAdmin

## ▶️ How to Run the Project

1. **Start XAMPP** → Turn on **MySQL**
2. **Open phpMyAdmin** → Create a new database named `online_store_db`
3. **Install MySQL connector (once only)**:
   ```bash
   pip install mysql-connector-python
Run the script using Python IDLE:

Open Snestron_Internship.py in Python IDLE

Press F5 to execute

View Results:

Terminal window will show SQL outputs

phpMyAdmin will show table structure and inserted data



👨‍💻 Author
Nithish V
DevOps Intern – July 2025
Snestron Internship Program

🙏 Acknowledgement
Special thanks to the Snestron Internship Team for organizing this opportunity and helping us grow through real-world project experience.

“Let’s build, learn, and grow together!” 🚀
