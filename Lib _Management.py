class LIBRARY:

  def __init__(self, book_list, name):
    self.book_list = book_list
    self.name = name
    self.lendbook = {}
    print(self.name)

  def display(self):
    print('  ')
    print("THE FOLLOWING BOOKS ARE PRESENT IN OUR LIBRARY :- ")
    print('  ')
    for i in self.book_list:
      print(i)

  def lendingbook(self, book, name):
    if book not in self.lendbook:
      self.lendbook.update({book: name})
      print(" ")
      print("LIST IS UPDATED. YOU CAN TAKE THIS BOOK")
      print(self.lendbook)
    else:
      print(' ')
      print("BOOK IS NOT AVAILABLE")

  def addbook(self, book):
    if book not in self.book_list:
      self.book_list.append(book)
      print("BOOK ADDED SUCCESFULLY")
      print(" ")
      print(self.book_list)
    else:
      print("BOOK IS ALREADY PRESENT IN THE LIBRARY")

  def returnbook(self, book):
    if book in self.lendbook:
      self.book_list.append(book)
      print("BOOK RETURNED SUCCESSFULLY")
      print(" ")
      print(self.book_list)
    elif book not in self.lendbook and self.book_list:
      print("BOOOK IS NOT IN LIBRARY. PLEASE ENTER THE CORRECT NAME")
    else:
      print("BOOK IS ALREADY THERE")


S = LIBRARY([
    "HARRY POTTER", "IT ENDS WITH US", "IT STARTS WITH US", "IKIGAI",
    "YOU'VE REACHED SAM", "TWISTED LOVE", "TWISTED HATE", "TWISTED GAMES",
    "TWISTED LIES", "RAMAYAN", "MAHABHARAT", "THE GIRL WHO KNEW TOO MUCH",
    "THE GIRL WHO DISAPPEARED"
], "THE DAYDREAM LIBRARY")
while True:
  print(" ")
  print("⭐⭐⭐ WELCOME TO OUR THE DAYDREAM LIBRARY ⭐⭐⭐".center(40))
  print(" ")
  print("ENTER YOUR CHOICE TO CONTINUE")
  print('''1. DISPLAY BOOKS''')
  print('''2. LEND BOOK''')
  print('''3. ADD A BOOK''')
  print('''4. RETURN A BOOK''')
  print('''OR PRESS [Q] TO QUIT''')

  choice = input("ENTER YOUR CHOICE :- ")
  if choice == '1':
    S.display()

  elif choice == '2':
    print(" ")
    book = input("ENTER THE BOOK YOU WANT TO LEND :- ")
    name = input("ENTER YOUR NAME :- ")
    S.lendingbook(book, name)

  elif choice == '3':
    print(" ")
    book = input("ENTER THE BOOK YOU WANT TO ADD :- ")
    S.addbook(book)

  elif choice == '4':
    print(" ")
    book = input("ENTER THE BOOK YOU WANT TO RETURN :- ")
    S.returnbook(book)

  elif choice == "Q":
    print("⭐⭐⭐ THANK YOU FOR VISITING. COME BACK AGAIN ⭐⭐⭐".center(40))
    exit()

  else:
    print("INVALID. PLEASE CHOOSE FROM THE GIVEN MENU")
