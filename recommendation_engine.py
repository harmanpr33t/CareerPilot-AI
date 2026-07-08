from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


JOB_DATABASE = {

    "Data Analyst":
    "Python SQL Excel Power BI Pandas Statistics Data Analysis",

    "Data Scientist":
    "Python Machine Learning Deep Learning SQL Pandas NumPy",

    "Python Developer":
    "Python Flask API HTML CSS JavaScript",

    "Business Analyst":
    "Excel SQL Tableau Power BI Communication",

    "Frontend Developer":
    "HTML CSS JavaScript Bootstrap React",

    "Java Developer":
    "Java SQL Spring Boot OOP",

    "Software Engineer":
    "Python Java SQL Problem Solving Communication"
}


def recommend_jobs(skills):

    resume = " ".join(skills)

    documents = [resume] + list(JOB_DATABASE.values())

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    jobs = []

    for index, score in enumerate(similarity):

        jobs.append({
            "job": list(JOB_DATABASE.keys())[index],
            "score": round(score * 100, 2)
        })

    jobs = sorted(jobs, key=lambda x: x["score"], reverse=True)

    return jobs[:5]