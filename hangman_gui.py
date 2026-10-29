
import random
import tkinter as tk


categories = {
    "Fruits": ["APPLE", "MANGO", "BANANA", "GRAPES", "ORANGE"],
    "Animals": ["TIGER", "ZEBRA", "RABBIT", "MONKEY", "LION"],
    "Colors": ["PURPLE", "YELLOW", "ORANGE", "GREEN", "BLUE"]
}

selected_word = random.choice(categories["Fruits"])
incorrect_guess = 0
max_incorrect_guess = 6
guessed_letters = []
display = ["_" for _ in selected_word]
game_over = False


root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x500")
root.configure(bg="#101827")
root.resizable(False, False)


label = tk.Label(
    root,
    text="Hangman Game",
    font=("Arial", 24, "bold"),
    bg="#101827",
    fg="#FBBF24"
)
label.pack(pady=(12, 5))


category_var = tk.StringVar(value="Fruits")

category_menu = tk.OptionMenu(
    root,
    category_var,
    *categories.keys()
)
category_menu.config(
    bg="#14B8A6",
    fg="#062D2B",
    font=("Arial", 12),
    relief="flat",
    cursor="hand2",
    highlightthickness=0
)
category_menu["menu"].config(
    bg="#1E293B",
    fg="#FFFFFF"
)
category_menu.pack(pady=5)


word_label = tk.Label(
    root,
    text=" ".join(display),
    font=("Courier", 24, "bold"),
    bg="#101827",
    fg="#14B8A6"
)
word_label.pack(pady=15)


attempts_label = tk.Label(
    root,
    text="Incorrect guesses: 0/6 | Remaining: 6",
    bg="#101827",
    fg="#FBBF24",
    font=("Arial", 12)
)
attempts_label.pack(pady=5)


guess_entry = tk.Entry(
    root,
    font=("Arial", 16),
    bg="#1E293B",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    relief="flat",
    justify="center"
)
guess_entry.pack(pady=8)


result_label = tk.Label(
    root,
    text="Enter a letter and click Guess",
    font=("Arial", 12),
    bg="#101827",
    fg="#FFFFFF"
)
result_label.pack(pady=5)


def check_guess():
    global incorrect_guess, game_over

    if game_over:
        return

    guess = guess_entry.get().strip().upper()
    guess_entry.delete(0, tk.END)

    
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Please enter a single letter.")
        return

    # Prevent repeated guesses
    if guess in guessed_letters:
        result_label.config(text="You already guessed that letter!")
        return

    guessed_letters.append(guess)

    
    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                display[i] = guess

        word_label.config(text=" ".join(display))
        result_label.config(text="Correct guess!", fg="#14B8A6")

    else:
        incorrect_guess += 1
        result_label.config(text="Wrong guess!", fg="#F87171")

    
    remaining_attempts = max_incorrect_guess - incorrect_guess

    attempts_label.config(
        text=f"Incorrect guesses: {incorrect_guess}/"
             f"{max_incorrect_guess} | Remaining: {remaining_attempts}"
    )

   
    if "_" not in display:
        result_label.config(text="You won! Great job!", fg="#14B8A6")
        game_over = True

    elif incorrect_guess >= max_incorrect_guess:
        result_label.config(
            text=f"You lost! The word was {selected_word}",
            fg="#F87171"
        )
        game_over = True


def restart_game():
    global selected_word, display, incorrect_guess, game_over

    # Choose a word from the selected category
    selected_category = category_var.get()
    selected_word = random.choice(categories[selected_category])

    # Reset game state
    display = ["_" for _ in selected_word]
    incorrect_guess = 0
    guessed_letters.clear()
    game_over = False

    # Reset the interface
    word_label.config(text=" ".join(display))
    attempts_label.config(
        text="Incorrect guesses: 0/6 | Remaining: 6"
    )
    result_label.config(
        text=f"New game: {selected_category}! Guess a letter.",
        fg="#FFFFFF"
    )
    guess_entry.delete(0, tk.END)
    guess_entry.focus_set()



button_frame = tk.Frame(root, bg="#101827")
button_frame.pack(pady=8)

guess_button = tk.Button(
    button_frame,
    text="Guess",
    font=("Arial", 12, "bold"),
    command=check_guess,
    bg="#14B8A6",
    fg="#062D2B",
    activebackground="#0D9488",
    activeforeground="#FFFFFF",
    relief="flat",
    cursor="hand2",
    width=10
)
guess_button.pack(side=tk.LEFT, padx=8)

restart_button = tk.Button(
    button_frame,
    text="Restart",
    font=("Arial", 12, "bold"),
    command=restart_game,
    bg="#FBBF24",
    fg="#422006",
    activebackground="#F59E0B",
    activeforeground="#101827",
    relief="flat",
    cursor="hand2",
    width=10
)
restart_button.pack(side=tk.LEFT, padx=8)


root.bind("<Return>", lambda event: check_guess())

guess_entry.focus_set()


root.mainloop()
