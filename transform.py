import pandas as pd

# Load the filtered data
filtered_df = pd.read_csv(r"C:\Users\helee\OneDrive\Desktop\purvi\filtered_sales_data.csv")

# === DATA CLEANING ===
# Handle missing values by filling with 0
filtered_df = filtered_df.assign(Sales=filtered_df['Sales'].fillna(0))


# Convert 'Sales' column to float for calculations
filtered_df['Sales'] = pd.to_numeric(filtered_df['Sales'], errors='coerce').fillna(0)

# === DATA AGGREGATION ===
# Group by Country and Year, summing sales
transformed_df = filtered_df.groupby(['Country Name', 'Year']).agg({'Sales': 'sum'}).reset_index()

# === DATA ENRICHMENT ===
# Add a column for percentage growth (Year-over-Year growth)
transformed_df['Sales Growth (%)'] = transformed_df.groupby('Country Name')['Sales'].pct_change().fillna(0) * 100

# === DATA FORMATTING ===
# Rename columns for clarity
transformed_df.rename(columns={'Country Name': 'Country'}, inplace=True)

# Save the transformed data
transformed_df.to_csv(r"C:\Users\helee\OneDrive\Desktop\purvi\transformed_sales_data.csv", index=False)

print("Data transformation complete. File saved as 'transformed_sales_data.csv'")
