from typing import Annotated, Union

from fastapi import FastAPI, Form, Header, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.Todo import Todo

app = FastAPI()

templates = Jinja2Templates(directory="templates")

todos = []

@app.get("/", response_class=HTMLResponse)
async def request(request: Request):
    return RedirectResponse(url="/todos")


@app.get("/todos", response_class=HTMLResponse)
async def list_todos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="todos.html",
        context={"todos": sorted(todos, key=lambda todo: todo.done)},
    )


@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, todo: Annotated[str, Form()]):
    todos.append(Todo(todo))
    return templates.TemplateResponse(
        request=request,
        name="todo-list.html",
        context={"todos": sorted(todos, key=lambda todo: todo.done)},
    )


@app.put("/todos/{todo_id}", response_class=HTMLResponse)
async def update_todo(request: Request, todo_id: str, text: Annotated[str, Form()]):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todo.title = text
            break
    return templates.TemplateResponse(
        request=request,
        name="todo-list.html",
        context={"todos": sorted(todos, key=lambda todo: todo.done), "updated": True},
    )


@app.post("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todos[index].done = not todos[index].done
            break
    return templates.TemplateResponse(
        request=request,
        name="todo-list.html",
        context={"todos": sorted(todos, key=lambda todo: todo.done)},
    )


@app.post("/todos/{todo_id}/delete", response_class=HTMLResponse)
async def delete_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            del todos[index]
            break
    return templates.TemplateResponse(
        request=request,
        name="todo-list.html",
        context={"todos": sorted(todos, key=lambda todo: todo.done)},
    )
