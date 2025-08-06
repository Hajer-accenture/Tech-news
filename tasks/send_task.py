from crewai import Task

send_task = Task(
    description="Send the final news summary via email to the user.",
    expected_output="Email format of the news summary. The email signature contains only Regards.",
)
