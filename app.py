import streamlit as st
import pandas as pd

# Load the CSV file
try:
    transactions = pd.read_csv('Transactional_data_retail_01.csv')
except FileNotFoundError:
    st.error("The specified CSV file was not found. Please check the file path.")
    st.stop()  # Stop further execution if file not found

# Strip any leading or trailing spaces from column names
transactions.columns = transactions.columns.str.strip()

# Print available columns to the app for debugging
st.write("Available columns in the DataFrame:")
st.write(transactions.columns.tolist())  # Display column names as a list

# Define stock_code for filtering
stock_code = 'YOUR_STOCK_CODE'  # Replace with the actual stock code you want to filter

# Check for required columns
required_columns = ['StockCode', 'TransactionDate', 'Quantity']
missing_columns = [col for col in required_columns if col not in transactions.columns]

if missing_columns:
    st.error(f"Missing columns in the data: {', '.join(missing_columns)}. Please check the CSV file.")
else:
    # Check if the DataFrame is empty
    if transactions.empty:
        st.error("The DataFrame is empty. Please check the CSV file.")
    else:
        # Attempt to filter and group the data
        try:
            product_sales = transactions[transactions['StockCode'] == stock_code].groupby('TransactionDate')['Quantity'].sum()
            st.write(product_sales)  # Display the product sales data
        except Exception as e:
            st.error(f"An error occurred while processing the data: {str(e)}")
