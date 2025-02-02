import streamlit as st
from resume_parser import extract_resume_text
from skill_matcher import match_skills
import openai  # OpenAI API for AI-based suggestions

# OpenAI API Key (Replace with your key)
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_ai_suggestions(missing_skills):
    """Generate improvement suggestions using OpenAI GPT"""
    prompt = f"My resume is missing these skills: {', '.join(missing_skills)}. How can I improve my resume?"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("📄 AI-Powered Job Application Analyzer")
st.write("🔍 Upload your resume & compare it with a job description!")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Paste Job Description
job_description = st.text_area("Paste the Job Description", "")

if uploaded_file and job_description:
    # Extract Resume Text
    resume_text = extract_resume_text(uploaded_file)
    
    # Skill Matching
    matched_skills, missing_skills = match_skills(resume_text, job_description)
    
    # Display Results
    st.subheader("✅ Skills Matched")
    st.write(", ".join(matched_skills) if matched_skills else "No skills matched.")

    st.subheader("❌ Missing Skills")
    st.write(", ".join(missing_skills) if missing_skills else "Your resume is a perfect match!")

    # AI Suggestions for Improvement
    if missing_skills:
        st.subheader("💡 AI-Powered Resume Suggestions")
        ai_suggestions = generate_ai_suggestions(missing_skills)
        st.write(ai_suggestions)
