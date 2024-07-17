import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Invalid input for password length: {e}")
        return

    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_punctuation.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Input", "Please select at least one character set")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Setting up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Setting up the background
bg_color = "#2C3E50"
root.configure(bg=bg_color)

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg=bg_color, fg="white")
title_label.pack(pady=20)

# Length input
length_frame = tk.Frame(root, bg=bg_color)
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12), bg=bg_color, fg="white")
length_label.pack(side=tk.LEFT, padx=10)
length_entry = tk.Entry(length_frame, font=("Helvetica", 12), width=5)
length_entry.pack(side=tk.LEFT)

# Checkboxes for character types
checkbox_frame = tk.Frame(root, bg=bg_color)
checkbox_frame.pack(pady=10)
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_punctuation = tk.BooleanVar()
tk.Checkbutton(checkbox_frame, text="Uppercase", variable=var_uppercase, font=("Helvetica", 10), bg=bg_color, fg="white").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Lowercase", variable=var_lowercase, font=("Helvetica", 10), bg=bg_color, fg="white").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Digits", variable=var_digits, font=("Helvetica", 10), bg=bg_color, fg="white").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Punctuation", variable=var_punctuation, font=("Helvetica", 10), bg=bg_color, fg="white").pack(side=tk.LEFT, padx=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#E74C3C", fg="white", command=generate_password)
generate_button.pack(pady=20)

# Password display
password_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
password_entry.pack(pady=10)

# Running the application
root.mainloop()