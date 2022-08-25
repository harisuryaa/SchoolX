from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///ssb_neww.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)



class Personal_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    year=db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(250), nullable=False)
    educational_bg = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    img_url = db.Column(db.String(250), nullable=True)
    ln_url=db.Column(db.String(250), nullable=True)
db.create_all()

# all Flask routes below
# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/", methods=["GET","POST"])
def receive_data():
    data = request.args.get('search')
    if data:
        profile = Personal_data.query.filter_by(name=data).first()
        data = profile.img_url
        print(data)
        return render_template('profile.html', data=profile)
    return render_template("index.html")

@app.route("/feeds")
def feeds():
    return render_template("feeds.html")

if __name__ == '__main__':
    app.run(debug=True)
