from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route("/")
def home():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append({"task": task, "done": False})
    return redirect(url_for("home"))

@app.route("/done/<int:index>")
def done(index):
    if 0 <= index < len(todos):
        todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)