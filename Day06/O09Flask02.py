

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Hello {usrname} </h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("user", usrname="root"))

if __name__ == "__main__":
    app.run()
