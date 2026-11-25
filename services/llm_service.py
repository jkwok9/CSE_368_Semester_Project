from typing import TypedDict


class ResumeReview(TypedDict):
    overall_assessment: str
    matching_skills: list[str]
    missing_qualifications: list[str]
    relevant_experience: list[str]
    recommendations: list[str]
    suggested_keywords: list[str]
    match_score: int
    score_explanation: str


def analyze_resume(resume_text: str, job_description: str) -> ResumeReview:
    """Return a fixed sample review for two nonempty inputs.

    The Ollama implementation should raise ConnectionError when the local
    service or model is unavailable and ValueError for an invalid response.
    """
    if not resume_text.strip() or not job_description.strip():
        raise ValueError("Provide both a resume and a job description.")

    return {
        "overall_assessment": (
            "The example résumé shows Python and SQL project work relevant to a data analyst role. "
            "It gives limited detail about dashboards and sharing findings."
        ),
        "matching_skills": ["Python for data cleaning", "SQL for querying and aggregating data"],
        "missing_qualifications": [
            "Dashboard experience is unclear.",
            "The résumé gives no example of presenting findings to stakeholders.",
        ],
        "relevant_experience": [
            "A course project analyzed a public transit dataset using Python and SQL."
        ],
        "recommendations": [
            "Describe what the project found and how you checked the data quality.",
            "If you presented the findings, name the audience and what you shared.",
        ],
        "suggested_keywords": ["Python", "SQL", "Data cleaning", "Exploratory data analysis"],
        "match_score": 72,
        "score_explanation": "The prototype uses a fixed score of 72 to demonstrate this screen.",
    }
