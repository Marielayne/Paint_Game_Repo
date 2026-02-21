""" 
This GUI will quiz teams of 1 - 10 players on the topic of paint!
"""

import tkinter as tk # creates GUI 
import csv # allows read and writes to csv 

root = tk.Tk() 

root.geometry('1400x800') 
root.configure(bg='#EAF4FF') 

# -- App Title --
root.title("How well do you know your paint?")

# -- App Heading -- 
heading_label = tk.Label(
    root, text = "Team building!",
    font=('Arial', 20), 
    bg='#EAF4FF',
    fg='black'
)
heading_label.pack() 

# -- App Subheading --
subheading_label = tk.Label(
    root,
    text="Please name your team, list your players then press submit once completed to advance to next window",
    font=('Arial', 12),
    bg='#EAF4FF',
    fg='black'
)
subheading_label.pack() 

# -- Team Name Input --
name_frame = tk.Frame(root, bg='#EAF4FF') 
name_frame.pack(pady=(20, 5))

name_label = tk.Label(
    name_frame,
    text="Enter your team name:",
    font=('Arial', 12),
    bg='#EAF4FF',
    fg='black'
)
name_label.grid(row=0, column=0, padx=5)

name_entry = tk.Entry(
    name_frame,
    font=('Arial', 12),
    width=30
)
name_entry.grid(row=0, column=1, padx=5)

# -- Department Dropdown --
department_frame = tk.Frame(root, bg='#EAF4FF')
department_frame.pack(pady=10)  

department_label = tk.Label(
    department_frame,
    text="Department:",
    font=('Arial', 12),
    bg='#EAF4FF',
    fg='black'
)
department_label.grid(row=0, column=0, padx=5)

 # Options for the dropdown
departments = [
    "R&D",
    "Sales",
    "Supply chain",
    "Retail",
    "Customer service"
]

# Variable to store selected value
selected_department = tk.StringVar()
selected_department.set(departments[0]) 

department_menu = tk.OptionMenu(department_frame, selected_department, *departments)
department_menu.config(font=('Arial', 11), width=20)
department_menu.grid(row=0, column=1, padx=5) 



# -- Number of team members Selector --
count_frame = tk.Frame(root, bg='#EAF4FF')
count_frame.pack(pady=15)

count_label = tk.Label(
    count_frame,
    text="Number of team members:",
    font=('Arial', 12),
    bg='#EAF4FF'
)
count_label.grid(row=0, column=0, padx=5)

Members_count = tk.IntVar(value=1)

count_spinbox = tk.Spinbox(
    count_frame,
    from_=1,
    to=10,
    width=5,
    font=('Arial', 12),
    textvariable= Members_count,
    command=lambda: update_members_fields()
)
count_spinbox.grid(row=0, column=1, padx=5)

# -- Dynamic Team Members Fields Will Appear Here --
team_container = tk.Frame(root, bg='#EAF4FF')
team_container.pack(pady=10)

member_entries = []  


def update_members_fields():
    # Clear existing fields
    for widget in team_container.winfo_children():
        widget.destroy()

    member_entries.clear()

    # Create new fields based on selected number
    for i in range(Members_count.get()):
        row_frame = tk.Frame(team_container, bg='#EAF4FF')
        row_frame.pack(pady=3)

        label = tk.Label(
            row_frame,
            text=f"member {i+1} name:",
            font=('Arial', 12),
            bg='#EAF4FF'
        )
        label.grid(row=0, column=0, padx=5)

        entry = tk.Entry(row_frame, width=30, font=('Arial', 12))
        entry.grid(row=0, column=1, padx=5)

        member_entries.append(entry)




root.mainloop()