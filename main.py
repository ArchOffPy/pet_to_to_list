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


