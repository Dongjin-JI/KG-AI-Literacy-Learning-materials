from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import database

app = FastAPI(title="todo-app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database.init_db()


class TodoCreate(BaseModel):
    title: str


@app.get("/todos")
def list_todos():
    return database.get_all_todos()


@app.post("/todos")
def create_todo(todo: TodoCreate):
    database.add_todo(todo.title)
    return {"message": "created"}


@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int):
    database.toggle_done(todo_id)
    return {"message": "updated"}


@app.delete("/todos/{todo_id}")
def remove_todo(todo_id: int):
    database.delete_todo(todo_id)
    return {"message": "deleted"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
