import tkinter as tk

root = tk.Tk()
root.title("KM")
root.geometry("400x200")

label = tk.Label(root, text="Hello World!").pack(pady=60)

button = tk.Button(root, text="Bye bye", command=root.destroy).pack()

root.mainloop()