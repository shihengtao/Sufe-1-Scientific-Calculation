from tkinter import *
from math import *


def cal(inputs, ans):
    try:
        ans.set("answer=" + str(eval(inputs.get())))
    except Exception:
        ans.set("ERROR!")


def addButton(parent, side, text, command=None):
    b = Button(parent, text=text, command=command)
    b.pack(side=side, expand=YES, fill=BOTH)
    return b


def construct(science):
    t = Text(science, height=3)
    t.pack(side=BOTTOM)
    t.insert("insert", "You can use the following symbols:\n")
    t.insert("insert", "log(); log10(); sin(); cos(); tan(); asin(); acos(); atan(); **; exp()\n")
    t.insert("insert", "And so on. More functions,please refer to the math.py!")

    temp = StringVar()
    temp.set("PLease input what you want to calculate in the following blank:")
    e = Entry(science, relief=SUNKEN, textvariable=temp)
    e.pack(side=TOP, expand=YES, fill=BOTH)

    ans = StringVar()
    inputs = StringVar()
    ans.set("answer=")

    e = Entry(science, relief=SUNKEN, textvariable=inputs, font=("Calibri",20))
    e.pack(side=TOP, expand=YES, fill=BOTH)
    r = Entry(science, relief=SUNKEN, textvariable=ans, font=("Calibri",20))
    r.pack(side=TOP, expand=YES, fill=BOTH)

    addButton(science, LEFT, 'Clear',
              lambda o=inputs: (o.set('')))
    addButton(science, LEFT, 'Del',
              lambda o=inputs: o.set(o.get()[0:-1]))
    addButton(science, LEFT, 'Complete',
              lambda o=inputs, s=ans: cal(o, s))


def Science():
    science = Toplevel()
    science.geometry('600x250')
    science.title('Sufe-1-Science-Calculator')
    construct(science)

    science.mainloop()
