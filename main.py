import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

# Create model data
class Task(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# storage
tasks: List[Task] = []

#get all tasks
@app.get('/tasks', response_model=List[Task])
def get_tasks():
    return tasks

#create task
@app.post('/tasks', response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# get one task
@app.get('/tasks/{id}', response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

# update task
@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return {"error": "Task not found"}

#delete task
@app.delete('/tasks/{task_id}', response_model=Task)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id == task_id]
    return {"message": "Task deleted"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)




