import pandas as pd

# Load the data
df = pd.read_csv("C:/Users/helee/OneDrive/Desktop/purvi/fdi_raw.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Melt the DataFrame to transform year columns into rows
melted_df = df.melt(id_vars=['Country Name'],
                    value_vars=[str(year) for year in range(2022, 2024)],  # Adjust year range as needed
                    var_name='Year',
                    value_name='Sales')

# Filter conditions
country_filter = ['USA', 'India']  # Add desired countries
year_filter = ['2022', '2023']      # Years must be strings

# Extract data by Country and Year
filtered_df = melted_df[(melted_df['Country Name'].isin(country_filter)) &
                        (melted_df['Year'].isin(year_filter))]

# Display the filtered data
print(filtered_df)

# Optional: Save filtered data to a CSV
filtered_df.to_csv(r"C:\Users\helee\OneDrive\Desktop\purvi\filtered_sales_data.csv", index=False)

