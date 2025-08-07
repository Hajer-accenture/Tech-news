from crewai import Task

summarize_task = Task(
    description="Summarize each article into 3–4 bullet points"
                "Categorize news by theme and ensure each summary retains the original event’s specificity"
                "Maintain key facts: names, dates, numbers, technologies, and partnerships. Avoid vague summaries and high-level restatements. ",
    expected_output="A concise, categorized summary of Renault news with critical facts retained. Each item must have factual precision.",
)
