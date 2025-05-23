import pandas as pd
import matplotlib.pyplot as plt

# Load transformed data
df = pd.read_csv(r"C:\Users\helee\OneDrive\Desktop\purvi\transformed_sales_data.csv")

# Visualization - Sales Trend by Year
plt.figure(figsize=(10, 6))
for country in df['Country'].unique():
    country_data = df[df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Sales'], label=country)

plt.title('Sales Trend by Country')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

# Show plot directly in the terminal
plt.show(block=True)
