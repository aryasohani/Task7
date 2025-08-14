# Task 7 – Basic Sales Summary (MySQL + Python)

## Objective
Connect Python to a MySQL database, run a sales summary query, and visualize revenue by product.

## Tools
- MySQL
- Python (mysql-connector-python, pandas, matplotlib)
- VS Code

## Steps
1. Created `sales` table in MySQL with product, quantity, price.
2. Inserted sample data.
3. Ran SQL query:
   ```sql
   SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;

## How to Run
pip install mysql-connector-python pandas matplotlib
python sales_summary.py
