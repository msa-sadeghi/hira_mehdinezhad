import tkinter as tk
import customtkinter as ctk

# root = tk.Tk()
root = ctk.CTk()


root.title("کار با Pack")
root.geometry("300x250")

tk.Label(root, text="ردیف 1", bg="lightblue").pack(fill="x")
tk.Label(root, text="ردیف 2", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(root, text="ردیف 3", bg="lightyellow").pack(fill="x")

root.mainloop()
