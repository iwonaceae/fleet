from flask import Flask, render_template
import sqlite3
import json

# Initialize the app
app = Flask(__name__)

# values from a database
conn = sqlite3.connect("fleet.db")
cur = conn.cursor()
cur.execute("SELECT * FROM vessel")
ships_data = cur.fetchall()

# ships directory
@app.route("/api/ships")
def ships():
    return render_template('ships.html', title='ships', ships=ships_data)

# positions directory
@app.route("/api/positions/<imo>")
def position(imo):
    with sqlite3.connect("fleet.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM position WHERE IMO_number = ? ORDER BY timestamp desc", (imo,))
        results = cur.fetchall()
        return render_template('positions.html', title='position', results=results)

# run server (by default on port 5000)
if __name__ == '__main__':
    app.run(port=8000, debug=True)