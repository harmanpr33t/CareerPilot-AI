import re


SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "data analysis",
    "pandas",
    "numpy",
    "matplotlib",
    "flask",
    "html",
    "css",
    "javascript",
    "java",
    "c++",
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "mysql"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))