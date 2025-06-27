from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Job

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/jobs", methods=["POST"])
@login_required
def create_job():
    data = request.get_json()
    job = Job(
        title=data["title"],
        company_name=data["company_name"],
        location=data["location"],
        job_type=data["job_type"],
        description=data.get("description"),
        skills=data.get("skills"),
        reference=data.get("reference", ""),
        user_id=current_user.id
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({"message": "Job posted successfully"}), 201

@jobs_bp.route("/jobs", methods=["GET"])
def get_jobs():
    page = int(request.args.get("page", 1))
    per_page = 5
    jobs = Job.query.paginate(page=page, per_page=per_page)
    return jsonify({
        "jobs": [j.to_dict() for j in jobs.items],
        "total": jobs.total,
        "page": jobs.page
    })

@jobs_bp.route("/jobs/<int:id>", methods=["GET"])
def get_job(id):
    job = Job.query.get_or_404(id)
    return jsonify(job.to_dict())

@jobs_bp.route("/jobs/<int:id>", methods=["PUT"])
@login_required
def update_job(id):
    job = Job.query.get_or_404(id)
    if job.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json()
    for key in ["title", "company_name", "location", "job_type", "description", "skills", "reference"]:
        if key in data:
            setattr(job, key, data[key])
    db.session.commit()
    return jsonify({"message": "Job updated"})

@jobs_bp.route("/jobs/<int:id>", methods=["DELETE"])
@login_required
def delete_job(id):
    job = Job.query.get_or_404(id)
    if job.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted"})


