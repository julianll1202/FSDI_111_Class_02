import requests

BASE_URL = "http://127.0.0.1:5000/tasks/"

def delete_task(task_id):
    # append the url with the task id
    URL = "http://127.0.0.1:5000/tasks/" + task_id
    # make an HTTP delete request
    response = requests.delete(URL)
    if response == 204:
        print("Task was deleted succesfully")
    else:
        print("We couldn't delete your task")

if __name__ == "__main__":
    print("Delete one of your tasks by filling out the prompt")
    task_id = input("Id: ")
    delete_task(task_id)