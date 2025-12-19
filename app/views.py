from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Ticket
from . import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/submit_ticket", methods=["POST"])
def submit_ticket():
    name = request.form.get("name").strip()
    department = request.form.get("department")
    issue = request.form.get("issue").strip()

    if not name or not issue:
        flash("Name and issue are required.", "warning")
        return redirect(url_for("main.user_dashboard"))

    t = Ticket(user_name=name, department=department, issue=issue)
    db.session.add(t)
    db.session.commit()

    flash("Ticket submitted successfully.", "success")
    return redirect(url_for("main.user_dashboard"))

@main_bp.route("/user_dashboard")
def user_dashboard():
    return render_template("user_dashboard.html")


