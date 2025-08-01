import tkinter as tk

#create the main window
#below are the elements we are providing
root = tk.Tk()
root.title("My GUI App") # calling  method of tkinter
root.geometry("300x200") # window size in pixels
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=lambda: print("Clicked!"))
button.pack(pady=20)
#run the main event loop
root.mainloop() #should be the last line of code
