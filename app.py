import streamlit as st

from services.llm_service import ResumeReview, analyze_resume
from utils.file_parser import extract_text


def document_input(label: str, key: str) -> str:
    st.subheader(label)
    method = st.radio(
        f"{label} input method",
        ("Paste text", "Upload a file"),
        horizontal=True,
        key=f"{key}_method",
    )
    if method == "Paste text":
        return st.text_area(f"{label} text", height=200, key=f"{key}_text").strip()

    upload = st.file_uploader(f"Upload {label.lower()}", type=["pdf", "txt"], key=f"{key}_file")
    if upload is None:
        return ""

    try:
        text = extract_text(upload.name, upload.getvalue())
    except ValueError as error:
        st.error(str(error))
        return ""

    st.text_area(f"{label} extracted text", value=text, height=200, disabled=True)
    return text


def show_review(review: ResumeReview) -> None:
    st.header("Sample review")
    st.metric("Approximate match score", f"{review['match_score']}/100")
    st.text(review["score_explanation"])
    st.caption("A match score estimates alignment with a job description. It does not predict hiring outcomes.")

    st.subheader("Overall assessment")
    st.text(review["overall_assessment"])

    sections = (
        ("Matching skills", review["matching_skills"]),
        ("Missing or unclear qualifications", review["missing_qualifications"]),
        ("Relevant experience and projects", review["relevant_experience"]),
        ("Improvement recommendations", review["recommendations"]),
        ("Suggested keywords", review["suggested_keywords"]),
    )
    for title, items in sections:
        st.subheader(title)
        if items:
            for item in items:
                st.text(f"• {item}")
        else:
            st.caption("No items identified.")


def main() -> None:
    st.set_page_config(page_title="Resume Reviewer", layout="wide")
    st.title("Resume Reviewer")
    st.info("Prototype mode displays the same sample review for every pair of inputs.")

    resume_column, job_column = st.columns(2)
    with resume_column:
        resume_text = document_input("Resume", "resume")
    with job_column:
        job_description = document_input("Job description", "job")

    inputs = (resume_text, job_description)
    if st.session_state.get("review_inputs") != inputs:
        st.session_state.pop("review", None)
        st.session_state.pop("review_inputs", None)

    ready = all(inputs)
    if not ready:
        st.caption("Provide a resume and a job description to enable review.")
    if st.button("Review resume", type="primary", disabled=not ready):
        st.session_state.pop("review", None)
        try:
            with st.spinner("Preparing review…"):
                review = analyze_resume(resume_text, job_description)
        except ConnectionError:
            st.error("The local model is unavailable. Start Ollama and check that the model is installed.")
        except ValueError:
            st.error("Could not prepare a valid review. Check the inputs and try again.")
        else:
            st.session_state["review"] = review
            st.session_state["review_inputs"] = inputs

    if "review" in st.session_state:
        show_review(st.session_state["review"])


if __name__ == "__main__":
    main()
