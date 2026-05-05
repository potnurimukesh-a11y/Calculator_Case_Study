import tkinter as tk

root = tk.Tk()
root.geometry("450x350")
root.title("Calculator")
previous_value = ""
present_value = ""
operation = ""

def getPreviousValue(operator):
    global previous_value, present_value, operation
    
    if entry.get() == "":   # NEW CHECK
        entry.delete(0, 'end')
        entry.insert(0, "1st Variable is Not Declared")
        return

    previous_value = entry.get()
    operation = operator
    entry.delete(0, 'end')
    
    
def getAnswer():
    global previous_value, present_value, operation
    
    if previous_value == "":   # NEW CHECK
        entry.delete(0, 'end')
        entry.insert(0, "1st Variable is Not Declared")
        return

    present_value = entry.get()
    
    try:
        if operation == '+':
            result = float(previous_value) + float(present_value)
        elif operation == '-':
            result = float(previous_value) - float(present_value)
        elif operation == '*':
            result = float(previous_value) * float(present_value)
        elif operation == '/':
            if float(present_value) == 0:
                raise ZeroDivisionError
            result = float(previous_value) / float(present_value)

        entry.delete(0, 'end')
        entry.insert(0, str(result))

    except ZeroDivisionError:
        entry.delete(0, 'end')
        entry.insert(0, "Math Error")

    except ValueError:
        entry.delete(0, 'end')
        entry.insert(0, "Invalid Input")
        
        
def enterNum(num):
    oldEntry = entry.get()
    entry.delete(0, 'end')
    newEntry = oldEntry + num
    entry.insert(0, newEntry)
    
    
def allClear():
    entry.delete(0, 'end')

frame = tk.Frame(root, background="pink", width=450, height=350)
frame.pack()

entry = tk.Entry(frame, width=33, font=('Arial',16))
entry.place(x=20,y=30)

button_1 = tk.Button(frame, text = "1", width = 2, height = 1, command = lambda: enterNum('1'))
button_1.place(x = 100,y = 100)

button_2 = tk.Button(frame, text = "2", width = 2, height = 1, command = lambda: enterNum('2'))
button_2.place(x = 160,y = 100)

button_3 = tk.Button(frame, text = "3", width = 2, height = 1, command = lambda: enterNum('3'))
button_3.place(x = 220,y = 100)

button_4 = tk.Button(frame, text = "+", width = 2, height = 1, command = lambda: getPreviousValue('+'))
button_4.place(x = 280,y = 100)

button_5 = tk.Button(frame, text = "4", width = 2, height = 1, command = lambda: enterNum('4'))
button_5.place(x = 100,y = 170)

button_6 = tk.Button(frame, text = "5", width = 2, height = 1, command = lambda: enterNum('5'))
button_6.place(x = 160,y = 170)

button_7 = tk.Button(frame, text = "6", width = 2, height = 1, command = lambda: enterNum('6'))
button_7.place(x = 220,y = 170)

button_8 = tk.Button(frame, text = "-", width = 2, height = 1, command = lambda: getPreviousValue('-'))
button_8.place(x = 280,y = 170)

button_9 = tk.Button(frame, text = "7", width = 2, height = 1, command = lambda: enterNum('7'))
button_9.place(x = 100,y = 240)

button_10 = tk.Button(frame, text = "8", width = 2, height = 1, command = lambda: enterNum('8'))
button_10.place(x = 160,y = 240)

button_11 = tk.Button(frame, text = "9", width = 2, height = 1, command = lambda: enterNum('9'))
button_11.place(x = 220,y = 240)

button_12 = tk.Button(frame, text = "*", width = 2, height = 1, command = lambda: getPreviousValue('*'))
button_12.place(x = 280,y = 240)

button_13 = tk.Button(frame, text = "0", width = 2, height = 1, command = lambda: enterNum('0'))
button_13.place(x = 100,y = 310)

button_14 = tk.Button(frame, text = "=", width = 2, height = 1, command = lambda: getAnswer())
button_14.place(x = 160,y = 310)


button_15 = tk.Button(frame, text = "AC", width = 2, height = 1, command = lambda: allClear())
button_15.place(x = 220,y = 310)

button_16 = tk.Button(frame, text = "/", width = 2, height = 1, command = lambda: getPreviousValue('/'))
button_16.place(x = 280,y = 310)


frame.pack()
root.mainloop()