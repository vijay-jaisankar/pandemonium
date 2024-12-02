from flask import Flask, render_template, send_from_directory, Response, url_for, make_response
from flask_bootstrap import Bootstrap
from imgflip import get_meme_url
from datetime import datetime

DEFAULT_IMAGE_URI = "https://cdn.vectorstock.com/i/preview-1x/65/30/default-image-icon-missing-picture-page-vector-40546530.jpg"

app = Flask(__name__)
Bootstrap(app)


@app.get("/")
def index():
    sample_img_url = get_meme_url() or DEFAULT_IMAGE_URI
    return render_template("index.html", image_url=sample_img_url)


@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')


@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == "__main__":
    app.run(debug=True)
