import streamlit as st
import pandas as pd

# Load the CSV file
transactions = pd.read_csv('Transactional_data_retail_01.csv')

# Strip any leading or trailing spaces from column names
transactions.columns = transactions.columns.str.strip()

# Print available columns to the app for debugging
st.write("Available columns in the DataFrame:")
st.write(transactions.columns.tolist())  # Display column names as a list

# Check if the DataFrame is empty
if transactions.empty:
    st.error("The DataFrame is empty. Please check the CSV file.")
else:
    # Display the first few rows of the DataFrame
    st.write(transactions.head())

    # Define stock_code for filtering
    stock_code = 'YOUR_STOCK_CODE'  # Replace with the actual stock code you want to filter

    # Check for required columns
    required_columns = ['StockCode', 'TransactionDate', 'Quantity']
    missing_columns = [col for col in required_columns if col not in transactions.columns]

    # If there are missing columns, display an error
    if missing_columns:
        st.error(f"Missing columns in the data: {', '.join(missing_columns)}. Please check the CSV file.")
    else:
        # Proceed to filter and group the data
        product_sales = transactions[transactions['StockCode'] == stock_code].groupby('TransactionDate')['Quantity'].sum()
        st.write(product_sales)  # Display the product sales data
