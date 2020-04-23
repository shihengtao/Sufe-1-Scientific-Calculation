# Following the SpecializedMath.py, mainly programming the function that
# can be used to calculate those related to matrix.

#[[1,2,3],[4,5,6],[7,8,10]]
#
from tkinter import *
import numpy as np


def Determinant(m, t):
    try:
        m = eval(str(m.get())[9:])
        m = np.mat(m)
        m = np.linalg.det(m)
        t.delete(1.0, END)
        t.insert("insert", str(m))
    except Exception:
        t.delete(1.0, END)
        t.insert("insert", "the matrix that you input exists error!")


def Eigenvalue(m, t):
    try:
        m = eval(str(m.get())[9:])
        m = np.linalg.eig(m)
        t.delete(1.0, END)
        t.insert("insert", str(m))
    except Exception:
        t.delete(1.0, END)
        t.insert("insert", "the matrix that you input exists error!")


def Inverse(m, t):
    try:
        m = eval(str(m.get())[9:])
        m = np.mat(m)
        m = np.linalg.inv(m)
        t.delete(1.0, END)
        t.insert("insert", str(m))
    except Exception:
        t.delete(1.0, END)
        t.insert("insert", "the matrix that you input exists error!")


def clear(m, t):
    m.set("Matrix = ")
    t.delete(1.0, END)


def Tk_Matrix():
    matrix = Toplevel()
    matrix.title('Matrix-Calculator')
    matrix.geometry('650x250')

    matr = StringVar()
    matr.set("Matrix = ")

    temp = StringVar()
    temp.set("PLease input the matrix ( format: [[1,2],[3,4]] ) that you want to calculate:")
    Entry(matrix, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    e = Entry(matrix, relief=SUNKEN, textvariable=matr, font=("Calibri", 20))
    e.pack(side=TOP, expand=YES, fill=BOTH)

    text = Text(matrix, height=10)
    text.pack(side=BOTTOM)

    temp = StringVar()
    temp.set("The result that you want to figure out is:")
    Entry(matrix, relief=SUNKEN, textvariable=temp).pack(side=BOTTOM, expand=YES, fill=BOTH)

    Button(matrix, text="Clear", command=lambda m=matr, t=text: clear(m, t), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(matrix, text="Determinant", command=lambda m=matr, t=text: Determinant(m, t), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(matrix, text="Eigenvalue", command=lambda m=matr, t=text: Eigenvalue(m, t), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(matrix, text="Inverse", command=lambda m=matr, t=text: Inverse(m, t), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)

    mainloop()
