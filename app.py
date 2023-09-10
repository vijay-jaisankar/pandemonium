from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from imgflip import get_meme_url

"""
    @constant Default image in case API throws errors
"""
DEFAULT_IMAGE_URI = "https://cdn.vectorstock.com/i/preview-1x/65/30/default-image-icon-missing-picture-page-vector-40546530.jpg"


"""
    Initialise Flask app
"""
app = Flask(__name__)
Bootstrap(app)


"""
    Base API Route to check if Flask is up and running
"""
@app.get("/")
def index():
    global DEFAULT_IMAGE_URI
    sample_img_url = get_meme_url()
    if sample_img_url is None:
        sample_img_url = DEFAULT_IMAGE_URI
    return render_template("index.html", image_url = sample_img_url)


"""
    Run the Flask App
"""
if __name__ == "__main__":
    app.run(debug = True)