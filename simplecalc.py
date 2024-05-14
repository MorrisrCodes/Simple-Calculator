import tkinter as tk

cal = tk.Tk()

cal.title('Simple Calculator')

enter = tk.Entry(cal)
enter.grid(row = 0, column = 0, columnspan = 4)

num1b = tk.Button(cal, text = '1', width=3)
num1b.grid(row = 3, column = 0)
num2b = tk.Button(cal, text = '2', width=3)
num2b.grid(row = 3, column = 1)
num3b = tk.Button(cal, text = '3', width=3)
num3b.grid(row = 3, column = 2)
num4b = tk.Button(cal, text = '4', width=3)
num4b.grid(row = 2, column = 0)
num5b = tk.Button(cal, text = '5', width=3)
num5b.grid(row = 2, column = 1)
num6b = tk.Button(cal, text = '6', width=3)
num6b.grid(row = 2, column = 2)
num7b = tk.Button(cal, text = '7', width=3)
num7b.grid(row = 1, column = 0)
num8b = tk.Button(cal, text = '8', width=3)
num8b.grid(row = 1, column = 1)
num9b = tk.Button(cal, text = '9', width=3)
num9b.grid(row = 1, column = 2)
num0b = tk.Button(cal, text = '0', width=3)
num0b.grid(row = 4, column = 1)

addb = tk.Button(cal, text = '+', width=3)
addb.grid(row = 4, column = 3)
subb = tk.Button(cal, text = '-', width=3)
subb.grid(row = 3, column = 3)
mulb = tk.Button(cal, text = 'X', width=3)
mulb.grid(row = 2, column = 3)
divb = tk.Button(cal, text = '/', width=3)
divb.grid(row = 1, column = 3)

equb = tk.Button(cal, text = '=', width=3)
equb.grid(row = 4, column = 2)
clrb = tk.Button(cal, text = 'C', width=3)
clrb.grid(row = 4, column = 0)



cal.mainloop()

