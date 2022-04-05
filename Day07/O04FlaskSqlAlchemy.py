
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Hello World"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite3"

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/students"

db  = SQLAlchemy(app)

class students(db.Model):
    studid =db.Column('student_id', db.Integer, primary_key=True)
    sname = db.Column(db.String(50))
    stud_cls = db.Column(db.String(50))
    addr = db.Column(db.String(50))
    city = db.Column(db.String(50))
    pin = db.Column(db.String(6))

    def __init__(self, sname, scls, addr, city, pin):
        self.sname = sname
        self.stud_cls = scls
        self.addr = addr
        self.city = city
        self.pin = pin

@app.route("/")
def show_all():
    return render_template("show_all.html", students= students.query.all())

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['sname'] or not request.form['studcls'] or not \
            request.form['addr'] or not request.form['city']:
            flash("Please enter all the fields", "error")
        else:
            student= students(request.form['sname'], request.form['studcls'],
                              request.form['addr'], request.form['city'],request.form['pin'])
            db.session.add(student)
            db.session.commit()

            flash("Record added successfully into the database......")
            return redirect(url_for("show_all"))

    return render_template("new.html")

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)