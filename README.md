# 🎮 TriClash-Game

**A Python-based Snake, Water, Gun game where you challenge the computer!**

TriClash is a simple command-line game built with Python. Choose Snake, Water, or Gun and compete against the computer, which randomly selects its move.

## 🚀 Features

- 🎲 Random computer choices using Python's `random` module
- 🐍 Three game options: Snake, Water, and Gun
- 🏆 Automatic winner and draw detection
- ⌨️ Simple command-line interface
- 🧠 Beginner-friendly Python project

## 🛠️ Technologies Used

- Python 3
- `random` module

## 📂 Project Structure

```text
TriClash-Game/
└── snake_water_gun/
    └── game.py
```

## 🎯 Game Rules

| Choice | Beats |
|---|---|
| 🐍 Snake | 💧 Water |
| 💧 Water | 🔫 Gun |
| 🔫 Gun | 🐍 Snake |

- If both players choose the same option, it's a draw.
- Otherwise, the winner is decided by the rules above.

## 💻 How to Run

**1. Clone the repository**

```bash
git clone https://github.com/harshit9934/TriClash-Game.git
```

**2. Navigate to the project folder**

```bash
cd TriClash-Game/snake_water_gun
```

**3. Run the game**

```bash
python game.py
```

If `python` doesn't work on your system, try:

```bash
py game.py
```

## 🎮 How to Play

1. Run the Python file in your terminal.
2. Enter your choice when prompted.
3. The computer randomly selects its choice.
4. See who wins!

## 📚 What I Learned

- Using Python's `random` module
- Taking user input with `input()`
- Working with dictionaries
- Implementing conditional statements (`if`, `elif`, `else`)
- Applying basic game logic

## 🔮 Future Improvements

- Add multiple rounds and score tracking
- Add input validation
- Create a graphical user interface (GUI)
- Add sound effects and animations

## 👨‍💻 Author

**Harshit Maurya**

- GitHub: [@harshit9934](https://github.com/harshit9934)

---

⭐ If you like this project, consider giving the repository a star!

*Built with Python ❤️*
