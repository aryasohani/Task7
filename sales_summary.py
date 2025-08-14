import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",    # MySQL host
    user="root",         # MySQL username
    password="root",         # Your MySQL password
    database="sales_db"  # Your database name
)

# SQL query
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql(query, conn)

# Print results
print(df)

# Bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.ylabel('Revenue')
plt.title('Revenue by Product')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
