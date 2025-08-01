import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root , text="Label-1" , bg = "blue")
label1.pack(fill=tk.BOTH , expand=True)

label2 = tk.Label(root,text='Label-2' , bg = "red")
label2.pack(fill=tk.BOTH , expand=True)

root.mainloop()