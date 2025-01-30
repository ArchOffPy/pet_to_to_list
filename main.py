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

@app.post('/tasks', response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task







