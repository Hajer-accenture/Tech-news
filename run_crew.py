from crewai import Crew
from agents.fetcher import fetcher_agent
from agents.summarizer import summarizer_agent
from agents.sender import sender_agent
from send_email import send_email
from tasks.fetch_task import fetch_task
from tasks.summarize_task import summarize_task
from tasks.send_task import send_task

# Associate tasks with agents
fetch_task.agent = fetcher_agent
summarize_task.agent = summarizer_agent
send_task.agent = sender_agent

crew = Crew(
    tasks=[fetch_task, summarize_task, send_task],
    agents=[fetcher_agent, summarizer_agent, sender_agent],
)


if __name__ == "__main__":
    output = crew.kickoff()
    send_task_output = str(send_task.output)
    print(type(send_task_output))
    print(str(send_task_output))
    send_email(subject="Your Daily News", body=str("send_task_output"))
