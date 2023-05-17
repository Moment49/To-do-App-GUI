import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import datetime
import json 


# Holds all the tasks
tasks_list = []

# Event functions
def return_entry(event):
    add_check_task(tasks_list)
    focusIn_entry(event)

def focusIn_entry(event):
    # Removes the Initial Value of the string
    task_entry.delete(0, tk.END)

# Toast Notiification for Add Item
toast_error = ToastNotification(
title="Notification",
message="Sorry!!! Enter a task",
duration=1000,
bootstyle='danger',
position = (100, 110, 's'), 
alert=True,
)

# Main Functions
def add_check_task(task_list):
    """Function to check the validation and append to the list"""
    task = placeholder_val.get()
    if task != 'Enter task...' and task != '':
        # Show add toast and append to list
        time_stamp = datetime.datetime.now().strftime('%H:%M:%S')
        date_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
        toast_add.show_toast()
        task_list.append([task, date_stamp, time_stamp])
        # Insert Values to the table
        data = (task, date_stamp, time_stamp)
        table.insert(parent='',  index=tk.END,  values=data)
    else:
        # Error toast for check validation
        toast_error.show_toast()
   
def load_tasks(task_list):
    for i in range(len(task_list)):
        task = task_list[i][0]
        print(task)
        date_stamp = task_list[i][1]
        time_stamp = task_list[i][2]
        data = (task, date_stamp, time_stamp)
        table.insert(parent='',  index=tk.END, values=data)

def delete_task(task_list):
    print(task_list)
    selected_item  = table.focus()
    print(selected_item)
    for item in table.selection():
        item_del = table.item(item)['values']
        # Delete item from table (GUI)
        print(table.delete(item))
        print(item_del)
        # Check if item is in the list
        if item_del in task_list:
            # Remove item from the list
            task_list.remove(item_del)
            print(task_list)
        
    


def save_task():
    pass


# window
window = ttk.Window(themename='superhero')
window.title("TO-DO LIST APPLICATION")
window.iconbitmap('To-do-App-GUI/logo_.ico')
window.resizable(False, False)
# App width and height
app_width = 650
app_height = 600

# Screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Get the offset
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Frame Color style class
s = ttk.Style()
s.configure('new.TLabel', background='#4e4d4c')

# Section 1
# Parent Setting and Label
label_heading = ttk.Label(window, 
                          text="Task List",
                          font=("arial", 20, 'underline', 'bold'), 
                          )
label_heading.pack(pady=35)


frame_1 = tk.Frame(window, width=600, height=400, relief=tk.GROOVE)
frame_1.pack()

# Create the Entry or Input widgets
placeholder_val = tk.StringVar(value='Enter task...')
task_entry = ttk.Entry( frame_1,
                        font=("arial", 15), 
                        width=42, 
                        bootstyle="secondary", 
                        textvariable=placeholder_val,
                        style="#ffff")
task_entry.pack(side='left',pady=20)


# Canvas (Line)
line_separator = ttk.Separator(window, bootstyle='light')
line_separator.pack(fill='x', padx=40, pady=20)

# Section 2 Tables
frame_2 = ttk.Frame(master=window, width=100, height=400, relief=tk.GROOVE)
frame_2.pack(fill='both', expand=True)

table = ttk.Treeview(frame_2, show='headings', bootstyle='primary', selectmode=tk.EXTENDED)

# Table Column
table['column'] = ('Tasks', 'Date', 'Time')

# format columns
table.column("#0", width=120)
table.column("Tasks",  anchor='nw', width=200)
table.column("Date",  anchor='center')
table.column("Time", anchor='center', width=30)

table.heading("#0")
table.heading('Tasks', text='All Task', anchor='w')
table.heading('Date', text='Date Added', anchor='center')
table.heading('Time', text='Time Added', anchor='center')
table.pack(fill='both', expand=True)



# Toast Notiification for Add Item
toast_add = ToastNotification(
    title="Notification",
    message="Item has been added",
    duration=2000,
    bootstyle='light',
    position = (100, 100, 's'),    
)


# Section 3
# Action buttons
add_btn = ttk.Button(window, bootstyle='primary', width=8, text='Add', command=lambda:[add_check_task(tasks_list)])
add_btn.pack(pady=10, padx=10, side='left')
delete_btn = ttk.Button(window, bootstyle='danger',width=8, text='Delete', command=lambda:[delete_task(tasks_list)])
delete_btn.pack(pady=10, padx=10, side='left')
save_btn = ttk.Button(window, bootstyle='primary',width=8, text='Save', command=add_check_task)
save_btn.pack(pady=10, padx=10, side='left')
load_btn = ttk.Button(window, bootstyle='primary',width=8,text='Load',command = lambda:[load_tasks(tasks_list)])
load_btn.pack(pady=10, padx=10, side='left')

# Events
task_entry.bind("<FocusIn>", focusIn_entry)
task_entry.bind("<Return>", return_entry)


# run
window.mainloop()