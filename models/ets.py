import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def perform_ets_prediction(data):
    """Perform ETS prediction."""
    # Preprocess the data
    data = data[['4. close']]  # Use the correct column name
    data.columns = ['Close']

    # Ensure the index is a proper datetime index and sorted
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()

    # Ensure daily frequency
    data = data.asfreq('D')

    # Fit the ETS model
    model = ExponentialSmoothing(data['Close'], trend='add', seasonal=None)  # No seasonality for daily data
    model_fit = model.fit()

    # Forecast the next day's closing price
    forecast = model_fit.forecast(steps=1)

    return forecast.iloc[0]  # Return the prediction value