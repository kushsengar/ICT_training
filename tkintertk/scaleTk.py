import tkinter as tk

def scale_change_value(value):
    label_value.config(text=f"value: {value}")

# Creating the main app window
root = tk.Tk()
root.title("Scale Widget Example")
root.geometry("400x200")

# Creating a frame to hold the scale
frame = tk.Frame(root)
frame.pack(pady=20)  # pack the frame into the root window

# Creating the scale widget
scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=scale_change_value)
scale.pack()

# Creating and packing the label to display the value
label_value = tk.Label(root, text="value: 0")
label_value.pack(pady=10)

root.mainloop()
