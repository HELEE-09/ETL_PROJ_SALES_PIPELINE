import pandas as pd
import mysql.connector

# Load transformed data
transformed_df = pd.read_csv(r"C:\Users\helee\OneDrive\Desktop\purvi\transformed_sales_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Replace with your username
    password='123',  # Replace with your password
    database='SalesDB'
)

cursor = conn.cursor()

# Insert data into MySQL
for index, row in transformed_df.iterrows():
    cursor.execute("""
        INSERT INTO TransformedSalesData (Country, Year, Sales, Sales_Growth)
        VALUES (%s, %s, %s, %s)
    """, (row['Country'], row['Year'], row['Sales'], row['Sales Growth (%)']))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Transformed data successfully inserted into MySQL.")
