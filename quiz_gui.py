import tkinter as tk
from tkinter import messagebox
import random
import re
import csv
import os
from question_data import questions, options, answers, G_messages, B_messages

# -- Classes to store team data and quiz data --
class Team:
    """Base class to store team information"""
    def __init__(self, name, department, members):
        self.name = name
        self.department = department
        self.members = members

class QuizResult(Team):
    """Child class that handles scoring and CSV formatting"""
    def __init__(self, name, department, members, score, total_questions):
        super().__init__(name, department, members)
        self.score = score
        self.total = total_questions
        self.percentage = int((score / total_questions) * 100)

    def get_csv_data(self):
        """Returns a dictionary formatted for CSV DictWriter"""
        return {
            "Team Name": self.name,
            "Department": self.department,
            "Members": ", ".join(self.members),
            "Score": f"{self.score}/{self.total}",
            "Percentage": f"{self.percentage}%"
        }

# -- GUI Setup --
root = tk.Tk()
root.title("Paint Quiz")
root.geometry("800x600")

BG_COLOR = "#EAF4FF"
TITLE_FONT = ("Arial", 20, "bold")
BODY_FONT = ("Arial", 12)
root.configure(bg=BG_COLOR)

# Global Variables
question_index = 0
score = 0
selected_option = tk.StringVar()

# stores results
final_result_obj = None 

def save_to_csv():
    """Saves the class-based data to a CSV file"""
    if final_result_obj is None:
        return

    filename = os.path.join(os.getcwd(), "quiz_results.csv")
    file_exists = os.path.isfile(filename)
    
    # Get data specifically from the child class method
    data = final_result_obj.get_csv_data()
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# -- Initial screen -- 
def show_welcome():
    tk.Label(root, text="Team Building Quiz", font=TITLE_FONT, bg=BG_COLOR).pack(pady=20)
    tk.Label(root, text="Enter team details to begin", font=BODY_FONT, bg=BG_COLOR).pack(pady=5)

    # Team Name Input
    team_frame = tk.Frame(root, bg=BG_COLOR)
    team_frame.pack(pady=10)
    tk.Label(team_frame, text="Team Name:", font=BODY_FONT, bg=BG_COLOR).grid(row=0, column=0, padx=5)
    team_name_entry = tk.Entry(team_frame, font=BODY_FONT, width=30)
    team_name_entry.grid(row=0, column=1, padx=5)

    # Department Dropdown
    dept_frame = tk.Frame(root, bg=BG_COLOR)
    dept_frame.pack(pady=10)
    tk.Label(dept_frame, text="Department:", font=BODY_FONT, bg=BG_COLOR).grid(row=0, column=0, padx=5)
    departments = ["R&D", "Sales", "Supply chain", "Retail", "Customer service"]
    selected_department = tk.StringVar(value=departments[0])
    dept_menu = tk.OptionMenu(dept_frame, selected_department, *departments)
    dept_menu.grid(row=0, column=1, padx=5)

    # Member Count & Dynamic Fields
    count_frame = tk.Frame(root, bg=BG_COLOR)
    count_frame.pack(pady=10)
    tk.Label(count_frame, text="Team Size:", font=BODY_FONT, bg=BG_COLOR).grid(row=0, column=0, padx=5)
    members_count = tk.IntVar(value=1)
    count_spinbox = tk.Spinbox(count_frame, from_=1, to=10, width=5, font=BODY_FONT,
                               textvariable=members_count, command=lambda: update_members_fields())
    count_spinbox.grid(row=0, column=1, padx=5)

    members_container = tk.Frame(root, bg=BG_COLOR)
    members_container.pack(pady=10)
    member_entries = []

    def update_members_fields():
        for widget in members_container.winfo_children(): widget.destroy()
        member_entries.clear()
        for i in range(members_count.get()):
            row = tk.Frame(members_container, bg=BG_COLOR)
            row.pack(pady=2)
            tk.Label(row, text=f"Member {i+1}:", font=BODY_FONT, bg=BG_COLOR).grid(row=0, column=0)
            entry = tk.Entry(row, font=BODY_FONT, width=25)
            entry.grid(row=0, column=1)
            member_entries.append(entry)

    update_members_fields()

    def start_quiz_logic():
        global team_name_val, dept_val, member_names, question_index, score
        team_name_val = team_name_entry.get().strip()
        dept_val = selected_department.get()
        member_names = [e.get().strip() for e in member_entries if e.get().strip()]
        
        if not team_name_val:
            messagebox.showwarning("Wait!", "Your team needs a name!")
            return
            
        question_index = 0
        score = 0
        show_question()

    tk.Button(root, text="Start Quiz", font=("Arial", 14, "bold"),
              command=start_quiz_logic, bg="#4CAF50", fg="black").pack(pady=20)

def show_question():
    global question_index, final_result_obj
    clear_screen()
    if question_index >= len(questions):
        # Create the QuizResult object now that the quiz is over
        final_result_obj = QuizResult(team_name_val, dept_val, member_names, score, len(questions))
        save_to_csv()
        show_results()
        return

    tk.Label(root, text=f"Question {question_index+1}", font=BODY_FONT, bg=BG_COLOR).pack(pady=10)
    tk.Label(root, text=questions[question_index], font=("Arial", 13, "bold"), wraplength=600, bg=BG_COLOR).pack(pady=15)

    selected_option.set("None")
    for i, option in enumerate(options[question_index], start=1):
        tk.Radiobutton(root, text=option, variable=selected_option, value=str(i),
                       font=BODY_FONT, bg=BG_COLOR).pack(anchor="w", padx=150)

    tk.Button(root, text="Submit Answer", font=BODY_FONT, command=check_answer).pack(pady=30)

def check_answer():
    global question_index, score
    guess = selected_option.get()
    if guess == "None":
        messagebox.showwarning("Selection Required", "Please pick an option!")
        return

    if guess == answers[question_index]:
        score += 1
        messagebox.showinfo("Correct!", random.choice(G_messages))
    else:
        messagebox.showinfo("Wrong", f"{random.choice(B_messages)}\nAnswer: {answers[question_index]}")

    question_index += 1
    show_question()

def show_results():
    clear_screen()
    tk.Label(root, text="QUIZ FINISHED", font=TITLE_FONT, bg=BG_COLOR).pack(pady=30)
    # Pulling data from the object for the final screen
    tk.Label(root, text=f"Team: {final_result_obj.name}", font=BODY_FONT, bg=BG_COLOR).pack()
    tk.Label(root, text=f"Score: {final_result_obj.percentage}%", font=("Arial", 14, "bold"), bg=BG_COLOR).pack(pady=10)
    
    tk.Button(root, text="Restart", font=BODY_FONT, command=show_welcome).pack(pady=10)
    tk.Button(root, text="Quit", font=BODY_FONT, command=root.destroy).pack()

def clear_screen():
    for widget in root.winfo_children(): widget.destroy()


if __name__ == "__main__":
    show_welcome()
    root.mainloop()