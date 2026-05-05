import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.resizable(False, False)

entry = tk.Entry(root, font=('Arial', 22), bd=3, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

def click(value):
    if value == "AC":
        entry.delete(0, tk.END)
    elif value == "⌫":
        entry.delete(len(entry.get())-1, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

buttons = [
    ['AC', '⌫', '/', '*'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['0', '.', '', '']
]

for i in range(6):
    root.rowconfigure(i, weight=1)

for j in range(4):
    root.columnconfigure(j, weight=1)

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        if val:
            tk.Button(
                root,
                text=val,
                font=('Arial', 14),
                bd=1,
                relief=tk.SOLID,
                command=lambda v=val: click(v)
            ).grid(row=r+1, column=c, sticky="nsew")

root.mainloop()