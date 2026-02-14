# Data Forecasting & Analysis Notebooks

## Description
This repository is dedicated to exercises and experiments with data forecasting. It serves as a sandbox for testing various regression analysis techniques and predictive modeling approaches across different domains.

The project demonstrates:
- **Data Wrangling & Cleaning**: Preparing raw data for analysis.
- **Exploratory Data Analysis (EDA)**: Visualizing relationships and distributions.
- **Statistical Modeling**: Using OLS regression and other statistical methods.
- **Predictive Analytics**: Forecasting future values based on historical data.

## Notebooks Overview

The `notebooks/` directory contains the following analyses:

1.  **[House Price Forecast](notebooks/House_price_forcast.ipynb)**
    -   **Goal**: Predict house prices based on features like square footage, grade, age, and location.
    -   **Key Techniques**: Multiple Linear Regression, Log-transformation of target variables, Feature Engineering (e.g., luxury district identification).

2.  **[Insurance Cost Forecast](notebooks/Insurance%20cost%20forcast.ipynb)**
    -   **Goal**: Forecast medical insurance charges based on patient demographics and lifestyle choices.
    -   **Key Techniques**: Interaction terms (e.g., Smoker * BMI), Residual Analysis, Shapiro-Wilk Normality Test.

3.  **[Sales & SQLite Analysis](notebooks/sqlite_prediction_poc.ipynb)**
    -   **Goal**: Analyze sales trends and seasonality using a SQL-backed data source.
    -   **Key Concepts**: SQL integration with Python, Time-series analysis visualization.

## Project Structure
- `data/`: Contains datasets (CSV files like `insurance.csv`, `kc_house_data.csv`) and the SQLite database (`sales.db`).
- `notebooks/`: Jupyter notebooks containing the analysis and code.
- `src/`: Helper scripts.
    - `create_db.py`: Script to generate synthetic sales data for the SQLite analysis.
- `requirements.txt`: Python dependencies.

## Setup

1. **Install Dependencies**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Database (Optional)**
   For the Sales/SQLite analysis, you may need to generate the database file:
   ```bash
   python src/create_db.py
   ```

3. **Run Notebooks**
   Open any of the notebooks in the `notebooks/` folder to view the analysis and run the models.

## Technologies
- **Python**
- **Statsmodels & Scikit-Learn** (Modeling)
- **Pandas & NumPy** (Data Manipulation)
- **Matplotlib & Seaborn** (Data Visualization)
- **SQLite** (Data Storage)
