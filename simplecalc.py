import tkinter as tk

def clear():
    enter.delete(0, tk.END)

def submit():
    if '+' in enter.get():
        num1, num2 = enter.get().split('+')
        ans = int(num1) + int(num2)
    elif '-' in enter.get():
        num1, num2 = enter.get().split('-')
        ans = int(num1) - int(num2)
    elif 'X' in enter.get():
        num1, num2 = enter.get().split('X')
        ans = int(num1) * int(num2)
    elif '/' in enter.get():
        num1, num2 = enter.get().split('/')
        ans = int(num1) / int(num2)
    enter.delete(0, tk.END)
    enter.insert(0, ans)

def type(n):
    enter.insert(tk.END, '')
    enter.insert(tk.END, n)

def func(i):
    if i == '+':
        enter.insert(tk.END, ' + ')
    elif i == '-':
        enter.insert(tk.END, ' - ')
    elif i == 'X':
        enter.insert(tk.END, ' X ')
    elif i == '/':
        enter.insert(tk.END, ' / ')

cal = tk.Tk()

cal.title('Simple Calculator')

enter = tk.Entry(cal)
enter.grid(row = 0, column = 0, columnspan = 4)

num1b = tk.Button(cal, text = '1', width=3, command = lambda: type(1))
num1b.grid(row = 3, column = 0)
num2b = tk.Button(cal, text = '2', width=3, command = lambda: type(2))
num2b.grid(row = 3, column = 1)
num3b = tk.Button(cal, text = '3', width=3, command = lambda: type(3))
num3b.grid(row = 3, column = 2)
num4b = tk.Button(cal, text = '4', width=3, command = lambda: type(4))
num4b.grid(row = 2, column = 0)
num5b = tk.Button(cal, text = '5', width=3, command = lambda: type(5))
num5b.grid(row = 2, column = 1)
num6b = tk.Button(cal, text = '6', width=3, command = lambda: type(6))
num6b.grid(row = 2, column = 2)
num7b = tk.Button(cal, text = '7', width=3, command = lambda: type(7))
num7b.grid(row = 1, column = 0)
num8b = tk.Button(cal, text = '8', width=3, command = lambda: type(8))
num8b.grid(row = 1, column = 1)
num9b = tk.Button(cal, text = '9', width=3, command = lambda: type(9))
num9b.grid(row = 1, column = 2)
num0b = tk.Button(cal, text = '0', width=3, command = lambda: type(0))
num0b.grid(row = 4, column = 1)

addb = tk.Button(cal, text = '+', width=3, command = lambda: func('+'))
addb.grid(row = 4, column = 3)
subb = tk.Button(cal, text = '-', width=3, command = lambda: func('-'))
subb.grid(row = 3, column = 3)
mulb = tk.Button(cal, text = 'X', width=3, command = lambda: func('X'))
mulb.grid(row = 2, column = 3)
divb = tk.Button(cal, text = '/', width=3, command = lambda: func('/'))
divb.grid(row = 1, column = 3)

equb = tk.Button(cal, text = '=', width=3, command = submit)
equb.grid(row = 4, column = 2)
clrb = tk.Button(cal, text = 'c', width=3, command = clear)
clrb.grid(row = 4, column = 0)

cal.mainloop()