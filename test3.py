import tkinter as tk

root = tk.Tk()
root.title("کار با Grid")
root.geometry("300x150")

tk.Label(root, text="نام:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="نام خانوادگی:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="ثبت").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
