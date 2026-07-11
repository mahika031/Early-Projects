# Early-Projects
A collection of my beginner Python projects created while learning programming in Class 11. These projects helped me build a strong foundation in Python, covering concepts like functions, loops, conditional statements, and basic GUI development





1. The Daydream Library — Library Management System📚 
A simple command-line Library Management System built in Python using Object-Oriented Programming. I wrote this project during Class 11th as one of my first hands-on attempts at applying OOP concepts in Python. I'm uploading it now as a record of where I started. 

✨Features
- Display Books — View all books currently available in the library
- Lend a Book — Borrow a book by entering the book name and your name
- Add a Book — Add a new book to the library's collection
- Return a Book — Return a borrowed book back to the library
- Simple, menu-driven console interface that runs in a loop until you quit

🔧 Possible Future Improvements
- Remove a book from book_list once it's lent out (currently it stays listed even while lent)
- Add persistent storage (e.g., save/load the library to a file or database)
- Add input validation for edge cases
- Build a GUI version using Tkinter





2. Denomination Counter 💵 
A simple GUI-based Denomination Calculator built in Python using Tkinter. Given an amount, it breaks it down into the minimum number of ₹2000, ₹500, ₹100, and ₹10 notes, plus ₹1 coins needed to make up that amount. 

✨Features
- Welcome screen with a greeting message
- A second window (opened via button click) where you enter an amount
- Instantly calculates and displays the required count of:
      ₹2000 notes
      ₹500 notes
      ₹100 notes
      ₹10 notes
      ₹1 coins

🔧 Known Issues / Possible Future Improvements
- Clicking "CALCULATE" more than once adds the new result to the old one instead of replacing it. The result boxes should be cleared before showing a new result.
- If the user enters text or leaves the amount box empty, the program crashes. Input checking should be added.
- PIL (Image, ImageTk) is imported but not used. It can be removed if no image is needed.
- There is an extra mainloop() in the code that is not needed. Only one mainloop() is required.
- A better message can be shown if the user enters 0 or a negative amount.





3. Rock Paper Scissor Game✊✋✌️ 
A simple GUI-based Rock Paper Scissors game built in Python using Tkinter. Type your move, click the button, and play a single round against the computer. 

✨Features
- Type your move (ROCK, PAPER, or SCISSOR) into a text box
- Computer randomly picks its move
- Instantly shows the result (win, lose, or draw) in a popup
- Displays the computer's chosen move on screen after each round
- Handles invalid input gracefully with a friendly prompt

🔧 Possible Future Improvements
- Add score tracking across multiple rounds instead of resetting each time
- Replace the text entry with clickable buttons/icons for each move (more intuitive than typing)
- Add images or emojis for Rock/Paper/Scissor instead of plain text
- Add a "Play Again" / "Reset" button
