import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from database import get_db
from models import Task, TaskUpdate, TaskResponse, TaskCreate


app = FastAPI()

#get all tasks
@app.get('/tasks', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

#create task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# get one task
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# update task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated_task.title is not None:
        task.title = updated_task.title
    if updated_task.description is not None:
        task.description = updated_task.description
    if updated_task.completed is not None:
        task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task


#delete task
@app.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return task



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)




