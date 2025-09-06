from flask import Flask
from flask import render_template
import requests

# Use your created api endpoint
resp = requests.get("")
resp.raise_for_status()
blog_posts = resp.json()

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", blogs=blog_posts)

@app.route("/about")
def get_about_page():
    return render_template("about.html")

@app.route("/contact")
def get_contact_page():
    return render_template("contact.html")

@app.route("/post/<int:blog_id>")
def get_post(blog_id):

    # checks every element until it finds the id provided by the index.html page (anchor tag)
    requested_post = None
    for blog_post in blog_posts:
        if int(blog_post["id"]) == int(blog_id):
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)