from crewai import Task

fetch_task = Task(
    description="Fetch today's trending technology news articles",
    expected_output="List of 5 top relevant headline+link pairs",
)