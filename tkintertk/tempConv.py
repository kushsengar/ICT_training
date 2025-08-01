import tkinter as tk

root = tk.Tk()
root.title("Temperature Convertor")
root.geometry("300x200")

def convert():
    f = float(entry.get())
    c = (f - 32) * 5/9
    result.config(text=f"{c:.2f} °C")  # Show 2 decimal places

# Label
label = tk.Label(root, text="Enter temp in Fahrenheit")
label.grid(row=0, column=0, padx=10, pady=10)

# Entry
entry = tk.Entry(root, width=25)
entry.grid(row=1, column=0, padx=10)

# Result label (using grid instead of pack)
result = tk.Label(root, text="")
result.grid(row=2, column=0, pady=10)

# Button
button = tk.Button(root, text="Convert", command=convert)
button.grid(row=3, column=0, pady=10)

root.mainloop()
