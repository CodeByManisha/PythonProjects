from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def say_hey():
   return render_template("index.html")

if __name__ == "__main__":
    # Run the app in debug mode  to auto-reload
    app.run(debug=True)
