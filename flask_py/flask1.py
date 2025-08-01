from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# Appointment booking route
@app.route("/book", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        name = request.form["name"]
        contact_number = request.form["contact"]
        date_of_app = request.form["date"]
        time_of_app = request.form["time"]

        new_appointment = Appointment(
            name=name,
            contact=contact_number,
            date=date_of_app,
            time=time_of_app
        )
        db.session.add(new_appointment)
        db.session.commit()

        return "<h2>Thank you! Your appointment has been booked.</h2>"

    return render_template("book.html")

# View all appointments
@app.route("/appointments")
def view_appointments():
    all_appointments = Appointment.query.all()
    return "<br>".join(
        [f"{a.name} — {a.contact} — {a.date} — {a.time}" for a in all_appointments]
    )

# About Us page
@app.route("/about")
def about_us():
    return "<h2>About Us Page</h2><p>This is a simple Appointment Booking System built with Flask and SQLAlchemy.</p>"

if __name__ == "__main__":
    app.run(debug=True)
