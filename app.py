from flask import Flask, render_template, request
import os

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from recommendation_engine import recommend_jobs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF."

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    resume_text = extract_text_from_pdf(file_path)

    skills = extract_skills(resume_text)

    jobs = recommend_jobs(skills)

    ats_score = jobs[0]["score"] if jobs else 0

    return render_template(
        "result.html",
        filename=file.filename,
        skills=skills,
        jobs=jobs,
        ats_score=ats_score
    )


if __name__ == "__main__":
    app.run(debug=True)