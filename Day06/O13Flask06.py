
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index03.html", usrname=name, content="Fruits available in all seasons",
                            fruits=['Apple', 'Orange', 'Grapes', 'Pineapple', 'Mango', 'Banana', 'Gauva', 'Strawberry'])

if __name__ == '__main__':
    app.run(debug=True)