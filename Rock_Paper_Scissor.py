import random
from tkinter import *
from tkinter import messagebox

T1 = Tk()
T1.title("ROCK PAPER SCISSOR GAME")
T1.geometry("500x500")
T1.config(bg="black")

L1 = Entry(T1, bg="red", fg="black")
L1.pack()

comp1 = Label(T1, bg="red", fg="black")
comp1.pack()


def select():

    user = L1.get().strip().upper()

    ch = ["ROCK", "PAPER", "SCISSOR"]
    comp = random.choice(ch)

    if user not in ch:
        messagebox.showinfo('result', 'Please enter ROCK, PAPER, or SCISSOR')
        return

    if comp == user:
        messagebox.showinfo('result', 'Its a draw')

    elif comp == "ROCK" and user == "PAPER":
        messagebox.showinfo('result', 'User wins')
    elif comp == "ROCK" and user == "SCISSOR":
        messagebox.showinfo('result', 'Computer wins')

    elif comp == "PAPER" and user == "SCISSOR":
        messagebox.showinfo('result', 'User wins')
    elif comp == "PAPER" and user == "ROCK":
        messagebox.showinfo('result', 'Computer wins')
    elif comp == "SCISSOR" and user == "ROCK":
        messagebox.showinfo('result', 'User wins')
    elif comp == "SCISSOR" and user == "PAPER":
        messagebox.showinfo('result', 'Computer wins')


    comp1.config(text=comp)


L2 = Button(T1, text="CLICK TO PLAY", bg="blue", fg="black", command=select)
L2.pack()

T1.mainloop()
