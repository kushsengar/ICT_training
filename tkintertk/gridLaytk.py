import tkinter as tk

root = tk.Tk()
root.title("Grid Layout with different widgets")
root.geometry("500x600")

label = tk.Label(root, text="This is a Label" , bg='lightblue')


button = tk.Button(root, text="Click me!")
entry = tk.Entry(root)
text = tk.Text(root , height=5 , width=30)
checkbutton = tk.Checkbutton(root,text="check me")
radiotbutton1 = tk.Radiobutton(root , text="option 1" , value = 1)
radiotbutton2 = tk.Radiobutton(root ,text="option 2" , value = 2)

# add widgtes
label.grid(row=0, column=0 ,padx=10 , pady=10 , sticky="w" )
button.grid(row=0, column=1 , padx=10 , pady=10 , sticky= "e")
entry.grid(row=1, column=0 ,columnspan=2, padx=10 , pady=10 , sticky="ew")
text.grid(row=2, column=0 , columnspan=2 , padx=10 , pady=10 , sticky="ew")
checkbutton.grid(row=3, column=0 , padx=10 , pady=10 , sticky="w")
radiotbutton1.grid(row=3, column=1 , padx=10 , pady=10 ,sticky = "e")
radiotbutton2.grid(row=4, column=1 , padx=10 , pady=10 , sticky ="e")

#configure
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()
