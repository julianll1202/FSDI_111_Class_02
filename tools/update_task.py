import requests

BASE_URL = "http://127.0.0.1:5000/tasks/"

def update_task(task_id, title, subtitle, body):
    task_data = {
        "id": task_id,
        "title": title,
        "subtitle": subtitle,
        "body": body
    }
    # append the url with the task id
    URL = "%s%s" % (BASE_URL, task_id)
    response = requests.put(URL, json=task_data)
    if response.status_code == 204:
        print("Task correctly updated")       
    else:
        print("There was a problem updating the task")

if __name__ == "__main__":
    print("Update a task by filling out the prompts")
    task_id = input("Id: ")
    title = input("Title: ")
    subtitle = input("Subtitle: ")
    body = input("Body: ")
    update_task(task_id, title, subtitle, body)