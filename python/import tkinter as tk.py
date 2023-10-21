import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main application window
root = tk.Tk()
root.title("Simple UI Example")

# Create a label widget
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button widget
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# Start the main event loop
root.mainloop()
