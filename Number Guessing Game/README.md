# 🎯 Number Guessing Game

## 📌 Project Overview

Number Guessing Game is a simple beginner-level Python project.

In this game, the computer randomly chooses a number between **1 and 100**. The player has to guess the number.

After every guess, the program gives a hint:

* **Too low!** → The guessed number is smaller than the secret number.
* **Too high!** → The guessed number is larger than the secret number.
* **Correct!** → The guessed number is correct.

The game continues until the player guesses the correct number.

---

## 🛠️ Technologies Used

* Python
* Random Module

---

## 🎮 Features

* 🎲 Generates a random number between 1 and 100
* 🔢 Takes guesses from the user
* 📈 Gives "Too high" hints
* 📉 Gives "Too low" hints
* 🎉 Shows a congratulation message when the answer is correct
* 🔢 Counts the total number of attempts

---

## ⚙️ How It Works

1. The `random` module is imported.
2. The computer generates a random number between 1 and 100.
3. The user enters a guess.
4. The program compares the guess with the random number.
5. It displays:

   * "Too low!" if the guess is smaller.
   * "Too high!" if the guess is larger.
   * "Correct!" if the guess matches.
6. The number of attempts is increased after every guess.
7. The game stops when the correct number is guessed.

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the project in VS Code and run:

```bash
python number_guessing_game.py
```

---

## 📂 Project Structure

```text
Number_Guessing_Game/
│
├── number_guessing_game.py
└── README.md
```

---

## 💻 Example Output

```text
🎯 Number Guessing Game
I have chosen a number between 1 and 100.

Enter your guess: 40
Too low! Try again.

Enter your guess: 80
Too high! Try again.

Enter your guess: 65
🎉 Correct!

You guessed the number in 3 attempts.
```

---

## 📚 Concepts Learned

This project helped me practice:

* Variables
* `random.randint()`
* `input()`
* `if-elif-else`
* `while` loop
* `break`
* Counting attempts

---

## 🚀 Future Improvements

The project can be improved by adding:

* Maximum number of attempts
* Difficulty levels
* Score system
* Play Again option
* High Score
* Input validation

---

## 👩‍💻 Author

**Chhavi Laxkar**
BS in AI & Data Science
IIT Jodhpur
