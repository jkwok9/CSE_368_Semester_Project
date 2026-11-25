# CSE_368_Semester_Project
Group 23's Semester Project

## Resume Reviewer

The Streamlit prototype accepts a resume and a job description through pasted text or PDF and TXT uploads. It displays a fixed sample review and score so the team can try the interface before connecting Ollama.

## Run locally on macOS

Open the repository folder in VS Code. With Python 3.10 or later installed, run these commands in the integrated terminal after cloning the repo.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the app from the same terminal.

```sh
python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Open `http://127.0.0.1:8501` if the browser does not open automatically. Press **Control+C** in the terminal to stop the app.

In a new terminal, run `source .venv/bin/activate` before starting the app. If `requirements.txt` changes after a pull, run `python -m pip install -r requirements.txt` again.

## Ollama integration

`services/llm_service.py` exposes `analyze_resume(resume_text, job_description)` and defines the response fields in `ResumeReview`. Replace the sample implementation with the local model call. Validate its JSON response before returning it, including the required fields and an integer `match_score` between 0 and 100. Use `score_explanation` to describe how the score was generated. Raise `ConnectionError` for an unavailable model or runtime and `ValueError` for an invalid response. When the real service is connected, remove the prototype banner and rename the review heading in `app.py`.
