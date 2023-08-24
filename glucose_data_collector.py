import datetime
import time
import sqlite3
import pytz
from pydexcom import Dexcom
import database

# Initialize the database
database.initialize_database()

# Set the Stockholm time zone using pytz
stockholm_timezone = pytz.timezone('Europe/Stockholm')

while True:
    dexcom = Dexcom("1eriklinde", "Eriklm1290", ous=True)
    bg = dexcom.get_current_glucose_reading()
    glucose_value = bg.mmol_l
    trend_arrow = bg.trend_arrow

    # Get the current time in the Stockholm time zone
    current_time = datetime.datetime.now(stockholm_timezone)

    # Save data to the database
    conn = sqlite3.connect('glucose_data.db')
    cursor = conn.cursor()

    # Format the timestamp without milliseconds and time zone offset
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M')

    cursor.execute("INSERT INTO glucose_readings (glucose_value, trend_arrow, timestamp) VALUES (?, ?, ?)",
                   (glucose_value, trend_arrow, formatted_time))

    conn.commit()
    conn.close()

    print(f'{formatted_time}: {glucose_value} {trend_arrow} (Saved to database)')

    # Wait for 5 minutes
    time.sleep(300)  # 5 minutes = 300 seconds
