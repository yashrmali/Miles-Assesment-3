# Miles-Assesment-3
# 📊 Sales Data Analysis

## Overview
This project performs extensive data manipulation on a sales dataset using Pandas. The script reads sales data from a CSV file, calculates total sales per region, computes average prices per unit for each product, and filters the dataset based on total sales criteria.

## 📋 Sample CSV Data
The dataset should be in the following format:
```
product_id,date,price,quantity,region
101,2024-09-01,500,20,North
102,2024-09-01,600,15,South
103,2024-09-02,300,40,West
104,2024-09-02,800,5,North
105,2024-09-03,700,10,East
```

## 🛠️ Requirements
To run this script, you will need:
- Python 3.x
- `pandas` library

### Install Required Libraries
You can install the necessary library using pip:
```bash
pip install pandas
```


## 🔍 Key Considerations

### Data Structure
- The dataset contains the following columns:
  - `product_id`: The product's unique ID
  - `date`: The date of the sale
  - `price`: The price of the product sold
  - `quantity`: The number of units sold
  - `region`: The region where the product was sold

### Tricky Aspects
- **Handling Large Datasets**: If the dataset contains millions of rows, consider using chunking with `pd.read_csv()` to process the data in smaller batches or utilizing Dask for out-of-core computation.
  
- **Performance Optimizations**: Use vectorized operations instead of loops, apply categorical data types, and consider using `query()` for filtering to enhance performance.

- **Missing or Duplicated Product IDs**: Handle missing values with `fillna()` or `dropna()`, and check for duplicates using `df.duplicated()`. Resolve them appropriately (e.g., using `groupby()` or `drop()`).

## 🚀 Getting Started
1. Create a CSV file named `sales_data.csv` with the sample data or your own sales data.
2. Run the script in your Python environment to analyze the sales data.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

 Happy coding! 🎉
