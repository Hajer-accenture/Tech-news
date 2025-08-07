from datetime import datetime

from crewai import Task

companies = [
    "Renault", "Airliquide", "Thales", "Naval Group",
    "Airbus", "TotalEnergies", "Valeo", "Forvia", "Stellantis"
]

fetch_clients_task = Task(
    description=(
        f"Collect all recent concrete and verifiable company news that could significantly affect a company’s strategic trajectory"
        f"published within the last month from {datetime.today()} in {datetime.today().year}"
        f"for the following companies: {', '.join(companies)}. "
        "Focus on high-impact developments related to innovation, digital transformation, R&D, AI, or other emerging technologies,"
        "finafncial events, executive leadership, or political implications"
    ),
    expected_output=(
        "For each company, a list of 4–5 detailed and recent news items. for each company, each entry must include the headline, summary, date, and source"
    )
)