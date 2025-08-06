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

def crew_output_to_html(crew_output):
    html = "<html><body>"
    html += "<h2>Tech News</h2>"
    html += f"<p>{crew_output.final_output}</p>"

    for task in crew_output.task_outputs:
        html += f"<h3>Task: {task.name}</h3>"
        html += f"<p><strong>Agent:</strong> {task.agent_name}</p>"
        html += f"<p>{task.output}</p><hr>"

    html += "</body></html>"
    return html

if __name__ == "__main__":
    report = crew.kickoff()
    print("*****")
    print(type(report))
    print("****")
    html_content = crew_output_to_html(report)

    send_email("Your Daily News", html_content)