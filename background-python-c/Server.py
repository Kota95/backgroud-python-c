from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def Output():
    return render_template('index.html'), 200

app.run(debug=True, host="0.0.0.0", port=9000)