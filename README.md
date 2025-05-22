# COVID-19 Dashboard

This is a COVID-19 data visualization and forecasting dashboard built with Python, Streamlit, and data science libraries.

## Features

- Fetches and processes COVID-19 data by country
- Visualizes daily COVID-19 cases with 7-day rolling averages
- Provides time-series forecasting using ARIMA and Prophet models
- Interactive dashboard built with Streamlit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/covid-dashboard.git
   cd covid-dashboard
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv covid-env
   source covid-env/bin/activate    # On Windows use: covid-env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app with:

```bash
streamlit run app/dashboard.py
```

Open your browser and go to `http://localhost:8501` to view the dashboard.

## Project Structure

* `app/dashboard.py`: Main Streamlit app
* `data/fetch.py`: Data fetching and preprocessing functions
* `visualize.py`: Visualization utilities
* `models/`: Contains forecasting models (ARIMA, Prophet)
* `requirements.txt`: Python dependencies

## License

This project is licensed under the MIT License.
