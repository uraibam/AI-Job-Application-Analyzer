#matches skills in the resume with the job description

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download("punkt")
nltk.download("stopwords")

def preprocess_text(text):
    """Tokenize and clean text"""
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return set(words)

def match_skills(resume_text, job_description):
    """Compare resume and job description to find missing skills"""
    resume_words = preprocess_text(resume_text)
    job_words = preprocess_text(job_description)

    matched_skills = resume_words.intersection(job_words)
    missing_skills = job_words - resume_words

    return list(matched_skills), list(missing_skills)
