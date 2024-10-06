import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
transactions = pd.read_csv('/path/to/Transactional_data_retail_01.csv')
top_10_products = transactions.groupby('StockCode')['Quantity'].sum().nlargest(10)
stock_code = st.selectbox('Select Stock Code', top_10_products.index)
weeks = st.slider('Number of Weeks to Forecast', 1, 15)
product_sales = transactions[transactions['StockCode'] == stock_code].groupby('TransactionDate')['Quantity'].sum()
train_data = product_sales[:-15]
model = ARIMA(train_data, order=(5,1,0))
result = model.fit()
forecast = result.forecast(steps=weeks)
st.write(f"Forecast for {stock_code} for {weeks} weeks:")
st.line_chart(forecast)

