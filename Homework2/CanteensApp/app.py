from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to the SQLite database
    conn = sqlite3.connect('database/DINERS.db')
    c = conn.cursor()

    # Retrieve all canteens
    c.execute("SELECT * FROM CANTEEN;")
    canteens = c.fetchall()

    # Close the connection
    conn.close()

    # Render the data in a template
    return render_template('index.html', canteens=canteens)

if __name__ == '__main__':
    app.run(debug=True)