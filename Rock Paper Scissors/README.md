# 🪨📄✂️ Rock Paper Scissors Game

## 📌 Project Overview

Rock Paper Scissors is a simple beginner-level Python game where the player plays against the computer.

The player chooses **Rock, Paper, or Scissors**, while the computer randomly selects one of the three choices.

The program then compares both choices and displays whether the player **wins, loses, or gets a tie**.

---

## 🛠️ Technologies Used

* Python
* Random Module

---

## 🎮 Features

* 🪨 Rock
* 📄 Paper
* ✂️ Scissors
* 🤖 Computer makes a random choice
* 🏆 Win, Lose, and Tie results
* ❌ Invalid input handling
* 🔄 Option to play multiple rounds
* 😊 Emoji-based choices

---

## ⚙️ How the Game Works

1. The player is asked to choose:

   * `r` → Rock 🪨
   * `p` → Paper 📄
   * `s` → Scissors ✂️

2. The computer randomly chooses Rock, Paper, or Scissors.

3. The program displays both choices.

4. The winner is decided using the following rules:

```text
Rock 🪨 beats Scissors ✂️
Scissors ✂️ beats Paper 📄
Paper 📄 beats Rock 🪨
```

5. If both choices are the same, the result is a **Tie**.

6. After each round, the player can choose whether to continue playing.

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the project in VS Code and run:

```bash
python rock_paper_scissors.py
```

---

## 📂 Project Structure

```text
Rock_Paper_Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

---

## 💻 Example Output

```text
Choose Rock,Paper,Scissors ? (r/p/s): r

You choose 🪨
Computer choose ✂️

You win!

Continue? (y/n): y
```

Another example:

```text
Choose Rock,Paper,Scissors ? (r/p/s): p

You choose 📄
Computer choose 📄

Tie!

Continue? (y/n): n
```

---

## 📚 Concepts Learned

This project helped me practice:

* Variables
* Dictionaries
* Tuples
* `random.choice()`
* `input()`
* `.lower()`
* `if-elif-else`
* `while` loop
* `continue`
* `break`
* Conditional operators
* User input validation

---

## 👩‍💻 Author

**Chhavi Laxkar**
BS in AI & Data Science
IIT Jodhpur
