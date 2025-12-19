print("AUTH BLUEPRINT LOADED")
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.role == "admin" and user.check_password(password):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("admin.dashboard"))

        flash("Invalid credentials or not an admin.", "danger")

    return render_template("admin_login.html")

@auth_bp.route("/admin/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect('/admin/login')

from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["arman"],
            email=request.form["thearman796@gmail.com"],
            password=request.form["London@0628"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("register.html")


