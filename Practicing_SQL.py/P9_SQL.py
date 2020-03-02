""" Practive 9 Left Outer Join """

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT);
    
INSERT INTO customers (name, email) VALUES ("Doctor Who", "doctorwho@timelords.com");
INSERT INTO customers (name, email) VALUES ("Harry Potter", "harry@potter.com");
INSERT INTO customers (name, email) VALUES ("Captain Awesome", "captain@awesome.com");

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    item TEXT,
    price REAL);

INSERT INTO orders (customer_id, item, price)
    VALUES (1, "Sonic Screwdriver", 1000.00);
INSERT INTO orders (customer_id, item, price)
    VALUES (2, "High Quality Broomstick", 40.00);
INSERT INTO orders (customer_id, item, price)
    VALUES (1, "TARDIS", 1000000.00);

# Come up with a query that lists the name and email of every customer 
# followed by the item and price of orders they've made

SELECT c.name, c.email, o.item, o.price 
FROM customers c 
LEFT OUTER JOIN orders o 
ON c.id = o.customer_id;

# Create another query that will result in one row per each customer, 
# with their name, email, and total amount of money they've spent on orders

SELECT c.name, c.email, SUM(o.price) AS "total_amount" 
FROM customers c
LEFT OUTER JOIN orders o ON c.id = o.customer_id
GROUP BY c.id 
ORDER BY total_amount DESC;