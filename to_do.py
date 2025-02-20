import tkinter as tk

window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")

def add_task():
    task = task_input.get()
    if task:
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

task_input = tk.Entry(window, width=35)
task_input.pack(pady=10)

add_task_button = tk.Button(window, text="Add Task", command=add_task)
add_task_button.pack(pady=10)

task_list = tk.Listbox(window, width=50, height=10)
task_list.pack(pady=10)

remove_task_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=10)

def add_task():
    task = task_input.get()
    if task:
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

window.mainloop()
