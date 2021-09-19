import tkinter
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Calculator')
window.geometry('350x450')
window.resizable(0,0)

value =""
A = 0
operator=""
data= StringVar()

def result():
    global A
    global operator
    global value
    value2 = value

    if operator == "+":
        x=int((value2.split("+")[1]))
        c = A + x
        data.set(c)
        value=str(c)
    elif operator == "-":
        x=int((value2.split("-")[1]))
        c = A - x
        data.set(c)
        value=str(c)
    elif operator == "*":
        x=int((value2.split("*")[1]))
        c = A * x
        data.set(c)
        value=str(c)
    elif operator == "/":
        x=int((value2.split("/")[1]))
        if x==0:
            messagebox.show("Cant divide by 0")
            A==""
            value=""
            data.set(value)
        else:    
            c = int(A / x)
            data.set(c)
            value=str(c)

def clear_clicked():
    global A
    global operator
    global value
    value = ""
    A = 0
    operator = ""
    data.set(value)

def button_add_clicked():
    global A
    global operator
    global value
    A = int(value)
    operator = "+"
    value = value + "+"
    data.set(value)

def button_subtract_clicked():
    global A
    global operator
    global value
    A = int(value)
    operator = "-"
    value = value + "-"
    data.set(value)

def button_mul_clicked():
    global A
    global operator
    global value
    A = int(value)
    operator = "*"
    value = value + "*"
    data.set(value)
    
def button_div_clicked():
    global A
    global operator
    global value
    A = int(value)
    operator = "/"
    value = value + "/"
    data.set(value)
    
def btn_equal_clicked():
    global A
    global operator
    global value
    A = int(value)
    operator = "="
    value = value + "="
    data.set(value)

def button1_clicked():
    global value
    value = value + "1"
    data.set(value)

def button2_clicked():
    global value
    value = value + "2"
    data.set(value)

def button3_clicked():
    global value
    value = value + "3"
    data.set(value)

def button4_clicked():
    global value
    value = value + "4"
    data.set(value)

def button5_clicked():
    global value
    value = value + "5"
    data.set(value)

def button6_clicked():
    global value
    value = value + "6"
    data.set(value)

def button7_clicked():
    global value
    value = value + "7"
    data.set(value)

def button8_clicked():
    global value
    value = value + "8"
    data.set(value)

def button9_clicked():
    global value
    value = value + "9"
    data.set(value)


calculator_display = Label(window, textvariable=data,bd=5, width=40,height=5, bg="light cyan")
calculator_display.place(x=10, y=20)

button_one = Button(window, text = "1",bd='15',command=button1_clicked)
button_one.place(x=30, y=350)

button_two = Button(window, text = "2",bd='15',command=button2_clicked)
button_two.place(x=100, y=350)

button_three = Button(window, text = "3",bd='15',command=button3_clicked)
button_three.place(x=170, y=350)

button_four = Button(window, text = "4",bd='15',command=button4_clicked)
button_four.place(x=30, y=280)

button_five = Button(window, text = "5",bd='15',command=button5_clicked)
button_five.place(x=100, y=280)

button_six = Button(window, text = "6",bd='15',command=button6_clicked)
button_six.place(x=170, y=280)

button_seven = Button(window, text = "7",bd='15',command=button7_clicked)
button_seven.place(x=30, y=210)

button_eight = Button(window, text = "8",bd='15',command=button8_clicked)
button_eight.place(x=100, y=210)

button_nine = Button(window, text = "9",bd='15',command=button9_clicked)
button_nine.place(x=170, y=210)

button_add = Button(window, text = "+",bd='15',command=button_add_clicked)
button_add.place(x=260, y=350)

button_subtract = Button(window, text = "-",bd='15',command=button_subtract_clicked)
button_subtract.place(x=260, y=280)

button_multiply = Button(window, text = "x",bd='15',command=button_mul_clicked)
button_multiply.place(x=260, y=210)

button_divide = Button(window, text = "/",bd='15',command=button_div_clicked)
button_divide.place(x=260, y=140)

button_procent = Button(window, text = "%",bd='13',command=window.destroy)
button_procent.place(x=190, y=140)

button_clear = Button(window, text = "Clear",bd='17',command=clear_clicked)
button_clear.place(x=30, y=140)

button_equal = Button(window, text = "=",bd='13',command=result)
button_equal.place(x=125, y=140)


window.mainloop()