from tkinter import *
import tkinter.messagebox
import math


root = Tk()
root.geometry("500x500")
root.title("Scientific Calculator")

switch = None

#Button Function

def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnplus_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnminus_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnmultiply_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btndivide_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnclear_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def sin_clicked():
    ans = float(disp.get())
    if switch is True:
        ans = math.sin(math.radians(ans))
    else:
        ans = math.sin(ans)
    disp.delete(0, END)
    disp.insert(0, str(ans))


def cos_clicked():

        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))



def tan_clicked():

        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def arcsin_clicked():

        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))



def arccos_clicked():

        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def arctan_clicked():

        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def power_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def roundup_clicked():

        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def logarithm_clicked():

        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))

def fact_clicked():

        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def sqrt_clicked():

        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def left_parenthesis_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


def right_parenthesis_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"


def ln_clicked():

        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))

def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btneq_clicked(*args):

        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)


# Label

data = StringVar()

disp = Entry(root, font="Verdana 20", fg="black", bg="#abbab1", bd=10, justify=RIGHT, insertbackground="#abbab1", background = "#88cc00",  cursor="arrow")

disp.insert(0, '0')
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow1, text="Rad", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=conv_clicked, fg="white", bg="#333333", width = 2)
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqrt_btn = Button(btnrow1, text=" √x ", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=sqrt_clicked, fg="white", bg="#333333", width = 2)
sqrt_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

left_parenthesis_btn = Button(btnrow1, text=" ( ",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=left_parenthesis_clicked, fg="white", bg="#333333", width = 2)
left_parenthesis_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

right_parenthesis_btn = Button(btnrow1, text=" ) ",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=right_parenthesis_clicked, fg="white", bg="#333333", width = 2)
right_parenthesis_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnclear = Button(btnrow1, text="C",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btnclear_clicked, fg="white", bg="#333333", width = 2)
btnclear.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow1, text="⌫", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=del_clicked, fg="white", bg="#333333", width = 7)
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)




# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)


pi_btn = Button(btnrow2, text="π", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=pi_clicked, fg="white", bg="#333333", width = 3)
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow2, text="sin", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=sin_clicked, fg="white", bg="#333333", width = 3)
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow2, text="cos", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=cos_clicked, fg="white", bg="#333333", width = 3)
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow2, text="tan", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=tan_clicked, fg="white", bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow2, text="7", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn7_clicked, fg="white", bg="#333333", width = 3)
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow2, text="8", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn8_clicked, fg="white", bg="#333333", width = 3)
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow2, text="9", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn9_clicked, fg="white", bg="#333333", width = 3)
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btndivide = Button(btnrow2, text="/", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btndivide_clicked, fg="white", bg="#333333", width = 3)
btndivide.pack(side=LEFT, expand=TRUE, fill=BOTH)





# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow3, text="e", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=e_clicked, fg="white", bg="#333333", width = 3)
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow3, text="sin−1", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=arcsin_clicked, fg="white", bg="#333333", width = 3)
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow3, text="cos-1",  font=("Times New Roman", 12," bold"),relief=GROOVE, bd=5, command=arccos_clicked, fg="white", bg="#333333", width = 3)
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow3, text="tan-1",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=arctan_clicked, fg="white", bg="#333333", width = 3)
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow3, text="4", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn4_clicked, fg="white", bg="#333333", width = 3)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow3, text="5",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn5_clicked, fg="white", bg="#333333", width = 3)
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow3, text="6", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn6_clicked, fg="white", bg="#333333", width = 3)
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnmultipy = Button(btnrow3, text="*", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=btnmultiply_clicked, fg="white", bg="#333333", width = 3)
btnmultipy.pack(side=LEFT, expand=TRUE, fill=BOTH)








# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow4, text=" x! ",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=fact_clicked, fg="white", bg="#333333", width = 3)
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


round_btn = Button(btnrow4, text="round", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=roundup_clicked, fg="white", bg="#333333", width = 3)
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


ln_btn = Button(btnrow4, text="ln",  font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=ln_clicked, fg="white", bg="#333333", width = 3)
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow4, text="log",  font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=logarithm_clicked, fg="white", bg="#333333", width = 3)
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn1 = Button(btnrow4, text="1", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=btn1_clicked, fg="white", bg="#333333", width = 3)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow4, text="2", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5,  command=btn2_clicked, fg="white", bg="#333333", width = 3)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow4, text="3", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=btn3_clicked, fg="white", bg="#333333", width = 3)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnminus = Button(btnrow4, text="-", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=btnminus_clicked, fg="white", bg="#333333" ,width = 3)
btnminus.pack(side=LEFT, expand=TRUE, fill=BOTH)


btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

power_btn = Button(btnrow5, text="x^y", font=("Times New Roman", 12," bold"),relief=GROOVE, bd=5, command=power_clicked, fg="white", bg="#333333" , width = 2)
power_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


mod_btn = Button(btnrow5, text="%",  font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=mod_clicked, fg="white", bg="#333333", width = 2)
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnplus = Button(btnrow5, text="+", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btnplus_clicked, fg="white", bg="#333333", width = 2)
btnplus.pack(side=LEFT, expand=TRUE, fill=BOTH)



dot_btn = Button(btnrow5, text=" • ", font=("Times New Roman", 12," bold"),  relief=GROOVE, bd=5, command=dot_clicked, fg="white", bg="#333333", width = 2)
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn0 = Button(btnrow5, text="0", font=("Times New Roman", 12," bold"), relief=GROOVE, bd=5, command=btn0_clicked, fg="white", bg="#333333", width = 2)
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneval = Button(btnrow5, text="=",   font=("Times New Roman", 12," bold"),relief=GROOVE, bd=5, command=btneq_clicked, fg="white", bg="#333333", width = 7)
btneval.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
