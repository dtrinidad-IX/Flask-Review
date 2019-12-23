from main import app, db, bcrypt, login_manager
from flask import render_template, request, url_for, redirect
from main.forms import login_form
from main.models import User
from flask_login import login_required, login_user, logout_user, current_user


@app.route('/welcome/dawd/dawdwd', methods = ["GET", "POST"] )
def home():
    return "<h1>WELCOME</h1>"


@app.route("/protected/dajwkda/dawkdlawd", methods = ["GET", "POST"])
@login_required
def protected():

    if "logout" in request.form:
        logout_user()
        return redirect("/")
    return render_template("bye.html")

@app.route('/', methods = ["GET", "POST"] )
def hello_world():
    form = login_form()
    if current_user.is_authenticated:
        print("Wwwww")
        return redirect(url_for("protected"))

    if form.validate_on_submit():
        # hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        # user = User(email = form.email.data, username = hashed)
        # db.session.add(user)
        # db.session.commit()
        # return redirect(url_for("home"))
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            password = bcrypt.check_password_hash(user.username, form.password.data)
            if password:
                login_user(user)
                return redirect(url_for("protected"))


    return render_template("sample.html", log_form = form)