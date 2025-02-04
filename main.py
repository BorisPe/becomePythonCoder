import tkinter as tk
from tkinter import ttk
from data import plan
import pickle
import os



# Define the plan


# Create the main application window
root = tk.Tk()
root.geometry("1500x700")
root.title("Junior Python Developer Plan")

# Create a scrollable frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Configure the canvas and scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Súbor na uloženie stavu
SAVE_FILE = "progress.pkl"

# Načíta uložené dáta (ak existujú)
def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            return pickle.load(f)
    return {}

# Uloží aktuálny stav pri ukončení
def save_progress():
    progress = {
        "steps": [var.get() for var in step_vars],
        "details": {(i, j): var.get() for (i, j), var in detail_vars.items()},
    }
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(progress, f)


# Configure the grid to have 3 columns with equal weight
for col in range(3):
    scrollable_frame.columnconfigure(col, weight=1)

# Track completion status of steps and details
step_vars = []  # For step-level completion
detail_vars = {}  # For detail-level completion

def toggle_step(index):
    """Callback to handle step completion toggling."""
    status = "Completed" if step_vars[index].get() else "Incomplete"
   # print(f"Step '{plan[index]['step']}' is now {status}.")
    save_progress()
    

def toggle_detail(step_index, detail_index):
    """Callback to handle detail completion toggling."""
    status = "Completed" if detail_vars[step_index,detail_index].get() else "Incomplete"
    detail_text = plan[step_index]['details'][detail_index]
   # print(f"Detail '{detail_text}' is now {status}.")
    check_toggle(step_index)
    save_progress()
    

def check_toggle(step_index):
    """If are every details done set True step"""
    all_completed = all(
        detail_vars[step_index, j].get() for j in range(len(plan[step_index]["details"]))
    )
    step_vars[step_index].set(all_completed)

saved_file = load_progress() 


# Populate the scrollable frame with steps and details
for i, step in enumerate(plan):
    # Create a frame for each step
    step_frame = ttk.Frame(scrollable_frame,borderwidth=2, relief='ridge')
    col = i % 3  # Column index (0, 1, or 2)
    row = i // 3  # Row index based on the current column
    # Create a frame for each step
    step_frame = ttk.Frame(scrollable_frame, padding="10", relief="ridge", borderwidth=2)
    step_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  # Use sticky="nsew"
    # Step checkbox
    
    step_var = tk.BooleanVar(value=saved_file['steps'][i])
    step_vars.append(step_var)
    step_checkbox = ttk.Checkbutton(
        step_frame, text=step["step"], variable=step_var, state="disabled", command=lambda i=i: toggle_step(i)
       
    )
    
    step_checkbox.grid(row=0, column=0, sticky="w",padx=10, pady=10)

     # Create a frame for details within each step
    details_frame = ttk.Frame(step_frame, padding="15")
    details_frame.grid(row=1, column=0, sticky="ew")
   

    for j,details in enumerate(step['details']):
        # Details checkbox
        detail_var = tk.BooleanVar(value=saved_file['details'][i,j])
        detail_vars[i,j] = detail_var
        detail_checkbox = ttk.Checkbutton(
            details_frame, text=details, variable=detail_var, command=lambda i=i,j=j: toggle_detail(i,j) 
       
        )
        detail_checkbox.grid(row=j, column=0, sticky="w",padx=10, pady=10)
    




       
# Run the application
root.mainloop()
