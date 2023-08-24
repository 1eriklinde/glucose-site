import sqlite3

def initialize_database():
    conn = sqlite3.connect('glucose_data.db')
    cursor = conn.cursor()

    # Create the glucose_readings table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS glucose_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            glucose_value REAL,
            trend_arrow TEXT,
            timestamp TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def insert_glucose_reading(glucose_value, trend_arrow, timestamp):
    conn = sqlite3.connect('glucose_data.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO glucose_readings (glucose_value, trend_arrow, timestamp) VALUES (?, ?, ?)",
                  (glucose_value, trend_arrow, timestamp))
    
    conn.commit()
    conn.close()

def get_latest_glucose_data():
    conn = sqlite3.connect('glucose_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT glucose_value, trend_arrow, timestamp FROM glucose_readings ORDER BY timestamp DESC LIMIT 1")
    latest_data = cursor.fetchone()
    conn.close()

    if latest_data:
        return latest_data
    else:
        return ("No data available", "", "")
