from crewai import Agent

fetch_clients_agent = Agent(
    role="Tech News Researcher",
    goal="Fetch the most relevant and recent news related to technology for a list of target companies",
    backstory=(
        "An expert in market intelligence and tech journalism, skilled at identifying the most impactful and recent technology-related news from trusted sources."
    ),
    allow_delegation=False
)