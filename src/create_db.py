import sqlite3
import pandas as pd
import numpy as np
import datetime
import os

# Configuration
# Set path relative to the script file, not the terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'sales.db')
START_DATE = datetime.date(2024, 1, 1)
END_DATE = datetime.date(2025, 12, 31)
CATEGORIES = ['Electronics', 'Clothing', 'Home & Garden']

def generate_sales_data(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += datetime.timedelta(days=1)
    
    data = []
    
    # Generate data for each date and category
    for date in dates:
        # Seasonality (sinusoidal) + linear trend + random noise
        day_of_year = date.timetuple().tm_yday
        trend = (date - start_date).days * 0.1 # Slight increase over time
        
        # Simulation: more sales on weekends
        is_weekend = 1 if date.weekday() >= 5 else 0
        weekend_boost = 50 * is_weekend
        
        # Simulation: Peak in December (holidays)
        christmas_boost = 100 if date.month == 12 else 0

        for category in CATEGORIES:
            base_sales = 100
            if category == 'Electronics':
                base_sales = 200 + trend + (50 * np.sin(day_of_year / 365 * 2 * np.pi))
            elif category == 'Clothing':
                base_sales = 150 + trend + (30 * np.cos(day_of_year / 365 * 2 * np.pi))
            elif category == 'Home & Garden':
                base_sales = 120 + trend + (80 * np.sin((day_of_year - 100) / 365 * 2 * np.pi)) # Spring peak
            
            final_sales = int(base_sales + weekend_boost + christmas_boost + np.random.normal(0, 20))
            final_sales = max(0, final_sales) # Cannot be negative
            
            data.append((date, category, final_sales))
            
    return data

def create_database():
    print(f"Generating data from {START_DATE} to {END_DATE}...")
    sales_data = generate_sales_data(START_DATE, END_DATE)
    
    print(f"Creating database at {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        category TEXT NOT NULL,
        amount INTEGER NOT NULL
    )
    ''')
    
    # Clear old data (optional)
    cursor.execute('DELETE FROM sales')
    
    # Insert new data
    cursor.executemany('INSERT INTO sales (date, category, amount) VALUES (?, ?, ?)', sales_data)
    
    conn.commit()
    
    # Verification
    count = cursor.execute('SELECT COUNT(*) FROM sales').fetchone()[0]
    print(f"Success! Database now contains {count} records.")
    
    conn.close()

if __name__ == "__main__":
    create_database()
