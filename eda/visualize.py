# visualize.py
import matplotlib.pyplot as plt

def plot_cases(df):
    df["7-Day Avg"] = df["Daily Cases"].rolling(window=7).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Daily Cases"], label="Daily Cases")
    plt.plot(df.index, df["7-Day Avg"], label="7-Day Average", linewidth=2)
    plt.legend()
    plt.title("COVID-19 Daily Cases")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.grid()
    plt.show()