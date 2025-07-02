from flask import Blueprint, request, render_template,redirect,url_for
from flask_login import login_required, current_user
from models import db, Job

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/jobs/create", methods=["GET", "POST"])
@login_required
def create_job():
    if request.method == "POST":
        data = request.form
        job = Job(
            title=data["title"],
            company_name=data["company_name"],
            location=data["location"],
            job_type=data["job_type"],
            description=data.get("description"),
            skills=data.get("skills"),
            reference=data.get("reference"),
            user_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for("jobs.list_jobs"))
    return render_template("create_job.html")

@jobs_bp.route("/jobs")
def list_jobs():
    page = int(request.args.get("page", 1))
    per_page = 5
    jobs = Job.query.paginate(page=page, per_page=per_page)
    return render_template("job_list.html", jobs=jobs.items, total=jobs.total, page=page, per_page=per_page)

@jobs_bp.route("/jobs/<int:id>")
def view_job(id):
    job = Job.query.get_or_404(id)
    return render_template("view_job.html", job=job)

@jobs_bp.route("/jobs/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_job(id):
    job = Job.query.get_or_404(id)
    if job.user_id != current_user.id:
        return "Unauthorized", 403
    if request.method == "POST":
        data = request.form
        for key in ["title", "company_name", "location", "job_type", "description", "skills", "reference"]:
            if key in data:
                setattr(job, key, data[key])
        db.session.commit()
        return redirect(url_for("jobs.view_job", id=job.id))
    return render_template("edit_job.html", job=job)

@jobs_bp.route("/jobs/<int:id>/delete", methods=["POST"])
@login_required
def delete_job(id):
    job = Job.query.get_or_404(id)
    if job.user_id != current_user.id:
        return "Unauthorized", 403
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for("jobs.list_jobs"))


