from flask import Flask, request;
from app.database import task

app = Flask(__name__)

@app.get("/tasks")
def get_all_tasks():
    out = {}
    response = task.scan()
    out["tasks"] = response
    return out

@app.get("/tasks/<int:id>")
def get_task(id):
    out = {}
    response = task.read(id)
    out["task"] = response
    return out

@app.post("/tasks")
def create_task():
    out = {"status":"OK"}
    task_data = request.json
    task.insert(task_data)
    # 201 status code means "succesfully created"
    return out, 201

@app.put("/tasks/<int:id>")
def update_task(id):
    task_data = request.json
    task.update(id, task_data)

    return '', 204

@app.patch("/tasks/<int:id>")
def complete_task(id):
    task.complete(id)

    return '', 204
    
@app.delete("/tasks/<int:id>")
def delete_task(id):
    task.delete(id)

    return '', 204