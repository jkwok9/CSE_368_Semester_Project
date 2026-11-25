# CSE_368_Semester_Project
Group 23's Semester Project

## Resume Reviewer

The Streamlit prototype accepts a resume and a job description through pasted text or PDF and TXT uploads. Right now, it only displays a fixed sample review and score so the we can try the interface before connecting Ollama.

## Run locally

Open the repository folder in VS Code. With Python 3.10 or later installed, run these commands in the integrated terminal after cloning the rep, which starts the app from the same terminal.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```


## Ollama integration

`services/llm_service.py` exposes `analyze_resume(resume_text, job_description)` and defines the response fields in `ResumeReview`. Replace the sample implementation with the local model call. Validate its JSON response before returning it, including the required fields and an integer `match_score` between 0 and 100. Use `score_explanation` to describe how the score was generated. Raise `ConnectionError` for an unavailable model or runtime and `ValueError` for an invalid response. When the real service is connected, remove the prototype banner and rename the review heading in `app.py`.
