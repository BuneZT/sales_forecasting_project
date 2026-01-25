# Sales Forecasting & Analysis (Proof of concept)

## Description
This project focuses on analyzing sales trends, seasonality, and product category performance using a simulated sales environment. The project uses a **SQLite database** to store and query generated sales data, mimicking a real-world data analysis workflow where data is retrieved from a database.

The project demonstrates:
- Data generation and database management.
- Data extraction using SQL and Python.
- Advanced data visualization with Matplotlib and Seaborn.
- Analysis of temporal patterns (seasonality, day-of-week trends).

## Project Structure
- `data/`: Contains the SQLite database (`sales.db`).
- `notebooks/`: Jupyter notebooks for analysis.
    - `2.0-sql-analysis.ipynb`: Connects to the database and performs comprehensive EDA (Exploratory Data Analysis).
- `src/`: Source code.
    - `create_db.py`: Script to generate synthetic English sales data and populate the SQLite database.
- `requirements.txt`: Python dependencies.

## Setup

1. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   **Note for Developers:**
   This project uses `nbstripout` to automatically strip output and execution counts from Jupyter notebooks to keep the repository clean. Initialize the git filters by running:
   ```bash
   nbstripout --install
   ```

2. **Generate Database**
   Before running the analyses, generate the `sales.db` file by running the script:
   ```bash
   python src/create_db.py
   ```
   This will create a `data/sales.db` file populated with synthetic sales records (2024-2025).

3. **Run Analysis**
   Open the Jupyter Notebook to view the visualizations:
   - File: `notebooks/2.0-sql-analysis.ipynb`
   - You can run all cells to see the generated reports on sales trends, category performance, and price distributions.

## Technologies
- **Python**
- **SQLite** (Data Storage)
- **Pandas** (Data Manipulation)
- **Matplotlib & Seaborn** (Data Visualization)
