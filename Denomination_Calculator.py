from tkinter import *
from tkinter import messagebox  
from PIL import Image, ImageTk

t1 = Tk()
t1.title("DENOMINATION")
t1.geometry("500x500")

I1 = Image.open("A2.png")
I1 = ImageTk.PhotoImage(I1)

L1 = Label(t1, image=I1, height=300, width=300)
L1.pack()
L2 = Label(t1, text="HEY USER...!! WELCOME TO DENOMINATION COUNTER.\nHOW MAY I HELP YOU...???")
L2.pack()
E1=None
E2=None
E3=None
E4=None
E5=None
E6=None

def calculator():

  amount = int(E1.get())
  note_2000 = amount // 2000
  E2.insert(END, str(note_2000))
  amount = amount % 2000
  
  note_500 = amount // 500
  E3.insert(END, str(note_500))
  amount = amount % 500
  
  note_100 = amount // 100
  E4.insert(END, str(note_100))
  amount = amount % 100
  
  note_10 = amount // 10
  E5.insert(END, str(note_10))
  amount = amount % 10
  
  coin_1 = amount // 1
  E6.insert(END, str(coin_1))
  
  
def newwindow():
  global E1
  global E2
  global E3
  global E4
  global E5
  global E6
  new = Toplevel()
  new.title("COUNTER OF DENOMINATION")
  new.geometry("400x400")
  L3 = Label(new, text="ENTER THE AMOUNT")
  E1 = Entry(new)

  L4 = Label(new, text="HERE IS YOUR DENOMINATION COUNT")
  B2 = Button(new, text="CALCULATE", command=calculator)

  L5 = Label(new, text="NO. OF 2000/- NOTES :- ")
  L6 = Label(new, text="NO. OF 500/- NOTES :- ")
  L7 = Label(new, text="NO. OF 100/- NOTES :- ")
  L8 = Label(new, text="NO. OF 10/- NOTES :- ")
  L9 = Label(new, text="NO. OF 1/- COINS :- ")

  E2 = Entry(new)
  E3 = Entry(new)
  E4 = Entry(new)
  E5 = Entry(new)
  E6 = Entry(new)

  L3.pack()
  E1.pack()
  L4.pack()
  B2.pack()
  L5.pack()
  E2.pack()
  L6.pack()
  E3.pack()
  L7.pack()
  E4.pack()
  L8.pack()
  E5.pack()
  L9.pack()
  E6.pack()

  new.mainloop()

B1 = Button(t1, text="CLICK HERE TO CONTINUE", command=newwindow)
B1.pack()
t1.mainloop()
print()
