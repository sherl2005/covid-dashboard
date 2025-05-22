# fetch.py
import requests
import pandas as pd

def fetch_data(country="USA"):
    url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=all"
    response = requests.get(url)
    data = response.json()
    cases = data['timeline']['cases']
    df = pd.DataFrame(list(cases.items()), columns=["Date", "Cases"])
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    df["Daily Cases"] = df["Cases"].diff().fillna(0)
    return df