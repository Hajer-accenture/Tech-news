from datetime import datetime

from crewai import Task

companies = [
    "Renault", "Airliquide", "Thales", "Naval Group",
    "Airbus", "TotalEnergies", "Valeo", "Forvia", "Stellantis"
]

fetch_clients_task = Task(
    description=(
        f"Collect all recent concrete and verifiable company news published within the last 2–3 days from {datetime.today()}"
        f"for the following companies: {', '.join(companies)}. "
        "Focus on high-impact developments related to innovation, digital transformation, R&D, AI, or other emerging technologies,"
        "financial events, executive leadership, or political implications"
    ),
    expected_output=(
        "A list of 4–7 detailed and recent news items per company. Each entry must include the headline, summary, date, and source"
    )
)