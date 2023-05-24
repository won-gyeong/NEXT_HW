const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
const inputcontent = document.querySelector("#content");

let todolists = [];

function submitAddTodo(event) {
  event.preventDefault();
  console.log("submit");
  const newtodo = { text: inputcontent.value, id: Date.now() };
  todolists.push(newtodo);
  window.localStorage.setItem("todolist", JSON.stringify(todolists));
  inputcontent.value = "";
  paintTodo(newtodo);
}

todoForm.addEventListener("submit", submitAddTodo);

function paintTodo(newtodo) {
  // const lasttodo = todolists[todolists.length -1];
  const li = document.createElement("li");
  li.id = newtodo.id;
  const span = document.createElement("span");
  const button = document.createElement("button");
  span.innerText = newtodo.text;
  button.innerText = "X";
  button.addEventListener("click", deleteTodo);

  li.appendChild(span);
  li.appendChild(button);
  todoList.appendChild(li);
}

function deleteTodo(event) {
  const li = event.target.parentElement;
  console.log(li, "확인");
  li.remove();
  todolists = todolists.filter((todolist) => todolist.id !== parseInt(li.id));
  window.localStorage.setItem("todolist", JSON.stringify(todolists));
}

todocontent = JSON.parse(localStorage.getItem("todolist"));

if (todocontent != null) {
  todolists = todocontent;
  todolists.forEach((todolist) => paintTodo(todolist));
}
