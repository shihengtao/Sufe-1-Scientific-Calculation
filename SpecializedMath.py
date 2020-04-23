from tkinter import *
from math import *
import SpecializedMathFollow as SMF


def integral(f, l, u, r):
    try:
        l = eval(str(l.get())[14:])
        u = eval(str(u.get())[14:])
        f = str(f.get())[11:]
        unit = 10000
        n = (u - l) * unit
        sum = 0
        for i in range(n):
            x = l + i / unit
            y = eval(f)
            sum += y
        sum = sum / unit

        r.set(str(sum))
    except Exception:
        r.set("the value that you input exists error!")


def clear(f, u, l, r):
    f.set("Function = ")
    u.set("Upper bound = ")
    l.set("Lower bound = ")
    r.set('')


def Tk_Integral():
    inte = Toplevel()
    inte.title('Integral-Calculator')
    inte.geometry('650x250')

    func = StringVar()
    upper = StringVar()
    upper.set("Upper bound = ")
    lower = StringVar()
    lower.set("Lower bound = ")
    result = StringVar()
    func.set("Function = ")

    temp = StringVar()
    temp.set("PLease input the function(use the parameter x) and its lower and upper bound that you want to integral:")
    Entry(inte, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    e = Entry(inte, relief=SUNKEN, textvariable=func, font=("Calibri", 20))
    e.pack(side=TOP, expand=YES, fill=BOTH)

    e = Entry(inte, relief=SUNKEN, textvariable=result, font=("Calibri", 20))
    e.pack(side=BOTTOM, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("The result of the integral is:")
    Entry(inte, relief=SUNKEN, textvariable=temp).pack(side=BOTTOM, expand=YES, fill=BOTH)

    Button(inte, text="Clear", command=lambda f=func, u=upper, l=lower, r=result: clear(f, u, l, r), height=1, width=6).\
        pack(side=BOTTOM, expand=YES, fill=BOTH)
    Button(inte, text="Complete", command=lambda f=func, u=upper, l=lower, r=result: integral(f, l, u, r), height=1, width=6).\
        pack(side=BOTTOM, expand=YES, fill=BOTH)

    e = Entry(inte, relief=SUNKEN, textvariable=lower, font=("Calibri", 20))
    e.pack(side=LEFT, expand=YES, fill=BOTH)

    e = Entry(inte, relief=SUNKEN, textvariable=upper, font=("Calibri", 20))
    e.pack(side=LEFT, expand=YES, fill=BOTH)


def SpecializedMath():
    math = Toplevel()
    math.title('Sufe-1-Specialized-Math')
    Button(math, text="Integral-Calculator", command=Tk_Integral, height=1, width=6).\
        grid(row=0, column=0, padx=20, pady=20, ipadx=40, ipady=40)

    Button(math, text="Matrix-Calculator", command=SMF.Tk_Matrix, height=1, width=6).\
        grid(row=0, column=1, padx=20, pady=20, ipadx=40, ipady=40)

    math.mainloop()
