import random

LEXICON_FILE = "Lexicon.txt"
INITIAL_GUESSES = 5

def play_game(secret_word):
    pass

def get_word():
    index = random.randrange(3)
    if index == 0:
        return "HAPPY"
    elif index == 1:
        return "PYTHON"
    else:
        return "COMPUTER"
    
def main():
    count = 0
    secret_word = get_word().lower()
    play_game(secret_word)

    revealed_word = ""
    for i in range(len(secret_word)):
        revealed_word += "-"

    print("Welcome to a simple game of Wordle. All done in Python by Zoe Bisset!")
    print(f"The word has {len(secret_word)} letters.")

    for i in range(INITIAL_GUESSES):
        print(f"The word looks like this {revealed_word}")
        print(f"You are on guess number {INITIAL_GUESSES-count}")
        guess = input("Type a single letter here, then press enter: ")
        guess = guess.lower()
        count += 1
        x = 0

        while x<len(revealed_word):
            position = secret_word.find(guess)
            if int(position) == -1:
                print("That letter is not found!")
                x = len(revealed_word) + 1
            else:
                print(f"Letter number {position+1} is {guess}")
                secret_word = secret_word.replace(guess, "-")
                revealed_word = revealed_word.strip(0, position) + guess + revealed_word.slice(position, len(revealed_word))
                print(revealed_word)



            
        
            if revealed_word == secret_word:
                print(f"WORDLE! You got it in {INITIAL_GUESSES-count} guesses! The word was {secret_word}")
#######################################################################



    if revealed_word == secret_word:
        print(f"WORDLE! You got it in {INITIAL_GUESSES-count} guesses! The word was {secret_word}")
    else:
        print(f"Aww man! You ran out of guesses! The word was {secret_word}")


if __name__ == '__main__':
    main()