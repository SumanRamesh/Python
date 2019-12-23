from tkinter import *
exp = ''
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

def equalpress():
    global exp
    total = str(eval(exp))
    equation.set(total)
    exp = ''

def clear():
    global exp
    exp = ''
    equation.set('')

if __name__ == '__main__':
    c = Tk()
    c.title('Simple Calculator')
    c.geometry('265x125')
    equation = StringVar()
    calculation = Entry(c, textvariable = equation)
    calculation.grid(columnspan=4 , ipadx=50)
    equation.set('Enter your expression')
    
    b1 = Button(c, text='1',command =lambda: press(1), height = 1, width = 7)
    b1.grid(column=0 , row=2)

    b2 = Button(c, text='2',command =lambda: press(2), height = 1, width = 7)
    b2.grid(column=1 , row=2)
 
    b3 = Button(c, text='3',command =lambda: press(3), height = 1, width = 7)
    b3.grid(column=2 , row=2)

    b4 = Button(c, text='4',command =lambda: press(4), height = 1, width = 7)
    b4.grid(column=0 , row=3)

    b5 = Button(c, text='5',command =lambda: press(5), height = 1, width = 7)
    b5.grid(column=1 , row=3)

    b6 = Button(c, text='6',command =lambda: press(6), height = 1, width = 7)
    b6.grid(column=2 , row=3)

    b7 = Button(c, text='7',command =lambda: press(7), height = 1, width = 7)
    b7.grid(column=0 , row=4)

    b8 = Button(c, text='8',command =lambda: press(8), height = 1, width = 7)
    b8.grid(column=1 , row=4)

    b9 = Button(c, text='9',command =lambda: press(9), height = 1, width = 7)
    b9.grid(column=2 , row=4)


    b0 = Button(c, text='0',command =lambda: press(0), height = 1, width = 7)
    b0.grid(column=0 , row=5)

    plus = Button(c, text='+',command =lambda: press('+'), height = 1, width = 7)
    plus.grid(column=3 , row=2)

    minus = Button(c, text='-',command =lambda: press('-'), height = 1, width = 7)
    minus.grid(column=3 , row=3)

    multiply = Button(c, text='*',command =lambda: press('*'), height = 1, width = 7)
    multiply.grid(column=3 , row=4)

    divide = Button(c, text='/',command =lambda: press('/'), height = 1, width = 7)
    divide.grid(column=3 , row=5)

    equal = Button(c, text='=',command =equalpress, height = 1, width = 7)
    equal.grid(column=2 , row=5)

    clear = Button(c, text='Clear',command =clear, height = 1, width = 7)
    clear.grid(column=1 , row=5)

    c.mainloop()
