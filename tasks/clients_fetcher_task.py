from crewai import Task

companies = [
    "Renault", "Airliquide", "Thales", "Naval Group",
    "Airbus", "TotalEnergies", "Valeo", "Forvia", "Stellantis"
]

fetch_clients_task = Task(
    description=(
        f"Collect all relevant company news published within the last 2–3 days from today 06 August 2025"
        f"for the following companies: {', '.join(companies)}. "
        "Prioritize topics related to innovation, digital transformation, R&D, AI, cybersecurity, electrification, or other emerging technologies. "
        "Include items like leadership changes, investor or market reactions, regulatory shifts, and strategic updates."
    ),
    expected_output=(
        "A list of bullet points of key financial, political and tech-related news from the past 2–3 days from today 06 August 2025"
    )
)