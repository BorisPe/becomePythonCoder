import tkinter as tk
from tkinter import ttk
from data import plan

# Define the plan


# Create the main application window
root = tk.Tk()
root.title("Junior Python Developer Plan")

# Track completion status of steps and details
step_vars = []  # For step-level completion
detail_vars = []  # For detail-level completion

def toggle_step(index):
    """Callback to handle step completion toggling."""
    status = "Completed" if step_vars[index].get() else "Incomplete"
    print(f"Step '{plan[index]['step']}' is now {status}.")

def toggle_detail(step_index, detail_index):
    """Callback to handle detail completion toggling."""
    status = "Completed" if detail_vars[step_index][detail_index].get() else "Incomplete"
    detail_text = plan[step_index]['details'][detail_index]
    print(f"Detail '{detail_text}' is now {status}.")

# Populate the scrollable frame with steps and details
for i in plan:
    # Step checkbox
    step_var = tk.BooleanVar()
    step_vars.append(step_var)
    rows = len(step_vars)
    step_checkbox = ttk.Checkbutton(
         text=i["step"], variable=step_var, 
        command=lambda i=rows: toggle_step(i)
       
    )
    for j in i['details']:
        # Details checkbox
        detail_var = tk.BooleanVar()
        detail_vars.append(detail_var)
        detail_checkbox = ttk.Checkbutton(
             text=j, variable=detail_var, 
       
        )
        detail_checkbox.grid(row=len(i['details']), column=1)
       
   

# Run the application
root.mainloop()
