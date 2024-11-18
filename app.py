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

# What`s done?
# 1. Removed global statements since its bad practice to rely on constant that some other function in future might modify
# 2. get_meme_url Result Check - used or to handle None responses more concisely.
# 3. Simplified the Logic: Removed unnecessary checks or redundant variable assignments.
# 4. Added more meta tags as per open issue on GH page
# 5. Removed styles.css - you dont need it since we are inheriting from bootstrap`s css. Unless you specifically want to style page yourself, you do not need styles.css
# 6. Added robots.txt and sitemap.xml. Since you have static site there is no need for dynaminc generation of urls (you have only index.html)
# Thus when you deploy this website to production make sure to modify both files, eg:
#   robots.txt
#  Sitemap: https://www.pandemonium-memes.com/sitemap.xml
#   sitemap.xml
#  <loc>https://www.pandemonium-memes.com/</loc>
# Documentation - what do you want to document? Only 1 webpage with 1 function and 1 API call so I think documenting it is redundant...
# 7. In index.html, in head section modify author and twitter handle to your, I put mine for now.
