
## FastAPI HTMX Todo App

This repository features a straightforward Todo List application developed using FastAPI and HTMX. It showcases how to dynamically create, update, and delete todo items without requiring a page refresh. FastAPI powers the backend, while HTMX handles AJAX requests and DOM updates. The primary goal is to provide a concise proof of concept demonstrating the effective combination of these two technologies.

### Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **HTMX**: A library that allows you to access AJAX, CSS Transitions, WebSockets, and Server-Sent Events directly in HTML, using attributes.
- **Jinja2 Templating**: For rendering HTML templates.
- **Dynamic Updates**: Add, update, and delete todo items without refreshing the page.
- **Reordering**: Automatically reorders todos to place completed items at the end.

### Getting Started

#### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fastapi-htmx-todo-list.git
   cd fastapi-htmx-todo-list
   ```

2. **Use docker :)**:
   ```bash
   docker compose up --build
   ```

5. **Open your browser** and navigate to `http://127.0.0.1:8000/` to see the TODO application in action.

### Project Structure

```
fastapi-htmx-todo-list/
│
├── main.py                # Main application file
├── models/
│   └── Todo.py            # Todo model
├── templates/
│   ├── todos.html         # Main todos template
│   └── todo-list.html     # Partial template for todo list
├── fixtures/
│   └── Todo.py            # Dummy fixtures if needed
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the MIT License.
