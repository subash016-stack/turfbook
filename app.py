from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -------------------------
# Database Connection
# -------------------------
def db():
    return sqlite3.connect("turf.db")

# -------------------------
# Create Table
# -------------------------
def init_db():
    conn = db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date TEXT,
            slot TEXT
        )
    """)
    conn.close()

init_db()

# -------------------------
# Home Route
# -------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    conn = db()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        slot = request.form["slot"]

        cur.execute(
            "INSERT INTO bookings(name,date,slot) VALUES(?,?,?)",
            (name, date, slot)
        )
        conn.commit()

    data = cur.execute("SELECT * FROM bookings").fetchall()
    conn.close()

    return render_template("index.html", bookings=data)

# -------------------------
# Delete Booking
# -------------------------
@app.route("/delete/<int:id>")
def delete(id):
    conn = db()
    conn.execute("DELETE FROM bookings WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)