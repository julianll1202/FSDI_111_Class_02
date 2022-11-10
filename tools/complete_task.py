import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def complete_a_task(task_id):
    URL = "%s/%s" % (BASE_URL,task_id)

    response = requests.patch(URL)
    if response.status_code == 204:
        print("Task successfully completed")
    else:
        print("We could not complete the task")
if __name__ == "__main__":
    print("Mark one of your tasks as complete by filling out the prompt")
    task_id = input("Id: ")
    complete_a_task(task_id)