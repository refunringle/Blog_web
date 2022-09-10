
import email
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String)
    publish_time = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return f"{self.id} - {self.title}"
    
    
class users(db.Model):
    """User account model."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
	)
    # confirm_pass = PasswordField(
    #     'Confirm Your Password',
    #     validators=[
    #         DataRequired(),
    #         EqualTo('password', message='Passwords must match.')
    #     ]
    # )

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    
@app.route("/",methods =['GET','POST'])
def index():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post = Post(title = title, content = content)
        db.session.add(post)
        db.session.commit()
    allPost = Post.query.all()
    # print(allPost)
    return render_template("index.html",posts = allPost)

  
    
@app.route("/signup",methods =['POST'])
def user():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        post = Post(name = name ,email = email ,password = password)
        db.session.add(post)
        db.session.commit()
    allPost = Post.query.all()
    # print(allPost)
    return render_template("signup.html",posts = allPost)



if __name__ == "__main__":
    app.run(debug=True)