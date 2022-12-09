import tkinter as tk
import random
import time


def show_frames():
    frame1 = tk.Frame(win, bg='pink')
    frame1.place(x=50, y=200, width=100, height=100)

    frame2 = tk.Frame(win, bg='pink')
    frame2.place(x=175, y=200, width=100, height=100)

    frame3 = tk.Frame(win, bg='pink')
    frame3.place(x=300, y=200, width=100, height=100)


def show_number1():
    rn1 = random_number()
    num1 = tk.Label(win, text=str(rn1), font=10)
    num1.place(x=50, y=200, width=100, height=100)
    return rn1


def show_number2():
    rn2 = random_number()
    num2 = tk.Label(win, text=str(rn2), font=10)
    num2.place(x=175, y=200, width=100, height=100)
    return rn2


def show_number3():
    rn3 = random_number()
    num3 = tk.Label(win, text=str(rn3), font=10)
    num3.place(x=300, y=200, width=100, height=100)
    return rn3


MONEY = 3000


def buttclick():
    global MONEY

    lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
    lblmoney.place(x=300, y=10)
    win.update()
    lblmoney.place(x=300, y=10)
    d = int(ent.get())
    lab1 = tk.Label(win, text='Your bet ', font=10)
    lab1.configure(text='Your bet ' + str(d), font=10)
    lab1.place(x=50, y=150, width=200)

    lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
    lblmoney.place(x=300, y=10)
    win.update()
    return d


def buttclick2():
    global MONEY
    for i in range(10):
        show_frames()
        win.update()
        a = show_number1()

        win.update()
        win.update()
        b = show_number2()

        win.update()
        c = show_number3()
        win.update()

    lblnum = tk.Label(win, text='Your Number ' + str(a) + str(b) + str(c), font=10)
    lblnum.place(x=50, y=300)
    B = []
    A = [a, b, c]
    for i in A:
        B.append(int(i))
    lblwon = tk.Label(win, text='                                                                           ', font=10)
    lblwon.place(x=50, y=350)
    if (B[0] == B[1] or B[0] == B[2] or B[1] == B[2]) and (B[0] != B[1] or B[0] != B[2] or B[1] != B[2]):

        lblwon = tk.Label(win, text='You won x2 bet', font=20)
        lblwon.place(x=50, y=350)
        MONEY += buttclick() * 2
        lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
        lblmoney.place(x=300, y=10)
        win.update()
    elif B[0] == B[1] == B[2] == 7:
        lblwon = tk.Label(win, text='You won JackPot!!!!', font=50)
        lblwon.place(x=50, y=350)
        MONEY += buttclick() * 100
        lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
        lblmoney.place(x=300, y=10)
        win.update()
    elif B[0] == B[1] == B[2] and B[0] != 7:
        lblwon = tk.Label(win, text='You won mini-JackPot!', font=50)
        lblwon.place(x=50, y=350)
        MONEY += buttclick() * 20
        lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
        lblmoney.place(x=300, y=10)
        win.update()
    else:
        lblwon = tk.Label(win, text='You loser', font=10)
        lblwon.place(x=50, y=350)
        MONEY -= buttclick()
        lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
        lblmoney.place(x=300, y=10)
        win.update()


def random_number():
    return random.randint(0, 9)


# def random_numbers():
#     a = [0, 0, 0]
#     for i in range(3):
#         for j in range(10):
#             time.sleep(0.08)
#             a[i] = random.randint(0, 9)
#     return a


win = tk.Tk()
win.title('Casino')
win.configure(width=600, height=600)
win.resizable(False, False)

lbl1 = tk.Label(win, text='Enter your bet', font=10)
lbl1.place(x=50, y=10)
lblmoney = tk.Label(win, text='Your money:' + str(MONEY), font=10)
lblmoney.place(x=300, y=10)
win.update()

ent = tk.Entry(win, bd=2)
ent.place(x=50, y=50, width=100)

but = tk.Button(win, text='Accept', command=buttclick)
but.place(x=50, y=100, width=200)

but2 = tk.Button(win, text='PLAY', command=buttclick2)
but2.place(x=250, y=100, width=200)

show_frames()

win.mainloop()
