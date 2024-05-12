import tkinter as tk
from tkinter import messagebox

# Function to open a new window for entering a new claim
def open_new_claim_window():
    # Destroy any existing widgets in the window
    clear_window()

    # Display button to open agent form
    agent_form_button = tk.Button(window, text="Agent Form", command=open_claim_info_window, bg="#ADD8E6", fg="black")
    agent_form_button.pack()

# Function to open a new window for entering claim information
def open_claim_info_window():
    # Destroy any existing widgets in the window
    clear_window()

    # Display widgets for entering claim details
    claim_label = tk.Label(window, text="Enter Claim Details:", fg="black", font=("Arial", 12))
    claim_label.pack()

    claim_entry = tk.Entry(window)
    claim_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=lambda: submit_claim(claim_entry), bg="#ADD8E6", fg="black")
    submit_button.pack()

# Function to submit a claim
def submit_claim(claim_entry):
    claim_details = claim_entry.get()
    if claim_details.strip().isdigit():  # Check if input is a digit
        messagebox.showinfo("Success", "Claim submitted successfully!")
        claim_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a valid numerical value for the claim.")

# Function to clear all widgets from the window
def clear_window():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()

# Function to handle forward action
def forward_action(label):
    label.config(text="Moving forward...", fg="black")

# Function to handle back action
def back_action(label):
    label.config(text="Moving back...", fg="black")

# Function to exit the application
def exit_application():
    if messagebox.askokcancel("Exit Confirmation", "Are you sure you want to exit the application?"):
        window.destroy()

# Function to save data
def save_data():
    # Logic to save data
    messagebox.showinfo("Save", "Data saved successfully!")

# Function to clear data
def clear_data():
    # Logic to clear data
    messagebox.showinfo("Clear", "Data cleared!")

# Main window
window = tk.Tk()
window.title("False Delivery Claims Tracker")

# Welcome label
label_welcome = tk.Label(window, text="Welcome to False Delivery Claims Tracker", font=("Arial Black", 20), fg="black")
label_welcome.pack(pady=10)

# Buttons
new_claim_button = tk.Button(window, text="Enter New Claim", command=open_new_claim_window, bg="#ADD8E6", fg="black")
new_claim_button.pack(side="top", pady=5)

view_claims_button = tk.Button(window, text="View Existing Claims", bg="#ADD8E6", fg="black")  # Define function and add command later
view_claims_button.pack(side="top", pady=5)

additional_info_button = tk.Button(window, text="Additional Information", bg="#ADD8E6", fg="black")  # Define function and add command later
additional_info_button.pack(side="top", pady=5)

forward_button = tk.Button(window, text="Forward", command=lambda: forward_action(label_status), bg="#ADD8E6", fg="black")
forward_button.pack(side="left", padx=5)

back_button = tk.Button(window, text="Back", command=lambda: back_action(label_status), bg="#ADD8E6", fg="black")
back_button.pack(side="left", padx=5)

exit_button = tk.Button(window, text="Exit", command=exit_application, bg="#ADD8E6", fg="black")
exit_button.pack(side="bottom", pady=10)

# Labels
label_status = tk.Label(window, text="", font=("Arial", 12))
label_status.pack(pady=10)

label_description = tk.Label(window, text="Description:", fg="black")
label_description.pack()

label_status = tk.Label(window, text="Status:", fg="black")
label_status.pack()

# Additional buttons
button_save = tk.Button(window, text="Save", command=save_data, bg="#ADD8E6", fg="black")
button_save.pack()

button_clear = tk.Button(window, text="Clear", command=clear_data, bg="#ADD8E6", fg="black")
button_clear.pack()

window.mainloop()
