
import random

# 1 = Snake, -1 = Water, 0 = Gun

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reversedDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

user_score = 0
computer_score = 0

while True:
    print("\n--- Snake Water Gun Game ---")
    print("s = Snake, w = Water, g = Gun")
    print("q = Quit")

    youstr = input("Enter your choice: ").lower()

    if youstr == "q":
        break

    if youstr not in youDict:
        print("Invalid choice! Try again.")
        continue

    you = youDict[youstr]
    computer = random.choice([1, -1, 0])

    print(f"You chose: {reversedDict[you]}")
    print(f"Computer chose: {reversedDict[computer]}")

    if you == computer:
        print("It's a Draw!")

    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score: You {user_score} - Computer {computer_score}")

print("\n--- Final Score ---")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Computer won the game!")
else:
    print("The game is a draw!")
