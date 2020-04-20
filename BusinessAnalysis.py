from tkinter import *


def Loan(money, items, interest, repayment):
    try:
        money = eval(money.get())
        items = eval(items.get())
        interest = eval(interest.get())

        base = 0
        for i in range(items):
            base += (1 + interest) ** i
        amount = (money * (1 + interest) ** items) / base
        repayment.set(str(amount)+"yuan")
    except Exception:
        repayment.set("the value that you input exists error!")


def Regression(X, y, result):
    import numpy as np
    from sklearn import linear_model

    try:
        X = eval(X.get())
        y = eval(y.get())
        X = np.asarray(X).reshape(-1, 1)
        y = np.asarray(y).reshape(-1, 1)

        regr = linear_model.LinearRegression()
        regr.fit(X, y)
        result.set("y = "+str(round(float(regr.coef_), 3))+" x + "+str(round(float(regr.intercept_), 3)))
    except Exception:
        result.set("the list that you input exists error!")


def Tk_Regression():
    Regr = Toplevel()
    Regr.title('Linear-Regression-Calculator')
    Regr.geometry('600x300')

    X_input = StringVar()
    y_input = StringVar()
    result = StringVar()

    temp = StringVar()
    temp.set("PLease input the list X (Format: [1,2,3]) in the following Entry:")
    Entry(Regr, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    e = Entry(Regr, relief=SUNKEN, textvariable=X_input, font=("Calibri", 20))
    e.pack(side=TOP, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("PLease input the list y (Format: [1,2,3]) in the following Entry:")
    Entry(Regr, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    r = Entry(Regr, relief=SUNKEN, textvariable=y_input, font=("Calibri", 20))
    r.pack(side=TOP, expand=YES, fill=BOTH)

    Entry(Regr, relief=SUNKEN, textvariable=result, font=("Calibri", 20)).pack(side=BOTTOM, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("The function that you want to figure out is:")
    Entry(Regr, relief=SUNKEN, textvariable=temp).pack(side=BOTTOM, expand=YES, fill=BOTH)

    Button(Regr, text="Complete",
           command=lambda X=X_input, y=y_input, r=result: Regression(X, y, r), height=1, width=6).\
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(Regr, text="Clear_X",
           command=lambda o=X_input: (o.set('')), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(Regr, text="Clear_y",
           command=lambda o=y_input: (o.set('')), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)

    Regr.mainloop()


def remove(m, it, i):
    m.set('')
    it.set('')
    i.set('')


def Tk_Loans():
    loans = Toplevel()
    loans.title('Loans-Calculator')
    loans.geometry('600x300')

    money = StringVar()
    items = StringVar()
    interest = StringVar()
    repayment = StringVar()

    temp = StringVar()
    temp.set("PLease input the repayment amount in the following Entry:")
    Entry(loans, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    e = Entry(loans, relief=SUNKEN, textvariable=money, font=("Calibri", 20))
    e.pack(side=TOP, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("PLease input the repayment periods in the following Entry:")
    Entry(loans, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    r = Entry(loans, relief=SUNKEN, textvariable=items, font=("Calibri", 20))
    r.pack(side=TOP, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("PLease input the interest in the following Entry:")
    Entry(loans, relief=SUNKEN, textvariable=temp).pack(side=TOP, expand=YES, fill=BOTH)

    r = Entry(loans, relief=SUNKEN, textvariable=interest, font=("Calibri", 20))
    r.pack(side=TOP, expand=YES, fill=BOTH)

    Entry(loans, relief=SUNKEN, textvariable=repayment, font=("Calibri", 20)).pack(side=BOTTOM, expand=YES, fill=BOTH)

    temp = StringVar()
    temp.set("The amount of money that you have to repay every period is:")
    Entry(loans, relief=SUNKEN, textvariable=temp).pack(side=BOTTOM, expand=YES, fill=BOTH)

    Button(loans, text="Complete",
           command=lambda m=money, it=items, i=interest, r=repayment: Loan(m, it, i, r), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)
    Button(loans, text="Clear",
           command=lambda m=money, it=items, i=interest: remove(m, it, i), height=1, width=6). \
        pack(side=LEFT, expand=YES, fill=BOTH)

    loans.mainloop()


def Business():
    business = Toplevel()
    business.title('Sufe-1-Business-Analysis')
    Button(business, text="Linear-Regression-Calculator", command=lambda b=0: Tk_Regression(), height=1, width=6).\
        grid(row=0, column=0, padx=30, pady=30, ipadx=60, ipady=60)

    Button(business, text="Loans-Calculator", command=lambda c=0: Tk_Loans(), height=1, width=6).\
        grid(row=0, column=1, padx=30, pady=30, ipadx=60, ipady=60)

    business.mainloop()
