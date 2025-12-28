let todos = [];

function renderTodos() {
    const list = document.getElementById("todo-list");
    list.innerHTML = "";
    todos.forEach((todo, index) => {
        const li = document.createElement("li");
        const span = document.createElement("span");
        span.textContent = todo;

        const editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.className = "edit";
        editBtn.onclick = () => editTodo(index);

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.onclick = () => deleteTodo(index);

        li.appendChild(span);
        li.appendChild(editBtn);
        li.appendChild(deleteBtn);
        list.appendChild(li);
    });
}

function addTodo() {
    const input = document.getElementById("todo-input");
    const text = input.value.trim();
    if (text !== "") {
        todos.push(text);
        input.value = "";
        renderTodos();
    }
}

function editTodo(index) {
    const newText = prompt("Edit task", todos[index]);
    if (newText !== null) {
        todos[index] = newText.trim();
        renderTodos();
    }
}

function deleteTodo(index) {
    todos.splice(index, 1);
    renderTodos();
}

document.addEventListener("DOMContentLoaded", renderTodos);
