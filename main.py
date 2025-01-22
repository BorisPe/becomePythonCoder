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
    status = "Completed" if detail_vars[detail_index].get() else "Incomplete"
    detail_text = plan[step_index]['details'][detail_index]
    print(f"Detail '{detail_text}' is now {status}.")

# Populate the scrollable frame with steps and details
for i, step in enumerate(plan):
    # Step checkbox
    step_var = tk.BooleanVar()
    step_vars.append(step_var)
    step_checkbox = ttk.Checkbutton(
         text=step["step"], variable=step_var, command=lambda i=i: toggle_step(i)
       
    )
    print(step_var)
    step_checkbox.grid(row=i, column=1)


    for j,details in enumerate(step['details']):
        # Details checkbox
        detail_var = tk.BooleanVar()
        detail_vars.append(detail_var)
        detail_checkbox = ttk.Checkbutton(
             text=details, variable=detail_var, command=lambda i=i,j=j: toggle_detail(i,j) 
       
        )
        detail_checkbox.grid(row=j+i, column=2)
       
   

# Run the application
root.mainloop()
