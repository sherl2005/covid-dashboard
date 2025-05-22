# main.py
from data.fetch import fetch_data
from eda.visualize import plot_cases
from forecast.arima_model import train_arima
from forecast.prophet_model import train_prophet

if __name__ == "__main__":
    df = fetch_data("India")
    plot_cases(df)

    train = df["Daily Cases"][:-30]
    test = df["Daily Cases"][-30:]

    arima_forecast, arima_error = train_arima(train, test)
    prophet_forecast, prophet_error = train_prophet(df)

    print(f"ARIMA MAE: {arima_error:.2f}")
    print(f"Prophet MAE: {prophet_error:.2f}")
