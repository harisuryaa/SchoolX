from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///ssb_neww.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
db.create_all()

@app.route('/')
def hello():
    return render_template('image.html')

@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200

@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

if __name__ == '__main__':
    app.run(debug=True)