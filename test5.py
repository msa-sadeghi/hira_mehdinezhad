import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="موقعیت دقیق", bg="lightyellow").place(x=50, y=50)
tk.Label(root, text="موقعیت نسبی", bg="lightgreen").place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
