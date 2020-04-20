from tkinter import *
import BasicCalculator as BC
import ScientificCalculator as SC
import BusinessAnalysis as BA

window = Tk()
window.title('Sufe-1-Scientific-Calculator')
window.geometry('500x500')

def Basic():
    BC.Basic()


def Science():
    SC.Science()


def Business():
    BA.Business()


def SpecificMath():
    pass


Button(window, text="Basic-Calculator", command=Basic, height=1, width=6).\
    grid(row=0, column=0, padx=30, pady=30, ipadx=60, ipady=60)

Button(window, text="Scientific-Calculator", command=Science, height=1, width=6).\
    grid(row=0, column=1, padx=30, pady=30, ipadx=60, ipady=60)

Button(window, text="Business-Analysis-Calculator", command=Business, height=1, width=6).\
    grid(row=1, column=0, padx=30, pady=30, ipadx=60, ipady=60)

Button(window, text="Specific-Maths-Calculator", command=None, height=1, width=6).\
    grid(row=1, column=1, padx=30, pady=30, ipadx=60, ipady=60)


window.mainloop()
