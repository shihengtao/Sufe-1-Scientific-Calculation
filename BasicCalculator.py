from tkinter import *


def show(inputs, char):
    s = inputs.get()
    if s == '0':
        s = ''
    s += char
    inputs.set(s)


def cal(inputs, ans):
    try:
        ans.set("answer=" + str(eval(inputs.get())))
    except Exception:
        ans.set("ERROR!")


def addButton(parent, side, text, command=None):
    b = Button(parent, text=text, command=command)
    b.pack(side=side, expand=YES, fill=BOTH)
    return b


def addFrame(parent, side):
    f = Frame(parent)
    f.pack(side=side, expand=YES, fill=BOTH)
    return f


def construct(frame):
    ans = StringVar()
    inputs = StringVar()
    ans.set("answer=")

    e = Entry(frame, relief=SUNKEN, textvariable=inputs, font=("Calibri",20))
    e.pack(side=TOP, expand=YES, fill=BOTH)
    r = Entry(frame, relief=SUNKEN, textvariable=ans, font=("Calibri",20))
    r.pack(side=TOP, expand=YES, fill=BOTH)

    charArray = ("123+", "456-", "789*", "-0./", "%()")
    for vx in charArray:
        keyF = addFrame(frame, TOP)
        for char in vx:
            addButton(keyF, LEFT, char,
                           lambda i=inputs, a='%s' % char: show(i, a))
    addButton(keyF, LEFT, '=', lambda i=inputs, a=ans: cal(i, a))

    keyF = addFrame(frame, TOP)
    addButton(keyF, LEFT, 'Clear',
                   lambda i=inputs, a=ans: (i.set('0'), a.set('answer=')))
    addButton(keyF, LEFT, 'Del',
                   lambda i=inputs: i.set(i.get()[0:-1]))
    addButton(keyF, LEFT, 'Demo', None)

    Str = 'This is a basic calculator.'
    addButton(keyF, LEFT, 'Help', lambda a=ans: a.set(Str))

    t = Text(frame,  height=5)
    t.pack(side=BOTTOM)
    t.insert("insert", "You can write down anything you want to here:")


def Basic():
    basic = Toplevel()
    basic.title('Sufe-1-Basic-Calculator')
    frame = Frame(basic, height=10, width=1)
    construct(frame)
    frame.pack()

    basic.mainloop()
