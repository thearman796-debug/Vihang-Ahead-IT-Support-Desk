from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Ticket, User
from . import db

admin_bp = Blueprint("admin", __name__, template_folder="templates")

def admin_only(fn):
    from functools import wraps
    from flask import abort
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            abort(403)
        return fn(*args, **kwargs)
    return wrapper

@admin_bp.route("/")
@login_required
@admin_only
def dashboard():
    tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
    return render_template("admin_dashboard.html", tickets=tickets)

@admin_bp.route("/ticket/<int:ticket_id>")
@login_required
@admin_only
def ticket_detail(ticket_id):
    t = Ticket.query.get_or_404(ticket_id)
    return render_template("ticket_detail.html", t=t)

@admin_bp.route("/ticket/<int:ticket_id>/update", methods=["POST"])
@login_required
@admin_only
def update_ticket(ticket_id):
    t = Ticket.query.get_or_404(ticket_id)
    status = request.form.get("status")
    assigned_to = request.form.get("assigned_to")
    if status:
        t.status = status
    t.assigned_to = assigned_to
    db.session.commit()
    flash("Ticket updated.", "success")
    return redirect(url_for("admin.ticket_detail", ticket_id=ticket_id))

@admin_bp.route("/ticket/<int:ticket_id>/delete", methods=["POST"])
@login_required
@admin_only
def delete_ticket(ticket_id):
    t = Ticket.query.get_or_404(ticket_id)
    db.session.delete(t)
    db.session.commit()
    flash("Ticket deleted.", "info")
    return redirect(url_for("admin.dashboard"))
