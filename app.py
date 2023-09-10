from flask import Flask, render_template


"""
    Initialise Flask app
"""
app = Flask(__name__)


"""
    Base API Route to check if Flask is up and running
"""
@app.get("/")
def index():
    return render_template("index.html")



"""
    Run the Flask App
"""
if __name__ == "__main__":
    app.run(debug = True)