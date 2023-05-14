import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


tasks_list = []

# Functions
def add_task():
    entry_val = placeholder_val.get()
    print(entry_val)








# window
window = ttk.Window(themename='darkly')
window.title("TO-DO LIST APPLICATION")
window.iconbitmap('logo_.ico')
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
s.configure('new.TLabel', background='#626262')

# Parent Setting and Label
label_heading = ttk.Label(window, 
                          text="Task List",
                          font=("arial", 20, 'underline', 'bold'), 
                          bootstyle="light")
label_heading.pack(pady=35)


frame_1 = tk.Frame(window, width=600, height=400, relief=tk.GROOVE)
frame_1.pack()

# Create the Entry or Input widgets
placeholder_val = tk.StringVar(value='  Enter task...')
task_entry = ttk.Entry(frame_1, font=("arial", 16), width=42, background='red', bootstyle="secondary", textvariable=placeholder_val)
task_entry.pack(side='left',pady=20)


# Canvas (Line)
line_separator = ttk.Separator(window, bootstyle='light')
line_separator.pack(fill='x', padx=40, pady=20)

# Section 2 Tables
frame_2 = ttk.Frame(master=window, width=650, height=400, relief=tk.GROOVE)
frame_2.pack(fill='both', expand=True)
table = ttk.Treeview(frame_2, columns=('Tasks', 'Date'), show='headings', bootstyle='light')
table.heading('Tasks', text='All Task')
table.heading('Date', text='Date added')
table.pack(fill='both', expand=True)

# Action buttons
add_btn = ttk.Button(window, bootstyle='primary', text='Add', command=add_task)
add_btn.pack(pady=10, padx=10, side='left')
delete_btn = ttk.Button(window, bootstyle='danger',text='Delete', command=add_task)
delete_btn.pack(pady=10, padx=10, side='left')
save_btn = ttk.Button(window, bootstyle='primary', text='Save', command=add_task)
save_btn.pack(pady=10, padx=10, side='left')
load_btn = ttk.Button(window, bootstyle='primary',text='Load',command=add_task)
load_btn.pack(pady=10, padx=10, side='left')










# run
window.mainloop()