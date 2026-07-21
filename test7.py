import ttkbootstrap as ttk
import tkinter as tk
import json

tasks = []


def add_item():
    print(todo_var.get())
    todos.insert(tk.END, todo_var.get())
    todo_var.set("")


def load_tasks():
    global tasks
    try:

        with open("todos.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
        print(tasks)
        for t in tasks:
            todos.insert(tk.END, t["title"])
    except:
        print("error")


root = ttk.Window(themename="superhero")  # any name from the catalog below
root.geometry("600x300")

todo_var = tk.StringVar()

f = ttk.Frame(root)
f.pack(pady=20)


todo_entry = ttk.Entry(f, textvariable=todo_var)
todo_entry.pack(side="left")
btn = ttk.Button(f, text="click me", command=add_item)
btn.pack(side="right")


f2 = ttk.Frame(root)
f2.pack(fill="both", expand=True)
scrollbar = ttk.Scrollbar(f2)
scrollbar.pack(side="right", fill="y")


todos = tk.Listbox(f2, width=70, height=10, yscrollcommand=scrollbar.set)
todos.pack(side="left", fill="both", expand=True)
scrollbar.config(command=todos.yview)

load_tasks()
root.mainloop()
