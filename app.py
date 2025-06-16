from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/time")
def time_api():
    now_utc = datetime.utcnow()
    ist = now_utc + timedelta(hours=5, minutes=30)
    return jsonify(time=ist.strftime("%H%M%S"))

if __name__ == "__main__":
    app.run(debug=True)
