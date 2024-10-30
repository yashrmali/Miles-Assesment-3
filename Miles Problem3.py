import pandas as pd

# Read data
df = pd.read_csv('sales_data.csv')

# Calculate total sales per region
df['total_sales'] = df['price'] * df['quantity']
total_sales_by_region = df.groupby('region')['total_sales'].sum().reset_index()

# Average price per unit
df['average_price_per_unit'] = df.groupby('product_id')['price'].transform('mean')

# Filter for total sales > ₹10,000
filtered_data = df[df['total_sales'] > 10000]

# Outputs
print("Total Sales by Region:")
print(total_sales_by_region)
print("Filtered Data:")
print(filtered_data)


# 3. Using pandas for Extensive Data Manipulation
# You have a large dataset in CSV format that contains sales data for multiple products. 
# The columns include:
# - product_id: The product's unique ID
# - date: The date of the sale
# - price: The price of the product sold
# - quantity: The number of units sold
# - region: The region where the product was sold

# Your task is to:
# 1. Group the data by region and calculate the total sales (price * quantity) for each region.
# 2. Create a new column, `average_price_per_unit`, which calculates the average price per unit sold for each `product_id`.
# 3. Filter the dataset to include only the rows where the total sales for that product exceed ₹10,000.

# Sample CSV Data:
# product_id,date,price,quantity,region
# 101,2024-09-01,500,20,North
# 102,2024-09-01,600,15,South
# 103,2024-09-02,300,40,West
# 104,2024-09-02,800,5,North
# 105,2024-09-03,700,10,East

# Expected Output (After Manipulation):
# - Grouped by region: total sales for each region.
# - New column `average_price_per_unit` for each product.
# - Filtered rows where total sales exceed ₹10,000.

# Tricky Aspects:
# - How would you efficiently handle this if the dataset contains millions of rows?
#   Consider using chunking with pd.read_csv() to process the data in smaller batches 
#   or utilizing Dask for out-of-core computation.
#
# - What are some possible performance optimizations you can make with pandas 
#   when filtering large datasets?
#   Use vectorized operations instead of loops, apply categorical data types, 
#   and consider using `query()` for filtering.
#
# - How will you handle cases where some `product_id` values are missing or duplicated?
#   Handle missing values using fillna() or dropna(), and check for duplicates 
#   using df.duplicated() and then resolve them appropriately (e.g., using groupby or drop).
