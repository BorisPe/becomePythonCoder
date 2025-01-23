import tkinter as tk
from tkinter import ttk
from data import plan

# Define the plan


# Create the main application window
root = tk.Tk()
root.geometry("500x400")
root.title("Junior Python Developer Plan")

# Create a frame to hold the grid layout
main_frame = ttk.Frame(root)
main_frame.pack()

# Configure the grid to have 3 columns with equal weight
for col in range(3):
    main_frame.columnconfigure(col, weight=1)

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
    # Create a frame for each step
    step_frame = ttk.Frame(main_frame,borderwidth=2, relief='ridge')
    col = i % 3  # Column index (0, 1, or 2)
    row = i // 3  # Row index based on the current column
    step_frame.grid(row=row, column=col)
    # Step checkbox
    step_var = tk.BooleanVar()
    step_vars.append(step_var)
    step_checkbox = ttk.Checkbutton(
        step_frame, text=step["step"], variable=step_var, command=lambda i=i: toggle_step(i)
       
    )
    
    step_checkbox.grid(row=0, column=0, sticky="w",padx=10, pady=10)

     # Create a frame for details within each step
    details_frame = ttk.Frame(step_frame, padding="15")
    details_frame.grid(row=1, column=0, sticky="ew")
   

    for j,details in enumerate(step['details']):
        # Details checkbox

         
        detail_var = tk.BooleanVar()
        detail_vars.append(detail_var)
        detail_checkbox = ttk.Checkbutton(
            details_frame, text=details, variable=detail_var, command=lambda i=i,j=j: toggle_detail(i,j) 
       
        )
        detail_checkbox.grid(row=j, column=0, sticky="w",padx=10, pady=10)
        
   

# Run the application
root.mainloop()
