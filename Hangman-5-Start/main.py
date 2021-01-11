import random
import hangman_words
import logo
import hangman_art

print(logo.logo)


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

print(f"\nSize of the Word is {word_length}")

end_of_game = False
lives = 6



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You Have Already Entered {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        print(f"{guess} letter is a wrong word!!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(hangman_art.stages[lives])