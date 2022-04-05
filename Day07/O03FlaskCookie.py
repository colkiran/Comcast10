
from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index04.html", usrname="Peter")

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Success")
    resp.set_cookie("Cookie01", "Bangalore")
    resp.set_cookie("Cookie02", "Hyderabad")
    return resp

@app.route("/get_cookie")
def get_cookie():
    val1 = request.cookies.get('Cookie01')
    val2 = request.cookies.get('Cookie02')
    if val1 == None:
        val1 = "Cookie Deleted....."
    elif val2 == None:
        val2 = "Cookie Deleted....."

    return "<h1> First Cookie :" + val1 + "<br> Second Cookie :" + val2 + " </h1>"


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("Deleted Cookies Successfully.....")
    resp.delete_cookie("Cookie02")
    return resp


if __name__ == '__main__':
    app.run(debug=True)

