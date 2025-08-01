import tkinter as tk
from tkinter import PhotoImage #for app icon

#create the main window
root = tk.Tk()
root.title("My tkinter APP")
#load an image file to use as the icon 
icon = PhotoImage(file='ipsLogo.png')

#set the icon for the windor
root.iconphoto(True, icon)

root.geometry("400x300")

root.mainloop()