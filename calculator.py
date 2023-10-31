from tkinter import *

symbol=num1=num2=NONE

def digit(num1):
    present=display['text']
    newest=present + str(num1)
    display.config(text=newest)


  
def clrscr():
    display.config(text='')

def opr(op):
    global num1,symbol
    num1=int(display['text'])
    symbol=op
    display.config(text='')

def result():
    global num1,symbol,num2
    num2=int(display['text'])
    if symbol=='+':
        display.config(text=(num1+num2))
    elif symbol=='-':
        display.config(text=(num1-num2))
    elif symbol=='*':
        display.config(text=(num1*num2))
    else:
        if num2==0:
            display.config(text='ERROR')
        else:
            display.config(text=(num1/num2))

window=Tk()
window.title("Simple Calculator")
window.geometry("328x480")
window.configure(bg='black')

display=Label(window,font=('verdana',30),text='',bg='black',fg='white')
display.grid(row=0,column=0,columnspan=10,sticky='w',pady=(55,30))

b1=Button(window,font=('verdana',14),text='1',bg='gold',fg='black',width=6,height=3,command=lambda:digit(1))
b1.grid(row=3,column=0)

b2=Button(window,font=('verdana',14),text='2',bg='gold',fg='black',width=6,height=3,command=lambda:digit(2))
b2.grid(row=3,column=1)

b3=Button(window,font=('verdana',14),text='3',bg='gold',fg='black',width=6,height=3,command=lambda:digit(3))
b3.grid(row=3,column=2)

b_mul=Button(window,font=('verdana',14),text='*',bg='skyblue',fg='black',width=6,height=3,command=lambda:opr('*'))
b_mul.grid(row=4,column=3)

b4=Button(window,font=('verdana',14),text='4',bg='gold',fg='black',width=6,height=3,command=lambda:digit(4))
b4.grid(row=2,column=0)

b5=Button(window,font=('verdana',14),text='5',bg='gold',fg='black',width=6,height=3,command=lambda:digit(5))
b5.grid(row=2,column=1)

b6=Button(window,font=('verdana',14),text='6',bg='gold',fg='black',width=6,height=3,command=lambda:digit(6))
b6.grid(row=2,column=2)

b_substraction=Button(window,font=('verdana',14),text='-',bg='skyblue',fg='black',width=6,height=3,command=lambda:opr('-'))
b_substraction.grid(row=3,column=3)

b7=Button(window,font=('verdana',14),text='7',bg='gold',fg='black',width=6,height=3,command=lambda:digit(7))
b7.grid(row=1,column=0)

b8=Button(window,font=('verdana',14),text='8',bg='gold',fg='black',width=6,height=3,command=lambda:digit(8))
b8.grid(row=1,column=1)

b9=Button(window,font=('verdana',14),text='9',bg='gold',fg='black',width=6,height=3,command=lambda:digit(9))
b9.grid(row=1,column=2)

b_addition=Button(window,font=('verdana',14),text='+',bg='skyblue',fg='black',width=6,height=3,command=lambda:opr('+'))
b_addition.grid(row=2,column=3)

b0=Button(window,font=('verdana',14),text='0',bg='gold',fg='black',width=6,height=3,command=lambda:digit(0))
b0.grid(row=4,column=0)

bc=Button(window,font=('verdana',14),text='AC',bg='orange',fg='black',width=6,height=3,command=lambda:clrscr())
bc.grid(row=1,column=3)

b_eql=Button(window,font=('verdana',14),text='=',bg='skyblue',fg='black',width=6,height=3,command=lambda:result())
b_eql.grid(row=4,column=1)

b_div=Button(window,font=('verdana',14),text='/',bg='skyblue',fg='black',width=6,height=3,command=lambda:opr('/'))
b_div.grid(row=4,column=2)

window.mainloop()