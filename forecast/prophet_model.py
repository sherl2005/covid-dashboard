# prophet_model.py
from prophet import Prophet
from sklearn.metrics import mean_absolute_error
import pandas as pd

def train_prophet(df):
    df_prophet = df.reset_index()[["Date", "Daily Cases"]]
    df_prophet.columns = ["ds", "y"]
    model = Prophet()
    model.fit(df_prophet[:-30])
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    error = mean_absolute_error(df_prophet["y"][-30:], forecast["yhat"][-30:])
    return forecast, error