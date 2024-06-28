import tkinter as tk

#Global declare the expression variable
expression = ""

#Create press function in the expression_field
def press(num):
    global expression
    expression = expression+str(num)

    #update express
    equation.set(expression)

def clear():
    global expression
    expression =""
    equation.set("")

def equalpress():
    try:
        global expression
        total =str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression =""

def percent():
    try:
        global expression
        result = str(eval(expression + "/100"))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""
    
def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def CE():
    global expression
    expression = expression[:-3]
    equation.set(expression)


app = tk.Tk()

#set Background color of GUI Window
app.configure(background="light blue")

#set title
app.title("Simple Calulator")


#Set size of window
app.geometry("370x500")

equation = tk.StringVar()

#Create TextBox for expression
expression_field = tk.Entry(app, textvariable=equation,bg="pink",font=('Arial 20'),width=24,justify="right",relief="solid").grid(columnspan=4)

#Create Button Nameber
#li ne Operator Button 
btnPercent= tk.Button(app,text="%", bg="wheat",command=lambda: percent(),heigh=2,width=11,borderwidth=5).grid(row=3, column=0)
btnCE = tk.Button(app,text="CE", bg="wheat",command=lambda: CE(),heigh=2,width=11,borderwidth=5).grid(row=3, column=1)
btnC = tk.Button(app,text="C", bg="wheat",command=lambda: clear(),heigh=2,width=11,borderwidth=5).grid(row=3, column=2)
btnDelete = tk.Button(app,text="<-", bg="wheat",command=lambda: delete(),heigh=2,width=11,borderwidth=5).grid(row=3, column=3)


#line Number 7-9,X
btn7 = tk.Button(app,text="7", bg="orange",command=lambda: press(7),heigh=2,width=11,borderwidth=5).grid(row=4, column=0)
btn8 = tk.Button(app,text="8", bg="orange",command=lambda: press(8),heigh=2,width=11,borderwidth=5).grid(row=4, column=1)
btn9 = tk.Button(app,text="9", bg="orange",command=lambda: press(9),heigh=2,width=11,borderwidth=5).grid(row=4, column=2)
btnMultiplied = tk.Button(app,text="x", bg="pink",command=lambda: press('*'),heigh=2,width=11,borderwidth=5).grid(row=4, column=3)

#line Number 4-6,-
btn4 = tk.Button(app,text="4", bg="orange",command=lambda: press(4),heigh=2,width=11,borderwidth=5).grid(row=5, column=0)
btn5 = tk.Button(app,text="5", bg="orange",command=lambda: press(5),heigh=2,width=11,borderwidth=5).grid(row=5, column=1)
btn6 = tk.Button(app,text="6", bg="orange",command=lambda: press(6),heigh=2,width=11,borderwidth=5).grid(row=5, column=2)
btnMinus = tk.Button(app,text="-", bg="pink",command=lambda: press('-'),heigh=2,width=11,borderwidth=5).grid(row=5, column=3)

#line Number 1-3,+
btn1 = tk.Button(app,text="1", bg="orange",command=lambda: press(1),heigh=2,width=11,borderwidth=5).grid(row=6, column=0)
btn2 = tk.Button(app,text="2", bg="orange",command=lambda: press(2),heigh=2,width=11,borderwidth=5).grid(row=6, column=1)
btn3 = tk.Button(app,text="3", bg="orange",command=lambda: press(3),heigh=2,width=11,borderwidth=5).grid(row=6, column=2)
btnPlus = tk.Button(app,text="+", bg="pink",command=lambda: press('+'),heigh=2,width=11,borderwidth=5).grid(row=6, column=3)

#link Nume /,0,.,=
btnDivide = tk.Button(app,text="/", bg="pink",command=lambda: press('/'),heigh=2,width=11,borderwidth=5).grid(row=7, column=0)
btn0 = tk.Button(app,text="0", bg="orange",command=lambda: press(0),heigh=2,width=11,borderwidth=5).grid(row=7, column=1)
btnDecimal = tk.Button(app,text=".", bg="pink",command=lambda: press('.'),heigh=2,width=11,borderwidth=5).grid(row=7, column=2)
btnEqua = tk.Button(app,text="=", bg="wheat",command=lambda: equalpress(),heigh=2,width=11,borderwidth=5).grid(row=7, column=3)






app.mainloop()
