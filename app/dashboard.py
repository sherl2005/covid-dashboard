# dashboard.py
import streamlit as st
from data.fetch import fetch_data
from forecast.arima_model import train_arima
from forecast.prophet_model import train_prophet
from eda.visualize import plot_cases

st.title("COVID-19 Trend & Forecast Dashboard")

country = st.selectbox("Select Country", ["USA", "India", "Brazil", "UK", "Germany"])
df = fetch_data(country)

st.subheader("Raw Data")
st.line_chart(df["Daily Cases"])

st.subheader("Visualization")
plot_cases(df)

st.subheader("Forecasting")
train = df["Daily Cases"][:-30]
test = df["Daily Cases"][-30:]

arima_forecast, arima_error = train_arima(train, test)
prophet_forecast, prophet_error = train_prophet(df)

st.write(f"ARIMA MAE: {arima_error:.2f}")
st.write(f"Prophet MAE: {prophet_error:.2f}")