from crewai import Task

companies = [
    "Renault", "Airliquide", "Thales", "Naval Group",
    "Airbus", "TotalEnergies", "Valeo", "Forvia", "Stellantis"
]

fetch_clients_task = Task(
    description=(
        f"Search and summarize the most recent and relevant news (past 2–3 days) of 2025 "
        f"for the following companies: {', '.join(companies)}. "
        "Focus on news related to innovation, digital transformation, R&D, AI, cybersecurity, electrification, or other emerging technologies. "
        "Focus also on financial or related political news."
    ),
    expected_output=(
        "A list of bullet points (3–4 per company) summarizing key financial, political and tech-related news from the past 2–3 days (today is August 2025)"
    )
)