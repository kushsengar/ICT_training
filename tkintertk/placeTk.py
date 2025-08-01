import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root , text="Label-1" , bg = "blue")
label1.place(x=50,y=55)

label2 = tk.Label(root,text='Label-2' , bg = "red")
label2.place(x=100,y=55)

root.mainloop()