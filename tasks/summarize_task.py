from crewai import Task

summarize_task = Task(
    description="Summarize each article into 2–3 bullet points",
    expected_output="Formatted summary with headlines and bullet points",
)
