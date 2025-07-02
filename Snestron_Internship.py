import mysql.connector

# 🔗 Connect to MySQL (XAMPP)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="online_store_db"
)
cursor = conn.cursor()

# 🧹 DROP Old Tables to Start Fresh
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("DROP TABLE IF EXISTS payment_box")
cursor.execute("DROP TABLE IF EXISTS ordered_items")
cursor.execute("DROP TABLE IF EXISTS order_table")
cursor.execute("DROP TABLE IF EXISTS item_store")
cursor.execute("DROP TABLE IF EXISTS customer_list")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
print("🧹 Old tables dropped successfully.\n")

# 🧱 CREATE Tables for Online Store
cursor.execute("""
CREATE TABLE customer_list (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL,
    cust_email VARCHAR(100) UNIQUE NOT NULL,
    signup_date DATE DEFAULT CURRENT_DATE
)
""")

cursor.execute("""
CREATE TABLE item_store (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    stock_left INT DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE order_table (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE DEFAULT CURRENT_DATE,
    order_status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES customer_list(customer_id)
)
""")

cursor.execute("""
CREATE TABLE ordered_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    qty_ordered INT,
    FOREIGN KEY (order_id) REFERENCES order_table(order_id),
    FOREIGN KEY (product_id) REFERENCES item_store(product_id)
)
""")

cursor.execute("""
CREATE TABLE payment_box (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    paid_amount DECIMAL(10,2),
    pay_mode VARCHAR(30),
    paid_on DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (order_id) REFERENCES order_table(order_id)
)
""")

print("✅ All tables created successfully.\n")

# 📥 INSERT Sample Data
cursor.execute("INSERT INTO customer_list (cust_name, cust_email) VALUES (%s, %s)", ("Nithish V", "nithish3120@example.com"))
cursor.execute("INSERT INTO customer_list (cust_name, cust_email) VALUES (%s, %s)", ("Diya R", "diya.rani@example.com"))

cursor.execute("INSERT INTO item_store (product_name, unit_price, stock_left) VALUES (%s, %s, %s)", ("Wireless Mouse", 499.0, 25))
cursor.execute("INSERT INTO item_store (product_name, unit_price, stock_left) VALUES (%s, %s, %s)", ("Mechanical Keyboard", 1799.0, 15))
cursor.execute("INSERT INTO item_store (product_name, unit_price, stock_left) VALUES (%s, %s, %s)", ("USB-C Cable", 199.0, 50))

cursor.execute("INSERT INTO order_table (customer_id, order_status) VALUES (%s, %s)", (1, "shipped"))

cursor.execute("INSERT INTO ordered_items (order_id, product_id, qty_ordered) VALUES (%s, %s, %s)", (1, 1, 2))  # 2 Mice
cursor.execute("INSERT INTO ordered_items (order_id, product_id, qty_ordered) VALUES (%s, %s, %s)", (1, 3, 1))  # 1 Cable

cursor.execute("INSERT INTO payment_box (order_id, paid_amount, pay_mode) VALUES (%s, %s, %s)", (1, 1197.0, "UPI"))

conn.commit()
print("📦 Sample data inserted into all tables.\n")

# 🔍 RUN Required SQL Queries

print("📋 All Customers:")
cursor.execute("SELECT * FROM customer_list")
for row in cursor.fetchall(): print(row)

print("\n📦 All Products:")
cursor.execute("SELECT * FROM item_store")
for row in cursor.fetchall(): print(row)

print("\n🛍 Orders with Customer Name & Item Count:")
cursor.execute("""
    SELECT o.order_id, c.cust_name, COUNT(oi.item_id) AS item_count
    FROM order_table o
    JOIN customer_list c ON o.customer_id = c.customer_id
    JOIN ordered_items oi ON o.order_id = oi.order_id
    GROUP BY o.order_id
""")
for row in cursor.fetchall(): print(row)

print("\n💰 Order Total vs Amount Paid:")
cursor.execute("""
    SELECT o.order_id,
           SUM(oi.qty_ordered * i.unit_price) AS total_price,
           p.paid_amount
    FROM order_table o
    JOIN ordered_items oi ON o.order_id = oi.order_id
    JOIN item_store i ON oi.product_id = i.product_id
    LEFT JOIN payment_box p ON p.order_id = o.order_id
    GROUP BY o.order_id
""")
for row in cursor.fetchall(): print(row)

print("\n🏆 Most Sold Product:")
cursor.execute("""
    SELECT i.product_name, SUM(oi.qty_ordered) AS total_qty
    FROM ordered_items oi
    JOIN item_store i ON oi.product_id = i.product_id
    GROUP BY i.product_id
    ORDER BY total_qty DESC
    LIMIT 1
""")
print(cursor.fetchone())

# 🔚 Close Connection
cursor.close()
conn.close()
print("\n🎉 Final Output: All steps complete — Database designed, data inserted, queries executed!")
