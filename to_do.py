import json
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")

tasks = []

def add_task():
    global counter

    task = task_input.get()
    if task:
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)
        tasks.append(task)

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        del tasks[selected_task_index]
    except IndexError:
        pass

def save():

    date = date_entry.get()

    if len(tasks) == 0:
        messagebox.showinfo(title="Yel3an 3omar", message="Please make sure you haven't left the date empty, or you didn't add any task.\nYel3an Abo Baker.")
    elif len(date) == 0:
        messagebox.showinfo(title="Yel3an 3omar", message="Please make sure you haven't left the date empty, or you didn't add any task.\nYel3an Abo Baker.")
    else:
        with open("data.txt", mode="a") as file:
            file.write(f"{date} | {tasks}\n")
            date_entry.delete(0, tk.END)
            task_list.delete(0, tk.END)
            del tasks[:]

date_entry = tk.Entry(window, width=10)
date_entry.pack(pady=10)

task_input = tk.Entry(window, width=50)
task_input.pack(pady=10)

add_task_button = tk.Button(window, width=30, text="Add Task", command=add_task)
add_task_button.pack(pady=10)

task_list = tk.Listbox(window, width=50, height=10)
task_list.pack(pady=10)

remove_task_button = tk.Button(window, width=30, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=10)

save_button = tk.Button(window, width=30, text="Save", command=save)
save_button.pack(pady=10)

window.mainloop()
