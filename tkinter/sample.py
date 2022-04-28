import tkinter as tk

root = tk.Tk()
root.minsize(800, 600)
root.maxsize(800, 600)

title = tk.Label(parent=root, text="PyChat")
title.pack()

chat_box = tk.Frame(parent=root, width=400, height=400)
chat_box.pack()

input_box = tk.Text(parent=root, width=400, height=100)

root.mainloop()