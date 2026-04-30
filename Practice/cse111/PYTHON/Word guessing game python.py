#word = str("workhard")
#word_length = len(word)
#for i in range(word_length):
#    print(word[i])
#Game Development
def generate_hint(secret, guess):
    hint = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            # Correct letter, correct position
            hint.append(guess[i].upper())
        elif guess[i] in secret:
            # Correct letter, wrong position
            hint.append(guess[i].lower())
        else:
            # Letter not in word
            hint.append("_")
    return "".join(hint)

def play_game():
    # You can change this secret word to anything you like
    secret_word = "python"
    word_length = len(secret_word)
    guesses_made = 0
    
    print("--- Welcome to the Word Guessing Game! ---")
    print(f"Your hint: {'_ ' * word_length}")

    while True:
        user_guess = input("Enter your guess: ").strip().lower()
        
        # Rule: Guess must be the same length
        if len(user_guess) != word_length:
            print(f"Your guess must be {word_length} letters long.")
            continue
        
        guesses_made += 1

        # Check for win
        if user_guess == secret_word:
            print(f"Congratulations! You guessed it!")
            print(f"It took you {guesses_made} guesses.")
            break
        else:
            # Generate and display hint
            hint = generate_hint(secret_word, user_guess)
            print(f"Your hint is: {hint}")

if __name__ == "__main__":
    play_game()
