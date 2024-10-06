import streamlit as st
import pandas as pd

# Load the CSV file
transactions = pd.read_csv('Transactional_data_retail_01.csv')

# Strip any leading or trailing spaces from column names
transactions.columns = transactions.columns.str.strip()

# Print available columns to the app for debugging
st.write(transactions.columns)

# Check the first few rows of the DataFrame
st.write(transactions.head())

# Filter and group the data
stock_code = 'YOUR_STOCK_CODE'  # Replace with the actual stock code you want to filter

# Check if the required columns exist
if 'StockCode' in transactions.columns and 'TransactionDate' in transactions.columns:
    product_sales = transactions[transactions['StockCode'] == stock_code].groupby('TransactionDate')['Quantity'].sum()
else:
    st.error("Required columns are missing from the data.")
