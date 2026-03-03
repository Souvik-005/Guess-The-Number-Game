import tkinter as tk
import random
number_to_guess = random.randint(1, 100)
attempts = 0

def check_guess():
    global number_to_guess, attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < number_to_guess:
            result.set("It's higher than this.")
        elif guess > number_to_guess:
            result.set("It's lower than this.")
        else:
            result.set(f"You guessed it correct! The number is {number_to_guess}.\nAttempts: {attempts}")
    except ValueError:
        result.set("Please enter a valid number.")

def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    result.set("New game started! Guess a number between 1 and 100.")
    entry.delete(0, tk.END)

# Create the window
window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("400x250")

# Heading
tk.Label(window, text="Guess the Number (1 - 100)", font=("Helvetica", 16)).pack(pady=10)

# Input field
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=5)

# Buttons
tk.Button(window, text="Check", font=("Helvetica", 12), command=check_guess).pack(pady=5)
tk.Button(window, text="Reset Game", font=("Helvetica", 12), command=reset_game).pack(pady=5)

# Result label
result = tk.StringVar()
result.set("Enter your guess and click Check.")
tk.Label(window, textvariable=result, font=("Helvetica", 12), wraplength=350, justify="center").pack(pady=20)

# Start the GUI loop
window.mainloop()
