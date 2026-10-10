from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SaaS Connector")

class Task(BaseModel):
    id: int
    title: str
    status: str = "open"

tasks_db = []

@app.get("/")
def health():
    return {"status": "Backend Running"}

@app.post("/tasks/")
def create_task(task: Task):
    tasks_db.append(task)
    return task

@app.get("/tasks/")
def get_tasks():
    return tasks_db
