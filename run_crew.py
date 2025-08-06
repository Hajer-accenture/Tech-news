from crewai import Crew
from agents.fetcher import fetcher_agent
from agents.summarizer import summarizer_agent
from agents.clients_fetcher import fetch_clients_agent
from send_email import send_email
from tasks.fetch_task import fetch_task
from tasks.summarize_task import summarize_task
from tasks.clients_fetcher_task import fetch_clients_task

# Associate tasks with agents
fetch_task.agent = fetcher_agent
summarize_task.agent = summarizer_agent
fetch_clients_task.agent = fetch_clients_agent

news_crew = Crew(
    tasks=[fetch_task, summarize_task],
    agents=[fetcher_agent, summarizer_agent],
)
clients_crew = Crew(
    tasks=[fetch_clients_task, summarize_task],
    agents=[fetch_clients_agent, summarizer_agent],
)

if __name__ == "__main__":
    news_crew.kickoff()
    summarize_task_output = summarize_task.output
    send_email(subject="Your Daily News", body=str(summarize_task_output))

    clients_crew.kickoff()
    summarize_task_output = summarize_task.output
    send_email(subject="Your Daily News", body=str(summarize_task_output))
