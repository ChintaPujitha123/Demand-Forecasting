import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
import numpy as np

# Sample data preparation function - replace with your actual data loading and processing
def load_data(stock_code):
    # Replace this with actual code to load your data
    dates = pd.date_range(start="2021-01-01", periods=100, freq="W")
    actual_train = np.random.normal(200, 20, 60)
    predicted_train = actual_train + np.random.normal(0, 10, 60)
    actual_test = np.random.normal(250, 20, 40)
    predicted_test = actual_test + np.random.normal(0, 10, 40)
    train_data = pd.DataFrame({"Date": dates[:60], "Actual": actual_train, "Predicted": predicted_train})
    test_data = pd.DataFrame({"Date": dates[60:], "Actual": actual_test, "Predicted": predicted_test})
    return train_data, test_data

# Streamlit App
st.title("Demand Forecasting")

# Sidebar - User Input
stock_code = st.selectbox("Select a Stock Code:", ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "FB", "NFLX", "NVDA"])

# Load Data
train_data, test_data = load_data(stock_code)

# Main Plot - Actual vs Predicted
st.subheader(f"Demand Overview for {stock_code}")
plt.figure(figsize=(10, 6))
plt.plot(train_data["Date"], train_data["Actual"], 'r-', label="Train Actual Demand")
plt.plot(train_data["Date"], train_data["Predicted"], 'b--', label="Train Predicted Demand")
plt.plot(test_data["Date"], test_data["Actual"], 'g-', label="Test Actual Demand")
plt.plot(test_data["Date"], test_data["Predicted"], 'y--', label="Test Predicted Demand")
plt.xlabel("Date")
plt.ylabel("Demand")
plt.legend()
st.pyplot(plt)

# Error Distributions
train_error = train_data["Actual"] - train_data["Predicted"]
test_error = test_data["Actual"] - test_data["Predicted"]

# Training Error Distribution Plot
st.subheader("Training Error Distribution")
sns.histplot(train_error, kde=True, color="green", bins=15)
plt.xlabel("Error")
plt.ylabel("Frequency")
st.pyplot(plt)

# Testing Error Distribution Plot
st.subheader("Testing Error Distribution")
sns.histplot(test_error, kde=True, color="red", bins=15)
plt.xlabel("Error")
plt.ylabel("Frequency")
st.pyplot(plt)
