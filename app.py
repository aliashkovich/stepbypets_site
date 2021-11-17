from flask import Flask, render_template
import pathlib

app = Flask(__name__,static_folder="templates")


@app.route("/")
def index():
    return render_template('index.html')


app.run(debug=True)
