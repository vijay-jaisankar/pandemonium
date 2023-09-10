from flask import Flask


"""
    Initialise Flask app
"""
app = Flask(__name__)


"""
    Base API Route to check if Flask is up and running
"""
@app.get("/")
def index():
    return "<h1> Welcome to Pandemonium! </h1>"



"""
    Run the Flask App
"""
if __name__ == "__main__":
    app.run(debug = True)