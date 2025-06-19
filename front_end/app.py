import streamlit as st
import requests
import os

API_URL = f"http://localhost:8000/match"
st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("🔍 Resume Matcher")
st.write("Upload your resume and enter the job description to see how well you match.")

# Upload PDF resume
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

# Job description input
job_desc = st.text_area("🧾 Paste Job Description Here", height=200)

# Submit button
if st.button("Match Resume"):
    if uploaded_file is None or not job_desc.strip():
        st.warning("Please upload a resume and enter a job description.")
    else:
        with st.spinner("Matching..."):
            # Prepare API call
            files = {"resume": uploaded_file}
            data = {"job_description": job_desc}
            try:
                response = requests.post(API_URL, files=files, data=data)
                result = response.json()
                if "match_score" in result:
                    score = result["match_score"]
                    st.success(f"✅ Match Score: **{score}%**")
                    if score > 70:
                        st.balloons()
                        st.info("🎯 Excellent match!")
                    elif score > 50:
                        st.info("👍 Good match!")
                    else:
                        st.info("⚠️ Might need improvement.")
                else:
                    st.error("Something went wrong: " + result.get("error", "Unknown error"))
            except Exception as e:
                st.error(f"API error: {e}")
