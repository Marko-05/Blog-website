from flask import Flask
from flask import render_template,request
import requests
import smtplib

# Write your email and app password here
YOUR_EMAIL = ""
YOUR_APP_PASSWORD = ""

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

@app.route("/contact", methods=["POST","GET"])
def get_contact_page():
    if request.method == 'POST':
        print(request.form["full_name"])
        print(request.form["emailadr"])
        print(request.form["phonenum"])
        print(request.form["message_body"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=YOUR_EMAIL,password=YOUR_APP_PASSWORD)
            connection.sendmail(from_addr=YOUR_EMAIL,to_addrs=YOUR_EMAIL,msg=f"Subject:New Message!\n\nName: {request.form["full_name"]}\nEmail: {request.form["emailadr"]}\nPhone: {request.form["phonenum"]}\nMessage: {request.form["message_body"]}")
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)

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