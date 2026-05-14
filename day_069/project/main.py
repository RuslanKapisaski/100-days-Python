from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import (
    UserMixin, login_user, LoginManager,
    current_user, logout_user
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

ckeditor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
Bootstrap5(app)



# DB SETUP
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# MODELS
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    posts: Mapped[list["BlogPost"]] = relationship(
        "BlogPost",
        back_populates="user"
    )

    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="user"
    )


class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # relationships
    user: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )

    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="post"
    )


class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_posts.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="comments"
    )

    post: Mapped["BlogPost"] = relationship(
        "BlogPost",
        back_populates="comments"
    )


with app.app_context():
    db.create_all()


# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))



# ADMIN DECORATOR
def admin_only(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        if current_user.id != 1:
            abort(403)
        return f(*args, **kwargs)
    return decorated



# AUTH ROUTES
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data, method="scrypt")

        if User.query.filter_by(email=form.email.data).first():
            flash("Email already exists")
            return redirect(url_for("register"))

        user = User(
            email=form.email.data,
            name=form.name.data,
            password=hashed
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            flash("Wrong credentials")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


# POSTS
@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()

    if form.validate_on_submit():

        if not current_user.is_authenticated:
            return redirect(url_for("login"))

        comment = Comment(
            text=form.comment.data,
            user=current_user,
            post=post
        )

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for("show_post", post_id=post_id))

    return render_template("post.html", post=post, form=form)


# CREATE POST
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()

    if form.validate_on_submit():

        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            user=current_user
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)



# EDIT POST
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)

    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        body=post.body,
        img_url=post.img_url
    )

    if form.validate_on_submit():

        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.img_url = form.img_url.data

        db.session.commit()

        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=form, is_edit=True)



# DELETE POST
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))



# STATIC PAGES
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)