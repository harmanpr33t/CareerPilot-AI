from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

JOB_DATABASE = {

    "Data Analyst":{
        "skills":"Python SQL Excel Power BI Pandas Statistics Data Analysis",
        "salary":"₹4 - ₹8 LPA"
    },

    "Data Scientist":{
        "skills":"Python Machine Learning Deep Learning SQL Pandas NumPy",
        "salary":"₹6 - ₹12 LPA"
    },

    "Python Developer":{
        "skills":"Python Flask API HTML CSS JavaScript",
        "salary":"₹5 - ₹10 LPA"
    },

    "Business Analyst":{
        "skills":"Excel SQL Tableau Power BI Communication",
        "salary":"₹5 - ₹9 LPA"
    },

    "Frontend Developer":{
        "skills":"HTML CSS JavaScript Bootstrap React",
        "salary":"₹4 - ₹8 LPA"
    },

    "Java Developer":{
        "skills":"Java SQL Spring Boot OOP",
        "salary":"₹5 - ₹10 LPA"
    },

    "Software Engineer":{
        "skills":"Python Java SQL Problem Solving Communication",
        "salary":"₹6 - ₹12 LPA"
    }

}


def recommend_jobs(skills):

    resume=" ".join(skills)

    documents=[resume]

    for job in JOB_DATABASE.values():
        documents.append(job["skills"])

    tfidf=TfidfVectorizer()

    vectors=tfidf.fit_transform(documents)

    similarity=cosine_similarity(vectors[0:1],vectors[1:]).flatten()

    jobs=[]

    for index,score in enumerate(similarity):

        job_name=list(JOB_DATABASE.keys())[index]

        jobs.append({

            "job":job_name,

            "score":round(score*100,2),

            "salary":JOB_DATABASE[job_name]["salary"]

        })

    jobs=sorted(jobs,key=lambda x:x["score"],reverse=True)

    return jobs[:5]