
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('../database/data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, text TEXT)")
    cursor.execute("INSERT INTO messages (text) VALUES ('Hello from Flask!')")
    conn.commit()
    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/api/messages')
def messages():
    return jsonify(get_data())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
