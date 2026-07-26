import streamlit as st

from utils.pdf_reader import extract_resume_text
from utils.gemini import generate_career_content


def career_toolkit_page():

    st.title("🚀 AI Career Toolkit")

    st.write(
        "Generate professional career content using your resume."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"],
        key="career_resume"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        tool = st.selectbox(
            "Choose Career Tool",
            [
                "Recruiter Email",
                "LinkedIn About",
                "Resume Headline",
                "Portfolio Description"
            ]
        )

        company_name = ""
        job_role = ""

        if tool == "Recruiter Email":

            company_name = st.text_input(
                "Company Name"
            )

            job_role = st.text_input(
                "Job Role"
            )

        st.divider()

        if st.button("🚀 Generate"):

            with st.spinner("Generating..."):

                try:

                    result = generate_career_content(
                        resume_text,
                        tool,
                        company_name,
                        job_role
                    )

                    st.success("✅ Generated Successfully!")

                    st.text_area(
                        "Result",
                        result,
                        height=450
                    )

                    st.download_button(
                        "📄 Download",
                        result,
                        file_name=f"{tool.replace(' ','_')}.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(e)