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


@app.get("/todos/{todo_id}/edit", response_class=HTMLResponse)
async def edit_todo_form(request: Request, todo_id: str):
    found_todo = None
    for todo_item in todos:
        if str(todo_item.id) == todo_id:
            found_todo = todo_item
            break
    if not found_todo:
        # Optionally, handle not found error, e.g., redirect to list or show error page
        return RedirectResponse(url="/todos", status_code=302)
    return templates.TemplateResponse(
        request=request, name="todo-detail.html", context={"todo": found_todo}
    )


@app.post("/todos/{todo_id}/description", response_class=HTMLResponse)
async def save_todo_description(
    request: Request, todo_id: str, description: Annotated[str, Form()]
):
    found_todo = None
    for todo_item in todos:
        if str(todo_item.id) == todo_id:
            todo_item.description = description
            found_todo = todo_item
            break
    if not found_todo:
        return RedirectResponse(url="/todos", status_code=302) # Or handle error

    # Redirect back to the edit page to see the saved description
    # Alternatively, could redirect to /todos
    return RedirectResponse(url=f"/todos/{todo_id}/edit", status_code=303)


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
