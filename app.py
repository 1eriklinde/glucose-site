import subprocess
from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the latest glucose data from the database
    latest_glucose_data = database.get_latest_glucose_data()

    return render_template('index.html', latest_glucose_data=latest_glucose_data)

def start_glucose_data_collection():
    subprocess.Popen(['python3', 'glucose_data_collector.py'])

if __name__ == '__main__':
    # Initialize the database
    database.initialize_database()

    # Start the glucose data collection process
    start_glucose_data_collection()

    # Run the Flask application
    app.run(port=5000, debug=True)
