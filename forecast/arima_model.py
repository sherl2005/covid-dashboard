# arima_model.py
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error

def train_arima(train, test):
    model = auto_arima(train, seasonal=False, trace=False)
    forecast = model.predict(n_periods=len(test))
    error = mean_absolute_error(test, forecast)
    return forecast, error
