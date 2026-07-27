import streamlit as st


def dashboard_page():

    # -----------------------------
    # Hero Section
    # -----------------------------

    st.markdown("""
    <div class="hero">
        <h1>🚀 AI Career Assistant Pro</h1>
        <p>
            Analyze resumes, match job descriptions, optimize resumes,
            generate cover letters, and prepare for interviews using
            Google Gemini AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # -----------------------------
    # Statistics
    # -----------------------------

    st.subheader("📊 Platform Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Modules", "6")

    with col2:
        st.metric("AI Features", "12+")

    with col3:
        st.metric("Reports", "PDF")

    with col4:
        st.metric("AI Model", "Gemini")

    st.markdown("---")

    # -----------------------------
    # Core Features
    # -----------------------------

    st.subheader("✨ Core Features")

    col1, col2, col3 = st.columns(3)

    features = [
        (
            "📄",
            "Resume Analysis",
            "Get ATS scores, strengths, weaknesses, technical skills, missing skills, and personalized recommendations."
        ),
        (
            "🎯",
            "Job Match",
            "Compare your resume against any job description and identify missing keywords."
        ),
        (
            "✨",
            "Resume Optimizer",
            "Rewrite resume content using ATS-friendly language and stronger action verbs."
        )
    ]

    for col, feature in zip([col1, col2, col3], features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature[0]}</div>
                <div class="feature-title">{feature[1]}</div>
                <div class="feature-desc">{feature[2]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    features2 = [
        (
            "💌",
            "Cover Letter",
            "Generate professional cover letters tailored to specific companies and job roles."
        ),
        (
            "🎤",
            "Interview Prep",
            "Practice HR, technical, AI/ML, and project-based interview questions."
        ),
        (
            "🚀",
            "Career Toolkit",
            "Generate LinkedIn summaries, recruiter emails, portfolio descriptions, and resume headlines."
        )
    ]

    for col, feature in zip([col4, col5, col6], features2):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature[0]}</div>
                <div class="feature-title">{feature[1]}</div>
                <div class="feature-desc">{feature[2]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # -----------------------------
    # Tech Stack
    # -----------------------------

    st.subheader("🛠 Technology Stack")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.info("🐍 Python")

    with tech2:
        st.info("⚡ Streamlit")

    with tech3:
        st.info("🤖 Google Gemini")

    with tech4:
        st.info("📊 ReportLab + Matplotlib")

    st.markdown("---")

    # -----------------------------
    # Quick Start
    # -----------------------------

    st.subheader("⚡ Quick Start")

    st.markdown("""
    <div class="feature-card">
    <ol>
    <li>Upload your resume (PDF).</li>
    <li>Analyze ATS Score and resume quality.</li>
    <li>Compare your resume with a Job Description.</li>
    <li>Optimize weak sections automatically.</li>
    <li>Generate a personalized Cover Letter.</li>
    <li>Prepare for interviews using AI-generated questions.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.caption(
        "Built with ❤️ using Python • Streamlit • Google Gemini AI • ReportLab • Matplotlib"
    )