import tkinter


def number1(num):
    global operation
    operation += num
    result.set(operation)

def calculation():
    global operation
    result.set(eval(operation))
    operation = ""

w = tkinter.Tk()

operation = ""

#entry
result = tkinter.StringVar("")
e1 = tkinter.Entry(w, textvariable=result)
e1.grid(row=0, column=0, padx=5, pady=5, ipadx=2, ipady=2, columnspan=4)

#button
b1 = tkinter.Button(w, text=1, command=lambda: number1("1"))
b1.grid(row=1, column=0, padx=1, pady=1, ipadx=5, ipady=5)

b2 = tkinter.Button(w, text=2, command=lambda: number1("2"))
b2.grid(row=1, column=1, padx=1, pady=1, ipadx=5, ipady=5)

b3 = tkinter.Button(w, text=3, command=lambda: number1("3"))
b3.grid(row=1, column=2, padx=1, pady=1, ipadx=5, ipady=5)

b4 = tkinter.Button(w, text=4, command=lambda: number1("4"))
b4.grid(row=2, column=0, padx=1, pady=1, ipadx=5, ipady=5)

b5 = tkinter.Button(w, text=5, command=lambda: number1("5"))
b5.grid(row=2, column=1, padx=1, pady=1, ipadx=5, ipady=5)

b6 = tkinter.Button(w, text=6, command=lambda: number1("6"))
b6.grid(row=2, column=2, padx=1, pady=1, ipadx=5, ipady=5)

b7 = tkinter.Button(w, text=7, command=lambda: number1("7"))
b7.grid(row=3, column=0, padx=1, pady=1, ipadx=5, ipady=5)

b8 = tkinter.Button(w, text=8, command=lambda: number1("8"))
b8.grid(row=3, column=1, padx=1, pady=1, ipadx=5, ipady=5)

b9 = tkinter.Button(w, text=9, command=lambda: number1("9"))
b9.grid(row=3, column=2, padx=1, pady=1, ipadx=5, ipady=5)

b0 = tkinter.Button(w, text=0, command=lambda: number1("0"))
b0.grid(row=4, column=1, padx=1, pady=1, ipadx=5, ipady=5)

bdot = tkinter.Button(w, text=".", command=lambda: number1("."))
bdot.grid(row=4, column=0,padx=1, pady=1, ipadx=5, ipady=5)

c1 = tkinter.Button(w, text="+", command=lambda: number1("+"))
c1.grid(row=1, column=3, padx=1, pady=1, ipadx=5, ipady=5)

c2 = tkinter.Button(w, text="-", command=lambda: number1("-"))
c2.grid(row=2, column=3, padx=1, pady=1, ipadx=5, ipady=5)

c3 = tkinter.Button(w, text="*", command=lambda: number1("*"))
c3.grid(row=3, column=3, padx=1, pady=1, ipadx=5, ipady=5)

c4 = tkinter.Button(w, text="/", command=lambda: number1("/"))
c4.grid(row=4, column=2, padx=1, pady=1, ipadx=5, ipady=5)

c5 = tkinter.Button(w, text="=", command=lambda: calculation())
c5.grid(row=4, column=3, padx=1, pady=1, ipadx=5, ipady=5)

w.mainloop()
