from crewai import Task

summarize_task = Task(
    description="Take as input a list of news articles returned by the fetch agent, grouped by company."
                "Extract and summarize the most relevant and important news"
                "Maintain key facts: names, dates, numbers, technologies, and partnerships. Avoid vague summaries and high-level restatements. "
                "Output format:\n"
                    "Company Name:\n"
                    "YYYY-MM-DD: [Concise yet complete summary of 1 key news item]\n"
                    "YYYY-MM-DD: [Next key item...]\n\n",
    expected_output="Most important company news in bullet format, dated, and factually detailed",
)
