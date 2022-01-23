from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret000"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youke.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone



@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000)





